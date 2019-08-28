import numpy as np
import pandas as pd

def get_nan_ds(ds):
    k = np.sum(ds.isnull())
    z = pd.DataFrame()
    z['column'] = k.index
    z['c_nan'] = k.values
    z['ratio'] = k.values/ds.shape[0]
    return z

