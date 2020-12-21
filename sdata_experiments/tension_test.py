# -*-coding: utf-8-*-
from sdata.experiments import Test

class TensionTest(Test):
    """Tension test

    """
    def __init__(self, name, **kwargs):
        Test.__init__(self, name=name, **kwargs)