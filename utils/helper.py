import random
import numpy as np
import torch




def set_random_seed(seed):
    """Set random seeds wherever required"""
    random.seed(seed)
    np.random.seed(seed) # Sets the seed for NumPy's random number generator
    torch.manual_seed(seed)  # Sets the seed for PyTorch's CPU random number generator,
    torch.cuda.manual_seed(seed) # Sets the seed for PyTorch's GPU random number generator
    torch.cuda.manual_seed_all(seed) # Sets the seed for all GPUs (if multiple GPUs are used)