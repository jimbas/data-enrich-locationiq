#pylint: disable=missing-module-docstring
import json

def read_json(path):
    """
    Reads JSON files from a specified directory and yields each record.
    Args:
        path (str): The directory containing JSON files.
    Yields:
        dict: Each record from the JSON files.
    """
    with open(path, 'r', encoding='utf-8') as ifl:
        return json.load(ifl)
    #pass
