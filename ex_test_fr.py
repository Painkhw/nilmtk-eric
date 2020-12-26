from mynilmtk.api import API

from mynilmtk.disaggregate import DAE, Seq2Point, Seq2Seq, WindowGRU, RNN
from mynilmtk.disaggregate import CO, DSC, AFHMM,AFHMM_SAC,FHMMExact,Mean,Hart85
from mynilmtk.losses import accuracy, f1score, precision, recall, mae, rmse
import warnings
warnings.filterwarnings("ignore")

path = '/home/eric/Project/data/ukdale.h5'

test = {
    'power': {
        'mains': ['apparent','active'],
        'appliance': ['apparent','active']
    },
    'sample_rate': 60,
    'appliances': ['fridge'],
    'methods': {
        'WindowGRU':WindowGRU({'n_epochs':50,'batch_size':256}),
        'RNN':RNN({'n_epochs':50,'batch_size':256}),
        'DAE':DAE({'n_epochs':50,'batch_size':256}),
        'Seq2Point':Seq2Point({'n_epochs':50,'batch_size':256}),
        'Seq2Seq':Seq2Seq({'n_epochs':50,'batch_size':256}),
        'Mean': Mean({}),
    },
    'train': {    
        'datasets': {
                'ukdale': {
                    'path': '/home/eric/Project/data/ukdale.h5',
                    'buildings': {
                        1: {
                            'start_time': '2012-12-20',
                            'end_time': '2017-04-20'
                        },
                        2: {
                            'start_time': '2013-05-23',
                            'end_time': '2013-09-23'
                        },
                    }                    
                }
            }
        },
        'test': {
        'datasets': {
            'ukdale': {
                'path': '/home/eric/Project/data/ukdale.h5',
                'buildings': {
                    5: {
                        'start_time': '2014-07-01',
                        'end_time': '2014-11-01'
                    },
                }
            }
        },
        'metrics':['mae','rmse','f1score','accuracy','precision']
    }
}

api_res = API(test)
