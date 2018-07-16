import tensorflow as tf
from data import Data

if tf.__version__ < '1.8.0':
  raise ImportError('Please upgrade your tensorflow installation to v1.8.* or later!')

dir = 'dataset'
data = Data(dir)
