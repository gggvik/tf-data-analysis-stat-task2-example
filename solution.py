import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 250483508 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = x.shape[0]
    left = np.quantile(x, (1 - p) / 2)
    right = np.quantile(x, 1 - (1 - p) / 2)
    return (left, right)

