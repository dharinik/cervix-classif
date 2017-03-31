from json import load, dump
from os.path import join, dirname, isfile

DATA_DIR = join(dirname(dirname(__file__)), 'data')
TRAIN_DIR = join(DATA_DIR, 'train')
TEST_DIR = join(DATA_DIR, 'test')
SUBMISSIONS_DIR = join(dirname(dirname(__file__)), 'submissions')
MODELS_DIR = join(dirname(dirname(__file__)), 'models')

CLASSES = ['Type_1', 'Type_2', 'Type_3']
ORGANIZED_DATA_INFO_FILE = 'organized_data_info_.json'


def load_organized_data_info(imgs_dim):
    """Loads the train, val, test datasets info file.
    
    Returns dict
    -------
    {
        'dir_tr': absolute path of the training directory
        'num_tr': number of training images
        'dir_val': absolute path of the validation directory
        'num_val': number of validation images
        'dir_te': absolute path of the test directory
        'num_te': number of test images
        'num_classes': number of distinct classes
    }
    """
    if not isfile(organized_data_info_file(imgs_dim)):
        raise FileNotFoundError('run data_dirs_organizer.py organize first')
    with open(organized_data_info_file(imgs_dim), 'r') as f:
        return load(f)


def save_organized_data_info(info, imgs_dim):
    with open(organized_data_info_file(imgs_dim), 'w') as f:
        dump(info, f)


def organized_data_info_file(imgs_dim):
    split = ORGANIZED_DATA_INFO_FILE.split('.')
    split[0] += str(imgs_dim)
    return join(DATA_DIR, '.'.join(split))