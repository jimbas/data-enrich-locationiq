#pylint: disable=missing-module-docstring,multiple-imports,multiple-statements,broad-exception-caught,missing-timeout,consider-using-f-string
import os
from dotenv import load_dotenv
from utils import reader
from utils import writer

def transform(address_iter):
    """
    Transforms an iterator of address dictionaries by enriching each address.
    Yields enriched addresses one by one.
    """
    load_dotenv()
    items = reader.read_json(os.getenv("DATA_INPUT_PATH"))
    i=0
    for item in items:
        items[i]['liq_addresses'] = []
        for addr in address_iter:
            items[i]['liq_addresses'].append(addr)
        _ = item
        i+=1
    writer.write_json(items, os.getenv("DATA_OUTPUT_PATH"))
    #pass
