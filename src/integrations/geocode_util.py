#pylint: disable=missing-module-docstring,multiple-imports,multiple-statements,broad-exception-caught,missing-timeout,consider-using-f-string

import os, requests
from dotenv import load_dotenv
from utils import reader

def get_structured_address():
    """
    Given a partial address, returns the full structured address using LocationIQ API.
    """
    load_dotenv()
    items = reader.read_json(os.getenv("DATA_INPUT_PATH"))
    i=0; liq_addresses = []
    for item in items:
        params = {
            "key": os.getenv("LOCATIONIQ_API_KEY"),
            "q": item['project_address'],
            "format": "json",
            "addressdetails": 1
        }
        try:
            response = requests.get(os.getenv("LIQ_SEARCH_URL"), params=params)
            jarr = response.json()
            for je in jarr:
                liq_addresses.append(je['address'])
                liq_addresses[i]['class'] = je['class']
                liq_addresses[i]['type'] = je['type']
                liq_addresses[i]['lon'] = je['lon']
                liq_addresses[i]['lat'] = je['lat']
        except Exception as e:
            print("EXCEPTION: {}".format(e))
        i+=1
    return liq_addresses
    #pass
