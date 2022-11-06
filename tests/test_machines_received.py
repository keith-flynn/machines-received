import pytest
import machines_received as mr

def test_for_clean_row():
    """Correctly cleans processor data."""
    assert mr.simple_i('3010-D-I5QC') == '3010-D-I5'
    assert mr.simple_i('7060-M-I7HC') == '7060-M-I7'
    assert mr.simple_i('3020-M-I3DCSODA') == '3020-M-I3'

def test_for_skipping_procs():
    """Correctly ignores non-intel naming conventions"""
    assert mr.simple_i('705G4-M-AMDQC') == '705G4-M-AMDQC'
    assert mr.simple_i('M58-U-C2D') == 'M58-U-C2D'
    assert mr.simple_i('705G1-M-AMD') == '705G1-M-AMD'

def test_bad_input_type_raises_error():
    """Fails if non-string is used."""
    with pytest.raises(AttributeError):
        mr.simple_i(3)
    with pytest.raises(AttributeError):
        mr.simple_i(False)
    with pytest.raises(AttributeError):
        mr.simple_i(6.9)