
from torchvision.models import *
from .inception import inception_v2, Inception2

def set_path_to_models(path):
    import os
    os.environ['TORCH_MODEL_ZOO'] = path
