from __future__ import division

import tensorflow as tf
import sys

class Data(object):
  def __init__(directory):
    '''directory: The file directory where the training images are located.'''
    self.dir = directory
    if not tf.gfile.Exists(self.dir):
      print('[!] The direcctory is non-existent.')
      sys.exit()
    if not tf.gfile.IsDirectory(self.dir):
      print('[!] The selected file is not a directory. Please refer to a directory.')
      sys.exit()
    self.setup()
    
  def setup(self):
    self.files = os.listdir(self.dir)
