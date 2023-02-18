import numpy as np
import typing as tp

def find_max_sum_segment(array: tp.List[int], k: int) -> int:    
    first = np.zeros((len(array) + 1, len(array)))
    np_arr = np.array(array)
    first += np_arr
    return first.reshape(len(array), len(array) + 1)[:k, :len(array) - k + 1].sum(axis=0).max()
