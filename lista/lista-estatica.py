import numpy as np
import sys

class Lista:
  def __init__(self, numero):
    self.max = numero
    self.elemento = np.zeros(self.max)