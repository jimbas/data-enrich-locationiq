#pylint: disable=missing-module-docstring,consider-using-f-string
import json

def write_json(data, path):
    """
    Writes an iterator of dicts to a JSON file.
    Args:
        data (iterable): An iterator of dictionaries to write to the JSON file.
        path (str): The file path where the JSON data will be written.
    """
    with open(path, "w", encoding='utf-8') as ofl:
        ofl.write("[")
        for d in data:
            ofl.write("{}".format(json.dumps(d, indent=4, ensure_ascii=False)))
        ofl.write("]\n")
    #pass
