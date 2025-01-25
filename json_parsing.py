def flatten_json(y):
    """
    Flattens a nested json object and creates unique keys for each value.

    :param y: The JSON object to flatten.

    :return: A dictionary with flattened keys and values.
    """
    out = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], name + a + '_')
        else:
            out[name.rstrip('_')] = x

    flatten(y)
    return out

def get_column_names_from_flattened(flattened_json):
    """
    Extracts the column names from the flattened JSON in the order they appear.
    
    :param flattened_json: Flattened JSON data as a dictionary.
    
    :return: Tuple of column names in the order corresponding to the data values.
    """
    return tuple(flattened_json.keys())

