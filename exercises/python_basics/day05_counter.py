# Input:
# rfq = {
#     "requirements": [
#         {"category": "Safety"},
#         {"category": "Electrical"},
#         {"category": "Safety"},
#         {"category": "Mechanical"},
#         {"category": "Safety"},
#     ]
# }

# Output:
# [
#     ("Safety", 3),
#     ("Electrical", 1),
#     ("Mechanical", 1),
# ]

rfq = {
    "requirements": [
        {"category": "Safety"},
        {"category": "Electrical"},
        {"category": "Safety"},
        {"category": "Mechanical"},
        {"category": "Safety"},
    ]
}
# Input: dict[list] -> list(dict: category -> text)


## also Counter needs the list in the following format to work: 
# [
#     "Safety",
#     "Electrical",
#     "Safety",
#     "Mechanical",
#     "Safety",
# ]

from collections import Counter

def top_categories(rfq):
    list_categories = []
    for requirement in rfq["requirements"]: 
        list_categories.append(requirement["category"])
    counts = Counter(list_categories)
    return counts 

top_categories(rfq)

## Output of this code would be: 
Counter({
    "Safety": 3,
    "Electrical": 1,
    "Mechanical": 1
})



###### Step 2
# Output should be the following: 
[
    ("Safety", 3),
    ("Electrical", 1),
    ("Mechanical", 1),
]

from collections import Counter

def top_categories(rfq):
    list_categories = []
    for requirement in rfq["requirements"]: 
        list_categories.append(requirement["category"])
    counts = Counter(list_categories)
    return counts.most_common()

top_categories(rfq)




