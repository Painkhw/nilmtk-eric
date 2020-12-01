import warnings

# Silence ImportWarnings for the time being
with warnings.catch_warnings():
    warnings.simplefilter('ignore', category=ImportWarning)
    from nilmtk import *
    from nilmtk.version import version as __version__
    from nilmtk.timeframe import TimeFrame
    from nilmtk.elecmeter import ElecMeter
    from nilmtk.datastore import DataStore, HDFDataStore, CSVDataStore, Key
    from nilmtk.metergroup import MeterGroup
    from nilmtk.appliance import Appliance
    from nilmtk.building import Building
    from nilmtk.dataset import DataSet

global_meter_group = MeterGroup()