# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 16:14:15 2018

@author: DE104752
"""

import utilities
import random

class EntropyGrouping:
    
    def __init__(self, df, name_column, feature_columns, N, n=10000, random_swap=False, shuffle = True):
        self.df = df
        self.name_column = name_column
        assert type(feature_columns)==list
        self.feature_columns = feature_columns
        self.N = N
        self.n = n
        self.random_swap = random_swap
        
        if shuffle == True:
            self.df = self.df.sample(frac=1, random_state = 42).reset_index(drop=True)
            
            
        def split(self):          
            df_groups =[df.loc[rng] for rng in list(utilities.split(range(self.df.shape[0]), self.N))]
            return df_groups
            
        def propose_swap(self, dfs):
            choice1 = random.choice(range(dfs[0].shape[0]))
            choice2 = random.choice(range(dfs[1].shape[0]))
            #print(choice1,choice2)
            temp_df1 =  dfs[0].copy()
            temp_df2 = dfs[1].copy()
            
            b, c = temp_df1.iloc[choice1].copy(), temp_df2.iloc[choice2].copy()
            temp_df1.iloc[choice1], temp_df2.iloc[choice2] = c,b
            
            entr_o = sum(utilities.df_entropy_partial(dfs[0], self.df, feature) + 
                         utilities.df_entropy_partial(dfs[0], self.df, feature) 
                         for feature in self.feature_columns)
            entr_n = sum(utilities.df_entropy_partial(temp_df1, self.df, feature) + 
                         utilities.df_entropy_partial(temp_df2, self.df, feature) 
                         for feature in self.feature_columns)
            if entr_n < entr_o or (self.random_swap ==True and random.choice(range(999))==42):
                return temp_df1, temp_df2, entr_n
            else:
                return dfs[0], dfs[1], entr_o
            
        def find_best_groups(self, n=10000):
            
            for i in range(n):
                sample = random.sample(range(self.N), 2)
                df_groups = self.split()
                df_groups[sample[0]], df_groups[sample[1]], entropy = self.propose_swap(
                                                                                        dfs = [df_groups[sample[0]], 
                                                                                               df_groups[sample[1]]], df=df 
                                                                                               )
                
                entropy_full = sum(utilities.df_entropy_partial(a, df, feat) for a, feat in zip(df_groups, self.feature_columns))
                print(entropy_full)
            return df_groups
        
        
            
            
            
            
        