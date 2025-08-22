"""
Create a basic ontology DAG, where we use each major as a node, and the edges between the nodes as a similarity score.
Then, to find the difference between 2 majors, we can traverse the graph and find the shortest path. Adding all of the
distances together gives us the total perceived difference between majors.

We'll start with 4 basic one: CS, MechE, Graphic Design, Consulting (Business)
"""
import ontology

# testing our data structure:
test_onto = ontology.WeightedOntology()

# "major" label as root node, BA and BS split up
test_onto.add_edge("Major", "BA", 0.3)
test_onto.add_edge("Major", "BS", 0.3)

# BA branches
test_onto.add_edge("BA", "Graphic Design", 0.6)
test_onto.add_edge("BA", "Music", 0.6)

# BS branches
test_onto.add_edge("BS", "CS", 0.6)
test_onto.add_edge("BS", "MechE", 0.6)

# Testing similarities
print("Design vs Music:", test_onto.similarity("Graphic Design", "Music")) # both in BA
print("Design vs MechE:", test_onto.similarity("Graphic Design", "MechE")) # split branch
print("Design vs Music:", test_onto.similarity("Graphic Design", "Music")) #
print("CS vs MechE:", test_onto.similarity("CS", "MechE")) # both in BS
print("Music vs MechE:", test_onto.similarity("Music", "MechE")) # split branch

