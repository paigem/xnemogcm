import numpy as np
import xarray as xr
from pathlib import Path
import os


def get_domcfg_points():
    """The points are hard coded at hand to be sure to not introduce errors from the reading of the names"""
    domcfg_points = {
        "nav_lon": "T",
        "nav_lat": "T",
        "jpiglo": None,
        "jpjglo": None,
        "jpkglo": None,
        "jperio": None,
        "ln_zco": None,
        "ln_zps": None,
        "ln_sco": None,
        "ln_isfcav": None,
        "glamt": "T",
        "glamu": "U",
        "glamv": "V",
        "glamf": "F",
        "gphit": "T",
        "gphiu": "U",
        "gphiv": "V",
        "gphif": "F",
        "e1t": "T",
        "e1u": "U",
        "e1v": "V",
        "e1f": "F",
        "e2t": "T",
        "e2u": "U",
        "e2v": "V",
        "e2f": "F",
        "ff_f": "F",
        "ff_t": "T",
        "e3t_1d": "T",
        "e3w_1d": "W",
        "e3t_0": "T",
        "e3u_0": "U",
        "e3v_0": "V",
        "e3f_0": "F",
        "e3w_0": "W",
        "e3uw_0": "UW",
        "e3vw_0": "VW",
        "top_level": "T",
        "bottom_level": "T",
        "stiffness": "T",
        "gdept_0": "T",
        "gdepw_0": "W",
        "gdepu": "U",
        "gdepv": "V",
        "ht_0": "T",
        "hu_0": "U",
        "hv_0": "V",
        "tmask": "T",
        "umask": "U",
        "vmask": "V",
        "fmask": "F",
        "tmaskutil": "T",
        "umaskutil": "U",
        "vmaskutil": "V",
        "gdept_1d": "T",
        "gdepw_1d": "W",
        "mbathy": "T",
        "misf": "T",
        "isfdraft": "T",
    }
    return domcfg_points
