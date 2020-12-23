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

            'redd': {
                'path': path,
                'buildings': {
                    1: {
                        'start_time': '2011-04-18',
                        'end_time': '2011-05-24'
                    }
                }
            }
        }
    },

    'test': {
        'datasets': {
            'redd': {
                'path': path,
                'buildings': {
                    2: {
                        'start_time': '2011-04-17',
                        'end_time': '2011-04-22'
                    },
                }
            }
        },
         'metrics':['mae','rmse','f1score','accuracy','precision']
    },
}

API(experiment2)