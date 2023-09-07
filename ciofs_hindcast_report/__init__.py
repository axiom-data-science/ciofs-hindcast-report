
import ciofs_hindcast_report.src.process
import ciofs_hindcast_report.src.utils
import ciofs_hindcast_report.src.plot_dataset_on_map
import ciofs_hindcast_report.src.generate_catalogs
import ciofs_hindcast_report.src.generate_data_pages
import ciofs_hindcast_report.src.generate_comparison_pages

import cf_xarray as cfx
import cf_pandas as cfp

import pathlib
base = pathlib.Path(__path__[0])

PATH_INPUTS = base / "inputs"
PATH_INPUTS_RIVER = PATH_INPUTS / "river"
PATH_INPUTS_DATA = PATH_INPUTS / "data"

PATH_OUTPUTS = base / "outputs"
PATH_OUTPUTS_RIVER = PATH_OUTPUTS / "river"
PATH_OUTPUTS_CATALOGS = PATH_OUTPUTS / "catalogs"
PATH_OUTPUTS_DATA_CACHE = PATH_OUTPUTS / "data_cache"
PATH_OUTPUTS_PAGES = PATH_OUTPUTS / "pages"
PATH_OUTPUTS_DATA_PAGES = PATH_OUTPUTS_PAGES / "data"
PATH_OUTPUTS_COMP_PAGES = PATH_OUTPUTS_PAGES / "comparison"

PATH_REPORT = base / "report"

# make directories
PATH_OUTPUTS.mkdir(parents=True, exist_ok=True)
PATH_OUTPUTS_RIVER.mkdir(parents=True, exist_ok=True)
PATH_OUTPUTS_CATALOGS.mkdir(parents=True, exist_ok=True)
PATH_OUTPUTS_PAGES.mkdir(parents=True, exist_ok=True)
PATH_OUTPUTS_DATA_PAGES.mkdir(parents=True, exist_ok=True)
PATH_OUTPUTS_COMP_PAGES.mkdir(parents=True, exist_ok=True)
PATH_OUTPUTS_DATA_CACHE.mkdir(parents=True, exist_ok=True)

def CAT_NAME(slug):
    return (PATH_OUTPUTS_CATALOGS / slug).with_suffix(".yaml")

def DATA_PAGE_PATH(slug):
    return PATH_OUTPUTS_DATA_PAGES / slug

def COMP_PAGE_DIR(slug):
    path = PATH_OUTPUTS_COMP_PAGES / slug
    path.mkdir(parents=True, exist_ok=True)
    return path


# Global parameters
annotate_fontsize=12
suptitle_fontsize=16
figsize=(10,6)
map_font_size=14
cmap = {}
cmap["salt"] = "cmo.haline"
cmap["temp"] = "cmo.thermal"
cmap["u"] = "cmo.delta"
cmap["diff"] = "cmo.balance"
cmap["speed"] = "cmo.tempo"
extent_whole = [-156.5, -148.5, 56.3, 61.5]

# Comprehensive list of dataset slugs
# used for catalog generation. Are used for data page generation if "included" in catalog metadata.
slugs = [
        "adcp_moored_noaa_coi_2005",
        "adcp_moored_noaa_coi_other",
        "adcp_moored_noaa_kod_1",
        "adcp_moored_noaa_kod_2",
        "adcp_towed_otf_kbnerr",
        "ctd_moored_circac",
        "ctd_moored_kbnerr",
        "ctd_profiles_2005_noaa",
        "ctd_profiles_2005_osu",
        "ctd_profiles_emap_2002",
        "ctd_profiles_emap_2008",
        "ctd_profiles_kachemack_kuletz_2005_2007",
        "ctd_profiles_kb_small_mesh_2006",
        "ctd_profiles_kbay_osu_2007",
        "ctd_profiles_north_gulf_small_mesh_2005",
        "ctd_profiles_piatt_speckman_1999",
        "ctd_profiles_usgs_boem",
        "ctd_towed_otf_kbnerr",
        "ctd_towed_ferry_noaa_pmel",
        "ctd_towed_gwa",
        "ctd_towed_gwa_temp",
        "ctd_transects_barabara_to_bluff_2002_2003",
        "ctd_transects_cmi_kbnerr",
        "ctd_transects_cmi_uaf",
        "ctd_transects_gwa",
        "ctd_transects_misc_2002",
        "ctd_transects_otf_kbnerr",
        "ctd_transects_uaf",
        "hfradar",
        "moorings_aoos_cdip",
        "moorings_kbnerr_bear_cove_seldovia",
        "moorings_kbnerr_historical",
        "moorings_kbnerr_homer",
        "moorings_noaa",
        "moorings_nps",
        "moorings_uaf",
        "surface_otf_adfg",
         ]

# Set up vocab for universal usage
vocab = cfp.Vocab()

# Make an entry to add to your vocabulary
reg = cfp.Reg(include="tem", exclude=["F_","qc","air","dew"], ignore_case=True)
vocab.make_entry("temp", reg.pattern(), attr="name")
reg = cfp.Reg(include="sal", exclude=["F_","qc"], ignore_case=True)
vocab.make_entry("salt", reg.pattern(), attr="name")
vocab.make_entry("speed", ["speed","s$"], attr="name")
vocab.make_entry("dir", ["dir","d$"], attr="name")
reg = cfp.Reg(include_or=["sea_surface_height","zeta"], exclude=["qc","sea_surface_height_amplitude_due_to_geocentric_ocean_tide_geoid_mllw"], ignore_case=True)
vocab.make_entry("ssh", reg.pattern(), attr="name")

reg = cfp.Reg(include="along", exclude=["subtidal"], ignore_case=True)
vocab.make_entry("along", reg.pattern(), attr="name")
reg = cfp.Reg(include="across", exclude=["subtidal"], ignore_case=True)
vocab.make_entry("across", reg.pattern(), attr="name")

# reg = cfp.Reg(include="u$", ignore_case=True)
# vocab.make_entry("u", reg.pattern(), attr="name")
# NEED TO DO U VS. EASTWARD
reg = cfp.Reg(include_or=["eastward_sea_water_velocity","sea_water_x_velocity"], ignore_case=True)
vocab.make_entry("u", reg.pattern(), attr="standard_name")

# reg = cfp.Reg(include="v$", ignore_case=True)
# vocab.make_entry("v", reg.pattern(), attr="name")
# THESE TWO NEED TO BE SEPARATED LATER!!
reg = cfp.Reg(include_exact="u", ignore_case=True)
vocab.make_entry("east", reg.pattern(), attr="name")
reg = cfp.Reg(include_exact="u_eastward", ignore_case=True)
vocab.make_entry("east", reg.pattern(), attr="name")
# reg = cfp.Reg(include_or=["sea_water_x_velocity"], ignore_case=True)
# vocab.make_entry("east", reg.pattern(), attr="standard_name")

reg = cfp.Reg(include_exact="v", ignore_case=True)
vocab.make_entry("north", reg.pattern(), attr="name")
reg = cfp.Reg(include_exact="v_northward", ignore_case=True)
vocab.make_entry("north", reg.pattern(), attr="name")
# reg = cfp.Reg(include_or=["sea_water_y_velocity"], ignore_case=True)
# vocab.make_entry("north", reg.pattern(), attr="standard_name")



vocab.make_entry("jday", ["julian", "yearday"], attr="name")  # julian or decimal days
vocab.make_entry("station", ["station", "Station"], attr="name")
vocab.make_entry("transect", ["transect","line"], attr="name")
vocab.make_entry("cruise", ["cruise", "Cruise"], attr="name")
vocab.make_entry("distance", ["distance"], attr="name")

# vocab.make_entry("longitude", ["(?i)x?(?=.*lon)[a-z0-9]*"], attr="name")
# vocab.make_entry("latitude", ["(?i)x?(?=.*lat)[a-z0-9]*"], attr="name")


cfp.set_options(custom_criteria=vocab.vocab)
cfx.set_options(custom_criteria=vocab.vocab)
