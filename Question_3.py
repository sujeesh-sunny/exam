"""
once match rate is found sort that array of dictionary using the match rate
"""

import Question_2
def array_sorting(items,match_rate) :
    match_rate = 100
    print(f"Item: {items['name']}, Match Rate: {items['match_rate']}")
    for item in items :
        if item == match_rate :
            return match_rate.sort()
        print(array_sorting,match_rate)