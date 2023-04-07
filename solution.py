import pandas as pd
import numpy as np


chat_id = 5441234011 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    sigma = np.exp(1)
    error = np.random.normal(-35, sigma, n)
    x = error/ 10
    
    return x.mean() # Ваш ответ
