from mynilmtk.api import API
from mynilmtk.disaggregate import CO, DSC, AFHMM,AFHMM_SAC,FHMMExact,Mean,Hart85
from mynilmtk.losses import accuracy, f1score, precision, recall, mae, rmse

import warnings
warnings.filterwarnings("ignore")

path = '/data/redd.h5'

experiment2 = {
  'power': {'mains': ['apparent','active'],'appliance': ['apparent','active']},
  'sample_rate': 60,
  'appliances': ['fridge','air conditioner', 'microwave'],
  'methods': {"Mean":Mean({}),"FHMM_EXACT":FHMMExact({'num_of_states':2}), "CombinatorialOptimisation":CO({})},
  'train': {    
    'datasets': {
        'Dataport': {
            'path': 'data/dataport.hdf5',
            'buildings': {
                10: {
                    'start_time': '2015-04-04',
                    'end_time': '2015-04-06'
                    }
                }                
            }
        }
    },
  'test': {
    'datasets': {
        'Datport': {
            'path': 'data/dataport.hdf5',
            'buildings': {
                10: {
                    'start_time': '2015-04-25',
                    'end_time': '2015-04-26'
                    }
                }
            }
        },
        'metrics':['mae','rmse','f1score','accuracy','precision']
    }
}