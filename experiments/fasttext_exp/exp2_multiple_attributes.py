"""
Run from test directory for access to the pre-loaded models.

Test 2: Utilizing Fasttext for matching multiple attributes

Goals:
- Create a reliable representation of an individual
- Find similarity scores between two individuals with multiple interests
- Add weights to attributes to emphasize things like major, gender, year, etc


Findings:
"""

class Mini:
    '''
    Representation of a mini in the ASU Minis Program.

    Holds the year, gender, major, and interests of the individual.

    Attributes:
        year (int): # of years this mini has been in college
        gender (string): gender identity of this mini
        major (string): major of this mini
        interest (list): interests this mini has
    '''

    def __init___(self):
        self.year = 1
        self.gender = None
        self.major = None
        self.interests = []

    def __init__(self, year, gender, major, interests):
        self.year = year
        self.gender = gender
        self.major = major
        self.interests = interests


mini_one_year = 2
mini_one_gender = 'male'
mini_one_major = 'software'
mini_one_interests = 'gaming, anime, '
        
