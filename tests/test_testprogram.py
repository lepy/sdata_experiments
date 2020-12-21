import sys
import os
import uuid
import six

modulepath = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(modulepath, "..", "..", "src"))

from sdata_experiments import TestProgram, TestSeries, Test
import pandas as pd
import numpy as np

def test_test():
    tpname = "ALU"
    tpuuid = "d4e97cedca6238bea16732ce88c1922f"
    tsname = "ALU_UT"
    tsuuid = "a1e97cedca6238bea16732ce88c19220"
    tname = "test A1-001"
    t = Test(name=tname)
    print(t)

    assert t.name == tname
    assert t.uuid_testseries == ""
    assert t.name_testseries == "N.N."

    t = Test(name=tname,
            uuid_testseries=tsuuid,
            name_testseries=tsname,
            uuid_testprogram=tpuuid,
            name_testprogram=tpname,
            )
    print(t)

    assert t.name == tname
    assert t.uuid_testseries == tsuuid
    assert t.name_testseries == tsname
    assert t.uuid_testprogram == tpuuid
    assert t.name_testprogram == tpname



def test_testseries():
    tpname = "ALU"
    tpuuid = "a00000edca6238bea16732ce88c1922f"
    tsname = "ALU_UT"
    tsuuid = "b111111dca6238bea16732ce88c19220"
    ts = TestSeries(name=tsname)
    print(ts)

    assert ts.name == tsname
    assert ts.uuid_testseries == ts.uuid
    assert ts.name_testseries == ts.name

    ts = TestSeries(name=tsname,
                    uuid_testseries=tsuuid,
                    name_testseries=tsname,
                    uuid_testprogram=tpuuid,
                    name_testprogram=tpname,
                    )
    print(ts)

    print(ts.metadata.df.value)

    assert ts.name == tsname
    assert ts.uuid_testseries == tsuuid
    assert ts.name_testseries == tsname
    assert ts.uuid_testprogram == tpuuid
    assert ts.name_testprogram == tpname


def test_testprogram():
    tpname = "ALU"
    tpuuid = "a0000000ca6238bea16732ce88c1922f"

    tp = TestProgram(name=tpname,
                     uuid=tpuuid,)
    print(tp.metadata.df.value)
    assert tp.uuid == tpuuid
    assert tp.uuid_testprogram == tpuuid
    assert tp.name == tpname
    assert tp.name_testprogram == tpname

    tp = TestProgram(name=tpname,
                     uuid=tpuuid,
                )
    print(tp.metadata.df.value)
    assert tp.uuid == tpuuid
    assert tp.name == tpname
    assert tp.uuid_testprogram == tpuuid
    assert tp.name_testprogram == tpname

    tsname = "Testseries S1"
    tsuuid = "b11111111a6238bea16732ce88c19221"
    ts = tp.gen_testseries(name=tsname, uuid=tsuuid)
    print(ts)
    assert ts.name == tsname
    assert ts.uuid_testprogram == tpuuid
    assert ts.name_testprogram == tpname

    tname = "Test S1-001"
    tuuid = "b4e97cedca6238bea16732ce88c19221"
    t = ts.gen_test(name=tname,
                          uuid=tuuid)
    print(ts)
    assert t.name == tname
    assert t.uuid_testprogram == tpuuid
    assert t.name_testprogram == tpname
    assert t.uuid_testseries == tsuuid
    assert t.name_testseries == tsname


def atest_testprogram():
    tp = gen_dummy_testprogram()
    print(tp)
    assert tp.name == "testprogram FOO"
    print(tp.dir())
    exportpath = "/tmp/mytestprogramx"
    tp.to_folder(exportpath, dtype="csv")
    tp.tree_folder(exportpath)
    tp2 = sdata.Data.from_folder(exportpath)
    print(tp)
    print(tp2)
    print(tp2.metadata.to_dataframe())
    exportpath2 = "/tmp/mytestprogramx2"
    tp2.to_folder(exportpath2)
    tp2.tree_folder(exportpath2)
    print()


if __name__ == '__main__':
    # test_test()
    # test_testseries()
    test_testprogram()
    sdata.print_classes()
