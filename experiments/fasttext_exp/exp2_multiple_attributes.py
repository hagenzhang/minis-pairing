"""
Run from test directory for access to the pre-loaded models.

Test 2: Utilizing Fasttext for matching multiple attributes

Goals:
- Find similarity scores between two individuals with multiple interests

Findings:
- Similarity between minis 1 and 2: 0.55202574
- Similarity between minis 2 and 3: 0.76513845
- Similarity between minis 1 and 3: 0.7158557

Findings are pretty expected I think, I did want 3 to be a mix of 1 and 2, and I wanted 1 and 2 to
be very different. 

I think the system of averaging the vectors works fine, and it should serve our purposes well enough!
"""
import fasttext
import fasttext.util
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

mini_one_interests = ['gaming', 'gym', 'running', 'hiking', 'music', 'guitar']
        
mini_two_interests = ['art', 'shopping', 'anime', 'indoors', 'cooking', 'plants']

mini_three_interests = ['gaming', 'shopping', 'running', 'indoors', 'music', 'plants']


# https://fasttext.cc/docs/en/support.html#building-fasttext-python-module
fasttext.util.download_model('en', if_exists='ignore')  # English
ft = fasttext.load_model('cc.en.300.bin')

def list_embeddings(word_list):
    '''
    Converts a list of strings into a single vector, which is the
    average of all of the word vectors
    '''
    vectors = [ft.get_word_vector(w) for w in word_list]
    return np.mean(vectors, axis=0)  # average

mini_one_vec = list_embeddings(mini_one_interests)
mini_two_vec = list_embeddings(mini_two_interests)
mini_three_vec = list_embeddings(mini_three_interests)

sim1_2 = cosine_similarity([mini_one_vec], [mini_two_vec])[0][0]
sim2_3 = cosine_similarity([mini_two_vec], [mini_three_vec])[0][0]
sim1_3 = cosine_similarity([mini_one_vec], [mini_three_vec])[0][0]

print("Similarity between minis 1 and 2:", sim1_2)
print("Similarity between minis 2 and 3:", sim2_3)
print("Similarity between minis 1 and 3:", sim1_3)

