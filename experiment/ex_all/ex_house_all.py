
from api import API
from disaggregate import ADAE, DAE, Seq2Point, Seq2Seq, WindowGRU, RNN
import warnings
warnings.filterwarnings("ignore")

path = '/home/eric/Project/NILMproj/Exam/redd_low_freq.h5'

debug = False
test = False

if(debug):
    method = {
        'DAE': DAE({'save-model-path': 'DAE', 'pretrained-model-path': None, 'n_epochs': 1, 'batch_size': 256}),
        'RNN': RNN({'save-model-path': 'RNN', 'pretrained-model-path': None, 'n_epochs': 1, 'batch_size': 256}),
        'Seq2Point': Seq2Point({'save-model-path': 'Seq2Point', 'pretrained-model-path': None, 'n_epochs': 1, 'batch_size': 256}),
        'Seq2Seq': Seq2Seq({'save-model-path': 'Seq2Seq', 'pretrained-model-path': None, 'n_epochs': 1, 'batch_size': 256}),
        'GRU': WindowGRU({'save-model-path': 'GRU', 'pretrained-model-path': None, 'n_epochs': 1, 'batch_size': 256}),
    }
else:
    method = {
        'DAE': DAE({'save-model-path': 'DAE', 'pretrained-model-path': None}),
        'RNN': RNN({'save-model-path': 'RNN', 'pretrained-model-path': None}),
        'Seq2Point': Seq2Point({'save-model-path': 'Seq2Point', 'pretrained-model-path': None}),
        'Seq2Seq': Seq2Seq({'save-model-path': 'Seq2Seq', 'pretrained-model-path': None}),
        'GRU': WindowGRU({'save-model-path': 'GRU', 'pretrained-model-path': None}),
    }
if test:
    method = {
        'DAE': DAE({'save-model-path': 'DAE', 'pretrained-model-path': 'DAE'}),
        'RNN': RNN({'save-model-path': 'RNN', 'pretrained-model-path': 'RNN'}),
        'Seq2Point': Seq2Point({'save-model-path': 'Seq2Point', 'pretrained-model-path': 'Seq2Point'}),
        'Seq2Seq': Seq2Seq({'save-model-path': 'Seq2Seq', 'pretrained-model-path': 'Seq2Seq'}),
        'GRU': WindowGRU({'save-model-path': 'GRU', 'pretrained-model-path': 'GRU'}),
    }


ex_train_fridge = {

    'power': {
        'mains': ['apparent', 'active'],
        'appliance': ['apparent', 'active']
    },
    'sample_rate': 6,


    'appliances': ['fridge','light', 'microwave',],
    'methods': method,
    'isState': False,
    'train': {
        'datasets': {

            'redd': {
                'path': path,
                'buildings': {
                    1: {
                        'start_time': '2011-04-18',
                        'end_time': '2011-05-24'
                    },
                    3: {
                        'start_time': '2011-04-16',
                        'end_time': '2011-05-30'
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
                        'end_time': '2011-05-22'
                    },
                    6: {
                        'start_time': '2011-05-21',
                        'end_time': '2011-06-14'
                    }
                }
            }
        },
    },
}

#%%

API(ex_train_all)
