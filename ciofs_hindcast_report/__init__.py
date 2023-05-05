
import ciofs_hindcast_report.src.process
import ciofs_hindcast_report.src.utils
import ciofs_hindcast_report.src.plot_dataset_on_map
import ciofs_hindcast_report.src.generate_catalogs
import ciofs_hindcast_report.src.generate_data_pages

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
PATH_OUTPUTS_PAGES = PATH_OUTPUTS / "pages"
PATH_OUTPUTS_DATA_PAGES = PATH_OUTPUTS_PAGES / "data"

PATH_REPORT = base / "report"

# make directories
PATH_OUTPUTS.mkdir(parents=True, exist_ok=True)
PATH_OUTPUTS_RIVER.mkdir(parents=True, exist_ok=True)
PATH_OUTPUTS_CATALOGS.mkdir(parents=True, exist_ok=True)
PATH_OUTPUTS_PAGES.mkdir(parents=True, exist_ok=True)
PATH_OUTPUTS_DATA_PAGES.mkdir(parents=True, exist_ok=True)

def CAT_NAME(slug):
    return (PATH_OUTPUTS_CATALOGS / slug).with_suffix(".yaml")

def DATA_PAGE_PATH(slug):
    return PATH_OUTPUTS_DATA_PAGES / slug


# Global parameters
annotate_fontsize=12
suptitle_fontsize=16
figsize=(10,6)
map_font_size=14
cmap = {}
cmap["salt"] = "cmo.haline"
cmap["temp"] = "cmo.thermal"
cmap["u"] = "cmo.delta"
extent_whole = [-156.5, -148.5, 56.3, 61.5]

# Comprehensive list of dataset slugs
# used for catalog generation. Are used for data page generation if "included" in catalog metadata.
slugs = [
        "moorings_uaf",
        "moorings_nps",
        "moorings_noaa",
        "moorings_aoos_cdip",
        "moorings_kbnerr_bear_cove_seldovia",
        "moorings_kbnerr_homer",
        "ctd_profiles_gwa",
        "ctd_profiles_2005_noaa",
        "ctd_profiles_usgs_boem",
        "ctd_towed_otf_kbnerr",
        "ctd_towed_ferry_noaa_pmel",
        "ctd_profiles_otf_kbnerr",
        "ctd_profiles_cmi_uaf",
        "ctd_profiles_cmi_kbnerr",
        "ctd_moored_circac",
        "ctd_moored_kbnerr",
        "ctd_time_series_uaf",
        "ctd_profiles_2005_osu",
        "ctd_towed_gwa",
        "temp_towed_gwa",
        "surface_otf_adfg",
        "moorings_kbnerr_historical",
        "adcp_moored_noaa_coi_2005",
        "adcp_moored_noaa_coi_other",
        "adcp_moored_noaa_kod_1",
        "adcp_moored_noaa_kod_2",
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
reg = cfp.Reg(include="sea_surface_height", exclude=["qc","sea_surface_height_amplitude_due_to_geocentric_ocean_tide_geoid_mllw"], ignore_case=True)
vocab.make_entry("ssh", reg.pattern(), attr="name")


vocab.make_entry("jday", ["julian", "yearday"], attr="name")  # julian or decimal days
vocab.make_entry("station", ["station", "Station"], attr="name")
vocab.make_entry("transect", ["transect","line"], attr="name")
vocab.make_entry("cruise", ["cruise", "Cruise"], attr="name")
vocab.make_entry("distance", ["distance"], attr="name")

# vocab.make_entry("longitude", ["(?i)x?(?=.*lon)[a-z0-9]*"], attr="name")
# vocab.make_entry("latitude", ["(?i)x?(?=.*lat)[a-z0-9]*"], attr="name")


cfp.set_options(custom_criteria=vocab.vocab)
cfx.set_options(custom_criteria=vocab.vocab)
