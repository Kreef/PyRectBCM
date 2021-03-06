from pyrectbcm.rectangular_input_generator import ModelData
import py.test


def test_import():
    Input = ModelData("testkees")
    assert hasattr(Input, "Basin")
    assert hasattr(Input, "Inlets")
    assert hasattr(Input, "Ocean")
    assert hasattr(Input, "Pars")

    Input = ModelData("testlocation")
    assert hasattr(Input, "Basin")
    assert hasattr(Input, "Inlets")
    assert hasattr(Input, "Ocean")
    assert hasattr(Input, "Pars")

    with py.test.raises(NameError):
        assert ModelData("AaP")
