import pytest
from xnemogcm import open_namelist

pytestmark = pytest.mark.parametrize("data_path", ["4.0.0"], indirect=True)


def test_open_namelist_cfg(data_path):
    """Test opening the namelist_cfg"""
    namcfg = open_namelist(data_path / "namelist", cfg=True, ref=False)
    assert "rn_e1_deg" in namcfg
    assert namcfg["cn_exp"] == "BASIN"
    assert "nn_it000" not in namcfg


def test_open_namelist_ref(data_path):
    """Test opening the namelist_ref"""
    namref = open_namelist(data_path / "namelist", cfg=False, ref=True)
    assert "rn_e1_deg" not in namref
    assert namref["cn_exp"] == "ORCA2"


def test_open_namelist_merge(data_path):
    """
    Test opening the namelist_ref and namelist_ref, merging and replacing
    with the values from namelist_cfg when necessary
    """
    namelist = open_namelist(data_path / "namelist")
    assert "rn_e1_deg" in namelist
    assert namelist["cn_exp"] == "BASIN"
    assert namelist["nn_it000"] == 1


def test_warning(data_path):
    """Test that warnings are raised"""
    with pytest.warns(UserWarning):
        open_namelist(data_path, cfg=True, ref=False)
    with pytest.warns(UserWarning):
        open_namelist(data_path, cfg=False, ref=True)
