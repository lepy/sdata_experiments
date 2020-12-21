# -*-coding: utf-8-*-
__version__ = '0.1.1'
__revision__ = None
__version_info__ = tuple([int(num) for num in __version__.split('.')])

'''
sdata experiments 
'''

import sys
import logging
logger = logging.getLogger("sdata_experiments")
import inspect

from sdata.experiments import TestProgram, TestSeries, Test
from sdata_experiments.tension_test import TensionTest

SDATACLS = {"TestProgram": TestProgram,
            "TestSeries": TestSeries,
            "Test": Test,
            "TensionTest": TensionTest,
            }


def print_classes():
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            print(obj)