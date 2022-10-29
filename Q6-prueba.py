# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 21:37:00 2020

@author: USUARIO
"""

state_df = pd.DataFrame()
state_df['State'] = $unique_state_names_list$

#intialise all state populations to 0
state_df['Top3PoP'] = 0
state_df.set_index('State',inplace=True)
for st in state_df.index:
    countiespop = $find_pop_of_st_cnties_sorted_descending(st)$
    #check if countiespop has more than one number
    #this check is needed because for states with one
    #county only, countiespop is a number
    if type(countiespop) == pd.Series:
      stsum = sum(countiespop$.getfirst3$)
    else:
      stsum = countiespop
    state_df['Top3PoP'].loc[st] = stsum

state_df$.sortDescAccordingToTop3PoP$
state_df$.getfirst3States$