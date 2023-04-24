from setuptools import setup

setup(
    packages=['ciofs_hindcast_report.src'],
    use_scm_version={
        "write_to": "src/_version.py",
        "write_to_template": '__version__ = "{version}"',
        "tag_regex": r"^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$",
    }
)
