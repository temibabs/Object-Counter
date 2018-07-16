from __future__ import division

import tensorflow as tf
import numpy as np
import sys
import os

from skimage.io import imread, imshow
from skimage.transform import resize
from random import shuffle

import main

class Data(object):
  def __init__(self, directory, train):
    '''
    directory: The file directory where the training images are located.
    train: (True or False) True for training purpose, False for validation purposes.'''
    
    self.dir = directory
    if not tf.gfile.Exists(self.dir):
      print('[!] The direcctory is non-existent.')
      sys.exit()
    if not tf.gfile.IsDirectory(self.dir):
      print('[!] The selected file is not a directory. Please refer to a directory.')
      sys.exit()
      
    if train == True:
      self.purpose = 'train'
    elif train == False:
      self.purpose = 'test'
    else:
      raise TypeError('[!] train can only be True or False.')
      
    if self._setup() == 0:
      self.ready = True
    
  def _setup(self):
    print('[+] Setting up your directory...')
    self.files = os.listdir(self.dir)
    
    allowed_extensions = ['png', 'jpeg', 'jpg']
    
    for i in self.files:
      if i.split('.')[1].lower() not in allowed_extensions:
        raise TypeError('[!] You have wrong file types in your directory')
        
    return 0
  
  def load_image(file):
    in_ = imread(self.dir + '/' + file)
    out_ = 
    
    return in_, out
  
  def load_batch(self, batch_size):
    X = np.zeros((batch_size, main.IMG_HEIGHT, main.IMG_WIDTH, 3) dtype=np.float32)
    Y = np.zeros((batch_size, main.OUT_HEIGHT, main.OUT_WIDTH, 5) dtype=np.float32)
    
    for i in range(0, batch_size):
      
      temp = self.files[0]
      X[i], Y[i] = self.load_image(temp)
      self.files.remove(temp)
    
    return X, Y
  
  def resize(X):
    return resize(X, [IMG_HEIGHT, IMG_WIDTH, 3], preserve_range=True)
  
  def reshape(X, Y):
    '''
    X: the image data to be reshaped.
    Y: What to reshape it into.'''
    return tf.reshape(X, Y)
