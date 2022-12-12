import numpy as np
import torch.nn as nn
import torch

import cv2

class torch_IO(object):
  def __init__(self):
    pass
  def t2n(self, tensor):
    if isinstance(tensor, torch.Tensor):
      tensor = tensor.detach().cpu().numpy()
    return tensor
  def __convert_input__(self, x):
    if not isinstance(x, torch.Tensor):
      x = torch.tensor(x)
    assert len(x.shape) in [3,4]
    if len(x.shape) == 3:
      x =  x.unsqueeze(0)
    return x
  def get_input(self, x):
    x = self.__convert_input__(x)
    return x
  def get_output(self):
    pass
  

    
