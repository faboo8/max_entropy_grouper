# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 15:35:12 2018

@author: DE104752
"""#

import pandas as pd
import numpy as np
import random

def entropy(n,N):
    return float(n)/N*np.log(float(n)/N)


def swap_rows(df1, df2, i1, i2):
    b, c = df1.iloc[i1].copy(), df2.iloc[i2].copy()
    df1.iloc[i1], df2.iloc[i2] = c,b
    return df1, df2


def df_entropy_partial(a, df, feature):
    FEATURES = df.groupby(feature).count()['name']
    features_a = a.groupby(feature).count()['name']

    count = a.shape[0] 

    entr_feature = sum(entropy(features_a[feature], min(count,FEATURES[feature])) for feature in features_a.index)

    return entr_feature


def split(rng, n):
    k, m = divmod(len(rng), n)
    return (rng[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))