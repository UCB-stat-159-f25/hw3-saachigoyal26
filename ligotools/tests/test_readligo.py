import numpy as np
from ligotools import readligo as rl
import os
import pathlib

def test_loaddata_returns_expected_keys():
    """Check that readligo.loaddata returns correct types."""
    fname = str(pathlib.Path(__file__).parents[2] / "data" / "H1_LOSC_4_V1-1126259446-32.hdf5")
    strain, time, chan_dict = rl.loaddata(fname, 'H1')
    assert isinstance(strain, np.ndarray)
    assert isinstance(time, np.ndarray)
    assert isinstance(chan_dict, dict)
    assert 'DATA' in chan_dict.keys()

def test_loaddata_time_increases_monotonically():
    """Ensure time array is strictly increasing."""
    fname = str(pathlib.Path(__file__).parents[2] / "data" / "H1_LOSC_4_V1-1126259446-32.hdf5")
    _, time, _ = rl.loaddata(fname, 'H1')
    assert np.all(np.diff(time) > 0)