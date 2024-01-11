import numpy as np
import pandas as pd
import math

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


'''
Assigns minis to heads.

This function has the following dependencies:
- minis-pairing/resources/minis_data.csv
- minis-pairing/resources/heads_data.csv
For information on how to format these files, refer to the README.

This function will create a new file: minis-pairing/outputs/pairings.csv
The pairings.csv file will outline which minis are recommended for which heads.
For more information on how to use the pairings.csv file, refer to the README.
'''
def main():
    dtype = {"id": int, "name": str, "interest_string": str}
    df_heads = pd.read_csv('./resources/heads_data.csv', header=0, dtype=dtype)
    df_minis = pd.read_csv('./resources/minis_data.csv', header=0, dtype=dtype)

    heads_freq_arr, heads_total = create_frequency_array(df_heads)
    minis_freq_arr, minis_total = create_frequency_array(df_minis)
    assert len(heads_freq_arr) == len(minis_freq_arr), "frequency arrays misaligned"
    
    print("Heads Frequency Array: " + str(heads_freq_arr))
    print("Minis Frequency Array: " + str(minis_freq_arr))

    heads_weight_arr = [0] * len(heads_freq_arr)
    for i in range(len(heads_freq_arr)):
        heads_weight_arr[i] = get_weight(heads_freq_arr[i], heads_total)
    print("Weight of the Heads traits: " + str(heads_weight_arr))

    minis_weight_arr = [0] * len(minis_freq_arr)
    for i in range(len(minis_freq_arr)):
        minis_weight_arr[i] = get_weight(minis_freq_arr[i], minis_total)
    print("Weight of the Minis traits: " + str(minis_weight_arr))


    # dictionary containing each head's interest string based on their id
    heads_interest_dict = {}
    for i in range(len(df_heads['name'])):
        heads_interest_dict[df_heads['id'].values[i]] = df_heads['interest_string'].values[i]
    
    # dictionary containing each mini's interest string based on their id
    minis_interest_dict = {}
    for i in range(len(df_minis['name'])):
        minis_interest_dict[df_minis['id'].values[i]] = df_minis['interest_string'].values[i]

    heads_weighted_dict = {}
    for id in heads_interest_dict:
        heads_weighted_dict[id] = assign_weights(heads_interest_dict[id], minis_weight_arr)

    minis_weighted_dict = {}
    for id in minis_interest_dict:
        minis_weighted_dict[id] = assign_weights(minis_interest_dict[id], minis_weight_arr)

    heads_magnitude_dict = {}
    for id in heads_interest_dict:
        heads_magnitude_dict[id] = np.linalg.norm(heads_weighted_dict[id])

    minis_magnitude_dict = {}
    for id in minis_interest_dict:
        minis_magnitude_dict[id] = np.linalg.norm(minis_weighted_dict[id])

    print("\n\nSimilarity Results")
    for h_index in range(len(df_heads['name'])):
        for m_index in range(len(df_minis['name'])):
            sim_score = np.arccos(
                (np.dot(heads_weighted_dict[h_index], minis_weighted_dict[m_index])) / 
                (heads_magnitude_dict[h_index] * minis_magnitude_dict[m_index]))

            print("head # " + str(h_index) +
                  " and mini # " + str(m_index) +
                  " have a similarity score of: " + str(sim_score))


if __name__ == "__main__":
    main()

    ###################################
    ### SCRIPT PSEUDOCODE / OUTLINE ###
    ###################################
    # to start off, we need a way to pipe in data. this will probably come from a csv file for ease of use.
    # we will need to enforce a file format, such as:

    # id | name | interest_string
    # the id is a unique identifier number for each person on a spreadsheet.
    # the name is the first_last name of the invidiual in question
    # the interest binary is a binary string that represents the interests an individual has.
    #   for example:
    #   say our matching only has to contend with 3 interests: boba, gaming, and hiking (order must be enforced)
    #   if an individual is interested in boba & hiking, their interest binary would be: 101
    #   if an individual is interested in gaming & hiking, their interest binary would be: 011
    #   if an individual is interested in gaming & boba, then they need to touch grass (110)
    #   0 ==> no interest, 1 ==> interest, TODO: -1 ==> negative interest

    # we can have 2 forms, one for all minis and one for all heads