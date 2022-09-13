from statsmodels.graphics.functional import fboxplot as fbplot
import numpy as np
from matplotlib import pyplot as plt

def central_region_area(data):
    '''
        Input:
            data: numpy with dim: T * R
        Output:
            central region area: scalar
    '''
    T, R = data.shape
    _ = fbplot(data.T)
    plt.close()
    
    ix = _[2]
    centralRegion = data[:,ix[0:int(R//2)]]
    return np.sum(centralRegion.max(axis = 1) - centralRegion.min(axis = 1))

def get_I_UQ(hatY, Y):
    '''
        Input:
            hatY: emulated realizations, numpy with dim: T * R
            Y: data, numpy with dim: T * R
        Output:
            Ifit: scalar
    '''
    T, R = Y.shape
    assert (T, R) == hatY.shape, 'Dimensions of realizations and data do not match!'

    num = central_region_area(hatY)
    den = central_region_area(Y)
    
    return num/den

def get_I_fit(hatYMean, Y):
    '''
        Input:
            hatYMean: emulated mean, numpy with dim: T
            Y: data, numpy with dim: T * R
        Output:
            Ifit: scalar
    '''
    T = Y.shape[0]
    assert T == hatYMean.size, 'Dimensions of realizations and data do not match!'

    num = np.mean((Y.T - hatYMean) ** 2)
    
    YMean = Y.mean(axis = 1)    
    den = np.mean((Y.T - YMean) ** 2)
    
    return num/den