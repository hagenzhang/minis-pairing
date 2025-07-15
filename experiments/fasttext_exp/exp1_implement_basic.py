"""
Run from test directory for access to the pre-loaded models.

Test 1: Implementing FastText

Goals:
- Import the FastText data into a project.
- Compare a series of words and find out the differences in their matrix representations using
  various metrics

Findings:
- Phrases like "milk tea" or "milk_tea" don't fare well, but "milk_tea" does a little bit better
- Training our own data might be necessary, but the similarity scores seem to suffice for now
- Sim scores are symmetric, which makes sense and can save us some storage
"""
import fasttext
import fasttext.util
import numpy as np

# https://fasttext.cc/docs/en/support.html#building-fasttext-python-module
# pre-trained word vectors, trained on CommonCrawl and Wikipedia
# downloading the model will take a bit to run
fasttext.util.download_model('en', if_exists='ignore')  # English
ft = fasttext.load_model('cc.en.300.bin')

print('fasttext model cc.en.300.bin loaded')
print('model dimesnions:', ft.get_dimension())

# we test various words and phrases to see the vector representations and how much they differ visually
# test_words = ['boba', 'milk_tea', 'milk tea', 'coffee', 'beverages', 'computer', 'chair']
test_words = ['boba', 'tea', 'coffee', 'beverages', 'computer', 'chair']

for word in test_words:
    print('\nTest Word For Nearest Neighbors Analysis:', word)
    # word_vec = ft.get_word_vector(word) # this is how we get the word vector for similarity comparison later on
    print('  5 Nearest Neighbors:', ft.get_nearest_neighbors(word, k=5))


# based on this test, we can tell that inputs like "milk_tea" or "milk tea" don't fare well, since they
# output gibberish as the nearest neighbors. however, maybe their vector similarity scores will be
# somewhat similar?
cos_sim_results_file = './exp1_cosine_similarity_analysis.txt'
eucl_dist_results_file = './exp1_euclidean_distance_analysis.txt'
l1_dist_results_file = './exp1_manhattan_distance_analysis.txt'
dot_prod_results_file = './exp1_dot_product_similarity_analysis.txt'

def cos_sim(vec1, vec2):
    '''Helper function for calculating cosine similarity between 2 vectors'''
    # range is [-1, 1]
    magnitude1 = np.linalg.norm(vec1)
    magnitude2 = np.linalg.norm(vec2)
    return np.dot(vec1, vec2) / (magnitude1 * magnitude2)

def eucl_dist(vec1, vec2):
    '''Helper function for calculating the euclidean distance between 2 vectors'''
    # range is [0, +inf]
    dist = np.linalg.norm(vec1 - vec2) # default ord value = 2, ord value of 1 is manhattan distance
    return dist

def manhattan_dist(vec1, vec2):
    '''Helper function for calculating the manhattan distance between 2 vectors'''
    # range is [0, +inf]
    dist = np.linalg.norm(vec1 - vec2, ord=1)
    return dist

def dot_prod_dist(vec1, vec2):
    '''Helper function for calculating the dot product between 2 vectors'''
    # range is [-inf, +inf]
    diff = np.dot(vec1, vec2)
    return diff

# to test:
# Cosine Similarity -> Only considers angles, vector magnitude doesn't matter
# Euclidean Distance -> Preserves true geometric distance, but doesn't scale well
# Manhattan (L1) Distance -> Robust against outliers
# Dot Product -> Captures direction and magnitude

with open(cos_sim_results_file, 'w') as f:
    for word in test_words:
        print('\nTest Word For Cosine Similarity Comparison:', word, file=f)

        for i in test_words:
            word_vec = ft.get_word_vector(word)
            comp_vec = ft.get_word_vector(i)
            sim = cos_sim(word_vec, comp_vec)
            print("  Similarity", word, "vs", i, '=', sim, file=f)

with open(eucl_dist_results_file, 'w') as f:
    for word in test_words:
        print('\nTest Word For Euclidean Distance Comparison:', word, file=f)

        for i in test_words:
            word_vec = ft.get_word_vector(word)
            comp_vec = ft.get_word_vector(i)
            sim = eucl_dist(word_vec, comp_vec)
            print("  Similarity", word, "vs", i, '=', sim, file=f)

with open(l1_dist_results_file, 'w') as f:
    for word in test_words:
        print('\nTest Word For L1 Distance Comparison:', word, file=f)

        for i in test_words:
            word_vec = ft.get_word_vector(word)
            comp_vec = ft.get_word_vector(i)
            sim = manhattan_dist(word_vec, comp_vec)
            print("  Similarity", word, "vs", i, '=', sim, file=f)

with open(dot_prod_results_file, 'w') as f:
    for word in test_words:
        print('\nTest Word For Dot Product Comparison:', word, file=f)

        for i in test_words:
            word_vec = ft.get_word_vector(word)
            comp_vec = ft.get_word_vector(i)
            sim = dot_prod_dist(word_vec, comp_vec)
            print("  Similarity", word, "vs", i, '=', sim, file=f)


"""
Result:

I'll probably go forward with cosine similarity. We can re-visit this if we ever make a new model using the ASU minis data, but for now
the other metrics are not accurate in the way I would like.
"""