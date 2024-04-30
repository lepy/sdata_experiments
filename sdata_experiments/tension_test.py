# -*-coding: utf-8-*-
from sdata.experiments import Test, TestSeries
import numpy as np


class TensionTest(Test):
    """Tension test

    """

    ATTRIBUTES = [
        ['actual_pre_deformation', np.nan, 'float', '-', 'Die tatsächliche Vorverformung vor dem Zugversuch.', '',
         False],
        ['actual_strain_rate', np.nan, 'float', '-', 'Die tatsächliche Dehnungsrate während des Versuchs.', '', False],
        ['actual_testing_speed', np.nan, 'float', '-', 'Die tatsächliche Geschwindigkeit des Tests.', '', False],
        ['actual_testing_temperature', np.nan, 'float', '-', 'Die tatsächliche Temperatur während des Tests.', '',
         False],
        ['actual_specimen_cross_section', np.nan, 'float', 'mm', 'Der Anfangsquerschnitt der Probe.', 'S_0', True],
        ['test_date', '', 'str', '-', 'Das Datum, an dem der Test durchgeführt wurde.', '', False],
        ['direction_of_pre_deformation', '', 'str', '-',
         'Die Richtung der Vorverformung bezüglich der Probenorientierung.', '', False],
        ['specimen_treatment', '', 'str', '-', 'Informationen über eventuelle Wärmebehandlungen des Materials.', '',
         False],
        ['actual_gauge_length', np.nan, 'float', '-', 'Die Anfangsmesslänge der Probe.', 'L_0', True],
        # ['material_name', '', 'str', '-', 'Der Name des Materials.', '', False],
        # ['material_norm_name', '', 'str', '-', 'Der normative Name des Materials.', '', False],
        # ['material_number_norm', '', 'str', '-', 'Die normative Nummer des Materials.', '', False],
        # ['nominal_pre_deformation', np.nan, 'float', '-', 'Die nominale Vorverformung.', '', False],
        # ['nominal_strain_rate', np.nan, 'float', '-', 'Die nominale Dehnungsrate.', '', False],
        # ['nominal_testing_speed', np.nan, 'float', '-', 'Die nominale Testgeschwindigkeit.', '', False],
        ['test_location', '', 'str', '-', 'Der Ort, an dem der Test durchgeführt wurde.', '', False],
        ['test_direction', np.nan, 'float', '-', 'Die Prüfrichtung der Probe.', '', False],
        ['specimen_geometry', '', 'str', '-', 'Die Geometrie der Probe.', '', False],
        ['actual_specimen_thickness', np.nan, 'float', 'mm', 'Die Dicke der Probe.', '', False],
        ['actual_specimen_diameter', np.nan, 'float', 'mm', 'Die Durchmesser der Probe.', '', False],
        ['actual_specimen_length', np.nan, 'float', 'mm', 'Die Gesamtlänge der Probe.', '', False],
        ['actual_specimen_width', np.nan, 'float', 'mm', 'Die Breite der Probe.', '', False],
        ['actual_specimen_temperature', np.nan, 'float', '°C', 'Die Ausgangstemperatur der Probe.', '', False],
        ['actual_specimen_humidity', np.nan, 'float', '%', 'Die Feuchte der Probe.', '', False],
        ]

    def __init__(self, name, **kwargs):
        Test.__init__(self, name=name, **kwargs)
        for attrlist in self.ATTRIBUTES:
            self.metadata.set_attr(attrlist[0], attrlist[1],
                                   dtype=attrlist[2],
                                   unit=attrlist[3],
                                   description=attrlist[4],
                                   label=attrlist[5],
                                   required=attrlist[6])

class TensionTestSeries(TestSeries):
    """Tension test

    """

    ATTRIBUTES = [
        ['nominal_pre_deformation_direction', '', 'str', '-',
         'Die Richtung der Vorverformung bezüglich der Probenorientierung.', '', False],
        ['nominal_specimen_cross_section', np.nan, 'float', 'mm', 'Der Anfangsquerschnitt der Probe.', 'S_0', True],
        ['nominal_gauge_length', np.nan, 'float', '-', 'Die Anfangsmesslänge der Probe.', 'L_0', True],
        ['nominal_pre_deformation', np.nan, 'float', '-', 'Die nominale Vorverformung.', '', False],
        ['nominal_strain_rate', np.nan, 'float', '-', 'Die nominale Dehnungsrate.', '', False],
        ['nominal_testing_speed', np.nan, 'float', '-', 'Die nominale Testgeschwindigkeit.', '', False],
        ['nominal_specimen_thickness', np.nan, 'float', 'mm', 'Die Dicke der Probe.', '', False],
        ['nominal_specimen_diameter', np.nan, 'float', 'mm', 'Die Durchmesser der Probe.', '', False],
        ['nominal_specimen_length', np.nan, 'float', 'mm', 'Die Gesamtlänge der Probe.', '', False],
        ['nominal_specimen_width', np.nan, 'float', 'mm', 'Die Breite der Probe.', '', False],
        ['nominal_specimen_temperature', np.nan, 'float', 'mm', 'Die Ausgangstemperatur der Probe.', '', False],
        ['nominal_specimen_huminity', np.nan, 'float', 'mm', 'Die Feuchte der Probe.', '', False],
        ['material_name', '', 'str', '-', 'Der Name des Materials.', '', False],
        ['material_norm_name', '', 'str', '-', 'Der normative Name des Materials.', '', False],
        ['material_number_norm', '', 'str', '-', 'Die normative Nummer des Materials.', '', False],
        ['specimen_geometry', '', 'str', '-', 'Die Geometrie der Probe.', '', False],
        ['specimen_treatment', '', 'str', '-', 'Informationen über eventuelle Wärmebehandlungen des Materials.', '',
         False],
        ['tester', '', 'str', '-', 'Der Tester oder die Person, die den Test durchführt.', '', False],
        ['test_date', '', 'str', '-', 'Das Datum, an dem der Test durchgeführt wurde.', '', False],
        ['test_location', '', 'str', '-', 'Der Ort, an dem der Test durchgeführt wurde.', '', False],
        ['test_direction', np.nan, 'float', '-', 'Die Prüfrichtung der Probe.', '', False],
        ['test_temperature', '', 'float', '°C', 'Raumtemperatur, bei der Test durchgeführt wurde.', '', False],
        ['test_humidity', '', 'float', '%', 'Luftfeuchte im Raum, bei der Test durchgeführt wurde.', '', False],
        ]

    def __init__(self, name, **kwargs):
        TestSeries.__init__(self, name=name, **kwargs)
        for attrlist in self.ATTRIBUTES:
            self.metadata.set_attr(attrlist[0], attrlist[1],
                                   dtype=attrlist[2],
                                   unit=attrlist[3],
                                   description=attrlist[4],
                                   label=attrlist[5],
                                   required=attrlist[6])