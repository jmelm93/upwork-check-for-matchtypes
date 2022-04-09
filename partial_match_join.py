def partial_match_join_all_matches_returned(full_values, matching_criteria):
    """The partial_match_join_first_match_returned() function takes two series objects and returns a dataframe with all matching values (duplicating the full value).
    Args:
        full_values = This is the series that contains the full values for matching pair.
        matching_criteria = This is the series that contains the partial values for matching pair.

    """
    # capture attribute name before reassigning for col naming at bottom of function
    # attribute=full_values.name
    # print(attribute) # held on doing anything with this for the time being

    full_values = full_values.str.lower()
    matching_criteria = matching_criteria.str.lower()
    
    matching_criteria = matching_criteria.to_frame("match")
    full_values = full_values.to_frame("full")

    full_values = full_values.drop_duplicates() 
    
    output=[]

    for n in matching_criteria['match']:
        mask = full_values['full'].str.contains(n, case=False, na=False)
        df = full_values[mask]
        df_copy = df.copy()
        df_copy['match'] = n 
        output.append(df_copy)

    return output