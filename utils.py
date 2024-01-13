'''
A page of utility functions for the Minis Matcher program.
'''

import math
import pandas as pd
import numpy as np

#################################
### interest_matcher.py utils ###
#################################
'''
Provides the weight of a given parameter based on the number of 
occurances within N total parameter occurances. 

This function uses an inverse document frequency formula:
w_n = log(N/n_t)
and will return the weight of the given parameter

Input is the number of occurances for a given parameter (n_t), and
the total number of parameter occurances (N)
Output is the weight of the given parameter (w_n)
'''
def get_weight(n_t, N):
    if n_t == 0:
        return 0
    
    x = N / n_t
    base = 2 # this will be hard-coded for now, we can parameterize this if needed
    return math.log(x, base)

'''
Creates a frequency array based on a given dataframe that contains an interest_string column

For instance, if the total number of individuals that have trait 0 = 3, then the
0th index of the frequency array would be 3.

Input is a dataframe that contains a interest string column.
Output is an array of integers representing how often the corresponding trait appears,
and the total number of all interest instances.
'''
def create_frequency_array(df):
    interest_arrays = df['interest_string'].values
    print("Interest Arrays: " + str(df['interest_string'].values))

    frequency_array = [0] * len(interest_arrays[0])
    total = 0
    
    for i in range(len(interest_arrays)):
        for j in range(len(frequency_array)):
            if str(interest_arrays[i])[j] == '1':
                frequency_array[j] = frequency_array[j] + 1
                total = total + 1

    return frequency_array, total

'''
Provides the weight values to an individual's interest flag array based on a provided interest string.
This function will take in 2 inputs: the individual's interest binary string, and the frequency array of each trait.

The interest string is an array of single-digit numbers. 
1 = the individual has the corresponding trait
0 = the individual does not have the corresponding trait
TODO: 2 = the individual has a negative association with this trait. 

The frequency array is the number of individuals total who have a given trait.
This function will return an array of weights, with each weight being associated with the interest in that position

Input is...
Output is...
'''
def assign_weights(interest_flags, weight_arr):
    return_flag = [0] * len(interest_flags)

    for j in range(len(return_flag)):
        if interest_flags[j] == "1":
            return_flag[j] = weight_arr[j]
    
    return return_flag

#####################################
### interest_matcher.py utils end ###
#####################################