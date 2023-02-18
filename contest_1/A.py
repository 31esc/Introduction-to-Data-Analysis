import numpy as np
import typing as tp

def matrix_multiplication(A: np.ndarray, B: np.ndarray) -> np.ndarray:    
    return (A[:, np.newaxis, :] * np.transpose(B)[np.newaxis, :, :]).sum(axis=2)
