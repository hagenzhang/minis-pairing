import numpy as np
import math
import copy

'''
Provides the weight (w_i) of a given parameter (n) based on the number of 
occurances (n_t) within N total parameter occurances. 

This function uses an inverse document frequency formula:
w_i = log(N/n_t)
'''
def get_weight(n_t, N):
    if n_t == 0:
        return 0
    
    x = N / n_t
    base = 2 # this will be hard-coded for now, we can parameterize this if needed
    return math.log(x, base)

'''
Assigns the weight values to an individual's interest flag array.
This function will take in 2 arrays: the individual's interest flag, and the frequency array of each trait.

The interest flag array is an array of positive / zero values. Positive means the individual has this trait,
and zero means the individual does not. 
TODO: negative values means the individual has a negative association with this trait. 

The frequency array is the number of individuals total who have a given trait.
'''
def assign_weights(interest_flag, frequency_arr):
    total = 0
    return_flag = copy.deepcopy(interest_flag)
    
    for i in frequency_arr:
        total = total + i

    for j in range(len(return_flag)):
        if return_flag[j]:
            return_flag[j] = get_weight(frequency_arr[j], total)
    
    return return_flag


def main():
    # [a, b, c, d, e, f]
    # i need to change these weights using log base 2 instead of log base 10.
    
    h1 = [1, 1, 0, 0, 1, 0]
    h2 = [1, 0, 1, 1, 0, 0]

    # TODO: optimization testing: do i only count the minis?
    # maybe have separate frequency arrays for heads and minis
    m1 = [1, 1, 1, 0, 0, 0]
    m2 = [1, 0, 1, 1, 0, 0]
    m3 = [1, 0, 0, 1, 1, 1]
    m4 = [0, 1, 1, 0, 0, 0]

    frequency_array = [3, 2, 3, 2, 1, 1]

    h1 = assign_weights(h1, frequency_array)
    print("h1 array: " + str(h1), flush=True)
    h2 = assign_weights(h2, frequency_array)
    print("h2 array: " + str(h2), flush=True)
    m1 = assign_weights(m1, frequency_array)
    print("m1 array: " + str(m1), flush=True)
    m2 = assign_weights(m2, frequency_array)
    print("m2 array: " + str(m2), flush=True)
    m3 = assign_weights(m3, frequency_array)
    print("m3 array: " + str(m3), flush=True)
    m4 = assign_weights(m4, frequency_array)
    print("m4 array: " + str(m4), flush=True)

    h1_mag = np.linalg.norm(h1)
    print("h1 mag: " + str(h1_mag))
    h2_mag = np.linalg.norm(h2)
    print("h2 mag: " + str(h2_mag))
    m1_mag = np.linalg.norm(m1)
    print("m1 mag: " + str(m1_mag))
    m2_mag = np.linalg.norm(m2)
    print("m2 mag: " + str(m2_mag))
    m3_mag = np.linalg.norm(m3)
    print("m3 mag: " + str(m3_mag))
    m4_mag = np.linalg.norm(m4)
    print("m4 mag: " + str(m4_mag))


    h1_m1_dot = np.dot(h1, m1)
    sim = np.arccos(h1_m1_dot / (h1_mag * m1_mag))
    print("h1_m1 similarity: " + str(sim), flush=True)

    h1_m2_dot = np.dot(h1, m2)
    sim = np.arccos(h1_m2_dot / (h1_mag * m2_mag))
    print("h1_m2 similarity: " + str(sim), flush=True)

    h1_m3_dot = np.dot(h1, m3)
    sim = np.arccos(h1_m3_dot / (h1_mag * m3_mag))
    print("h1_m3 similarity: " + str(sim), flush=True)

    h1_m4_dot = np.dot(h1, m4)
    sim = np.arccos(h1_m4_dot / (h1_mag * m4_mag))
    print("h1_m4 similarity: " + str(sim), flush=True)


    h2_m1_dot = np.dot(h2, m1)
    sim = np.arccos(h2_m1_dot / (h2_mag * m1_mag))
    print("h2_m1 similarity: " + str(sim), flush=True)

    h2_m2_dot = np.dot(h2, m2)
    sim = np.arccos(h2_m2_dot / (h2_mag * m2_mag))
    print("h2_m2 similarity: " + str(sim), flush=True)

    h2_m3_dot = np.dot(h2, m3)
    sim = np.arccos(h2_m3_dot / (h2_mag * m3_mag))
    print("h2_m3 similarity: " + str(sim), flush=True)

    h2_m4_dot = np.dot(h2, m4)
    sim = np.arccos(h2_m4_dot / (h2_mag * m4_mag))
    print("h2_m4 similarity: " + str(sim), flush=True)


if __name__ == "__main__":
    main()