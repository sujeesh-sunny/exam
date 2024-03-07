"""
from the dictioanry thus created from question_1, 
write a program to accept a key word from  user and return a array of dictinary with item name and its the match rate


eg:

Enter keyword: Pink apple
result:[
    {
        "name": "Granny Smith Apples",
        "mathch rate":80
    }
    {
        "name": "Pink Lady Apples",
        "mathch rate":95
    }
    {
        "name": "Honey Crisp apple",
        "mathch rate":85
    }
]
match rate is percentage

match rate shown below are random not generated using program

Remember user can give any keyword in any format you have to clean it
"""
import json

def match_rate(item_name, keyword):
    if keyword.lower() in item_name.lower():
        return len(set(keyword.lower().split()) & set(item_name.lower().split())) / len(set(keyword.lower().split())) * 100
    else:
        return 0

with open("data.json", 'r') as file:
    data = json.load(file)

keyword = input("Enter keyword: ")

result = []
for item in data["items"]:
    item_name = item["name"]
    result.append({
        "name": item_name,
        "match_rate": match_rate(item_name, keyword)
    })

for item in result:
    print(f"Item: {item['name']}, Match Rate: {item['match_rate']}")