import pdb
import pandas as pd

omit_keywords = ["'", "for", "and", "in", "&"]
def matcher(value, match):
    match = match.copy()
    res = match.loc[match.phrase == value, "MatchID"]
    if len(res) > 0: return (res.iloc[0], "Full", "Exact Order")

    res = match.loc[match.phrase.str.contains(value), "MatchID"]
    if len(res) > 0: return (res.iloc[0], "Partially Match", "Exact Order")
    
    match.phrase = match.phrase.str.replace("'", "")
    value = value.replace("'", "")
    res = match.loc[match.phrase == value, "MatchID"]
    if len(res) > 0: return (res.iloc[0], "Full", "Removed apostrophe from Tag. Exact Order")

    res = match.loc[match.phrase.str.contains(value), "MatchID"]
    if len(res) > 0: return (res.iloc[0], "Partially Match", "Removed apostrophe from Tag. Partially Matched")

    match.phrase = match.phrase.str.split(" ")
    match.phrase = match.phrase.apply(lambda x: [a for a in x if a not in omit_keywords])
    value = [v for v in value.split(" ") if v not in omit_keywords]
    res = match.loc[match.phrase.apply(lambda x: all([a in x for a in value])), "MatchID"]
    if len(res) > 0: return (res.iloc[0], "Partially Match", "Removed apostrophe from Tag. Removed 'for'...")

    return (0, "No Match")




def partial_match_join_all_matches_returned(full_values, matching_criteria):
    """The partial_match_join_first_match_returned() function takes two series objects and returns a dataframe with all matching values (duplicating the full value).
    Args:
        full_values = This is the series that contains the full values for matching pair.
        matching_criteria = This is the series that contains the partial values for matching pair.

    """
    # capture attribute name before reassigning for col naming at bottom of function
    # attribute=full_values.name
    # print(attribute) # held on doing anything with this for the time being

    full_values = full_values.to_frame("full")
    full_values["phrase"] = full_values.full.str.lower()
    full_values = full_values.drop_duplicates()
    
    matching_criteria = matching_criteria.to_frame("match")
    matching_criteria["phrase"] = matching_criteria.match.str.lower()
    matching_criteria = matching_criteria.drop_duplicates()
    matching_criteria["MatchID"] = matching_criteria.index + 1

    full_values[["MatchID", "Match Type", "Reason"]] = full_values.phrase.apply(lambda x: matcher(x, matching_criteria)).apply(pd.Series)

    #after matching, there is no need of phrase columns
    full_values = full_values.drop("phrase", axis=1)
    matching_criteria = matching_criteria.drop("phrase", axis=1)

    full_values = full_values.merge(matching_criteria, on="MatchID", how="left").drop("MatchID", axis=1)
    return full_values