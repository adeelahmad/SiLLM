import mlx.core as mx
import mlx.nn as nn

from sillm.args import ModelArgs

class BaseModel(nn.Module):
    """
    Base class for LLM models.
    """
    def __init__(self, args: ModelArgs):
        super().__init__()
    
    def __call__(self,
                 inputs: mx.array,
                 cache = None
                 ):
        raise NotImplementedError("Class model.Model is used for inheritance only")
    
    def loss(self,
        inputs: mx.array,
        targets: mx.array,
        lengths: mx.array):
        raise NotImplementedError("Loss function is not implemented for this model")