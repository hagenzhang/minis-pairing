import numpy as np
import pandas as pd
from utils import *

'''
Assigns minis to heads.

TODO: implement likert-scale like system to introduce variations in how much someone likes something
suggested implementation:
add another column to the csv tables: interest_weight or smth like that.
then, multiply each value by the corresponding amount in the interest_weight
this should impact the vector either positively or negatively depending on the value,
to the point that we can get dislikes by using smaller values
- Maybe using negative values makes more sense?

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