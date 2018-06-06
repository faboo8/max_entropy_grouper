# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 09:40:27 2018

@author: DE104752
"""

import pandas as pd
import numpy as np
import random

df = pd.read_excel(sheet_name=1, skiprows=range(8), io = 'Digital Day 2018 - Teilnehmer_FH.xlsx',
                   header=None, names= ['role', 'name', 'branch', 'gender'], usecols=[0,1,2,4])



def entr(n,N):
    return float(n)/N*np.log(float(n)/N)





def df_entr(a, df):
    BRANCHES = df.groupby('branch').count()['name']
    ROLES = df.groupby('role').count()['name']
    GENDERS =  df.groupby('gender').count()['name']
    branches_a = a.groupby('branch').count()['name']
    roles_a = a.groupby('role').count()['name']
    genders_a =  a.groupby('gender').count()['name']
    
    count = a.shape[0] 
    
    entr_branch = sum(entr(branches_a[branch], min(count,BRANCHES[branch])) for branch in branches_a.index)       
    entr_role = sum(entr(roles_a[role], min(count,ROLES[role])) for role in roles_a.index)
    entr_gender = sum(entr(genders_a[g], min(count, GENDERS[g])) for g in genders_a.index)
    return entr_role + entr_branch + entr_gender


def df_entr_partial(a, df, feature):
    FEATURES = df.groupby(feature).count()['name']
    features_a = a.groupby(feature).count()['name']

    count = a.shape[0] 

    entr_feature = sum(entr(features_a[feature], min(count,FEATURES[feature])) for feature in features_a.index)

    return entr_feature


def propose_switch(dfs, df):
    choice1 = random.choice(range(dfs[0].shape[0]))
    choice2 = random.choice(range(dfs[1].shape[0]))
    print(choice1,choice2)
    temp_df1 =  dfs[0].copy()
    temp_df2 = dfs[1].copy()
    
    b, c = temp_df1.iloc[choice1].copy(), temp_df2.iloc[choice2].copy()
    temp_df1.iloc[choice1], temp_df2.iloc[choice2] = c,b
    
    entr_o = df_entr(dfs[0], df) + df_entr(dfs[1], df)
    entr_n = df_entr(temp_df1, df) + df_entr(temp_df2, df)
    if entr_n < entr_o or random.choice(range(999))==42:
        return temp_df1, temp_df2, entr_n
    else:
        return dfs[0], dfs[1], entr_o
    
    

##optimize groups:
df = df.sample(frac=1, random_state = 42).reset_index(drop=True)
df_groups = [df.iloc[0:15,:], df.iloc[15:30,:], df.iloc[30:46,:], df.iloc[46:62,:]]
entropy_start = sum(df_entr(a, df) for a in df_groups)
print(entropy_start)
    
df_groups = [df.iloc[0:15,:], df.iloc[15:30,:], df.iloc[30:46,:], df.iloc[46:62,:]]
for i in range(40000):
    sample = random.sample(range(4), 2)
    print(sample)
    df_groups[sample[0]], df_groups[sample[1]], entropy = propose_switch(dfs = [df_groups[sample[0]], df_groups[sample[1]]], df=df )
    
    entropy_full = sum(df_entr(a, df) for a in df_groups)
    print(entropy_full)