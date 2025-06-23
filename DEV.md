# minis pairing dev notes

After initially attemping some proof of concept work, I realized that I would need to use more pre-existing resources to make this program as accurate as possible.

## Approach

### Interest Matching
The approach is going to be using established word embeddings in order to determine how similar two people are. 

For the word embeddings, we'll start off by implementing it with FastText, and create some basic code snippets in order to test how it handles different interests.

Next up, we can try it on some sample data with real life fams and pairings, and see how compatible people were with each other versus how compatible our programs says they should be.

One thing that might be worth looking into is seeing how to "train" the embeddings? But this might turn out to be quite a complicated process, and the outputs of this are meant to be taken with a grain of salt anyways.

Lastly, focus on building in nuance. Naunce here includes:
- How much their major should impact fam choice (0 - neutral, -1 wants different majors, 1 wants same major)
- Personality (introversion / extraversion)
- Negative weights for people (maybe someone really hates a hobby, avoid matching them!)

### Group Matching
Once we have a successful approach to matching individuals with a similarity score, we can turn our attention to groups.

Given a list of hypotheical students, see how well the model is able to group them to minimize the differences. 

Once we have run on hypothetical students, try to run on real student entries and see if we can re-derive successful fams. Ask people from previous committees to see if they have opinions on the matching.

Potentially try and look into training the model with successful fams? Maybe we can feed the model fams like BUSA to adjust the weights slightly.

### User Friendliness
Lastly, if we are able to successfully pair groups together, find a clean way for non-computer literate people to use this tool.

Not everyone on committee will be comfortable with csv files or the terminal, so try and feed in the data through other means.

One approach could be feeding the program an excel sheet or something? Or maybe a web or app UI (which is a lot more work, maybe hire some help for this.)

I could also try and pre-process sentences into distinct words using FastText, and run it like that. That way, the user would just need to copy and paste a summary into the program instead of distinct words to directly use as tokens.
