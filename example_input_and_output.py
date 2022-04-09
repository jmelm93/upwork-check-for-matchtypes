
import pandas as pd
from partial_match_join import partial_match_join_all_matches_returned
import pdb

#### INPUT 1 #####
d1 = pd.DataFrame({
    'URL': [
        "https://www.example.com/mens-halloween-costumes", 
        "https://www.example.com/womens-masks-for-halloween"
        ], 
    'Tag': [
        "Men's Halloween Costumes", 
        "Women's Masks for Halloween"
        ]})

#### INPUT 2 #####
d2 = pd.DataFrame({
    'URL': [
        "https://www.example.com/mens-halloween-costumes", 
        "https://www.example.com/mens-halloween-costumes", 
        "https://www.example.com/mens-halloween-costumes", 
        "https://www.example.com/mens-halloween-costumes", 
        "https://www.example.com/womens-masks-for-halloween",
        "https://www.example.com/womens-masks-for-halloween",
        "https://www.example.com/womens-masks-for-halloween"
        ], 
    'Keywords': [
        "men's halloween costumes", 
        "halloween costumes for mens",
        "costumes for halloween party",
        "costumes for halloween",
        "womens masks",
        "womens masks for halloween",
        "masks for halloween",
        ]})

#### OUTPUT #####
output = pd.DataFrame({
    'URL': [
        "https://www.example.com/mens-halloween-costumes", 
        "https://www.example.com/mens-halloween-costumes", 
        "https://www.example.com/mens-halloween-costumes", 
        "https://www.example.com/mens-halloween-costumes", 
        "https://www.example.com/womens-masks-for-halloween",
        "https://www.example.com/womens-masks-for-halloween",
        "https://www.example.com/womens-masks-for-halloween",
        "https://www.example.com/masks-for-halloween",
        ], 
    'Tag': [
        "Men's Halloween Costumes", 
        "Men's Halloween Costumes", 
        "Men's Halloween Costumes", 
        "Men's Halloween Costumes", 
        "Women's Masks for Halloween",
        "Women's Masks for Halloween",
        "Women's Masks for Halloween",
        "Men's & Women's Masks for Halloween",
        ],    
    'Keywords': [
        "men's halloween costumes", 
        "halloween costumes for mens",
        "costumes for halloween party",
        "costumes for halloween",
        "womens masks",
        "womens masks for halloween",
        "masks for halloween",
        "mens and womens masks for halloween",
        ],    
    'Match Type': [
        "Exact Match", 
        "Partial Match",
        "Partial Match",
        "No Match",
        "Partial Match",
        "Exact Match",
        "Partial Match",
        "Exact Match",
        ],    
    #### There are 3 potential phrases to include if the condition is met #####
    #### Phrase 1 == `Removed apostrophe from tag.` ## If an apostrophee had to be removed in order for match to be achieved
    #### Phrase 2 == Removed `_________`. ## If any "omitted words" were found in the keyword
    #### Phrase 3 == `Exact Order.` ## If the `Keyword`` is exact order of words in `Tag``
    'Reason': [
        "Exact Order.", 
        "Removed apostrophe from tag. Removed `for`.", ### Omitted Words == `for`, `and`, `in`
        "Removed apostrophe from tag. Removed `for`.", ### Omitted Words == `for`, `and`, `in`
        "Removed apostrophe from tag. Removed `for`.", ### Omitted Words == `for`, `and`, `in`
        "Removed apostrophe from tag.",
        "Removed apostrophe from tag. Exact Order.", ### Apostrophes are removed
        "Removed apostrophe from tag.",
        "Removed apostrophe from tag. Removed `and`. Exact Order.", ### Omitted Words == `for`, `and`, `in` ### `&` is converted into `and` for matching
        ]})

wip_function = partial_match_join_all_matches_returned(full_values=d2['Keywords'], matching_criteria=d1['Tag'])

print('##########')
print('##########')
print('##########')
print('WIP Script:')
print(wip_function)
print('##########')
print('##########')
print('##########')
print('Desired Output:')
print(output)