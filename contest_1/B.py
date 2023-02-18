import numpy as np
import typing as tp


def find_nearest_points(A: np.ndarray, B: np.ndarray, k: int) -> np.ndarray:    
    dist = np.sqrt(((B[:, np.newaxis, :] - A[np.newaxis, :, :]) * (B[:, np.newaxis, :] - A[np.newaxis, :, :])).sum(axis=2))
    dist = np.argsort(dist, axis=1)
    one = [1]
    return dist[:, :k] + one
