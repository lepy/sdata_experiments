
from sdata_experiments.tension_test import TensionTest

def test_tensiontest():

    tt = TensionTest(name="a tension test")
    print(tt)
    assert tt.name == "a tension test"