import sys

import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.processor import clean_data
def analyze_data(responses):
    style_count = {}
    size_count = {}
    shoe_size_count = {}
    for response in responses :
        response = clean_data(response)
        style = response.get("style")
        size = response.get("size")
        shoe = response.get("shoe_size")
        if style in style_count:
            style_count[style] +=1
        else :
            style_count[style] = 1
        if size in size_count :
            size_count[size] +=1
        else: 
            size_count[size] = 1
        if shoe in shoe_size_count :
            shoe_size_count[shoe] += 1
        else :
            shoe_size_count[shoe] = 1

    top_style = max(style_count ,key =  style_count.get)
    top_size = max(size_count , key=size_count.get)
    top_shoe =  max(shoe_size_count , key= shoe_size_count.get) if shoe_size_count else None
    return{'top style': top_style,
           'top size': top_size,
           'top shoe size' : top_shoe}

