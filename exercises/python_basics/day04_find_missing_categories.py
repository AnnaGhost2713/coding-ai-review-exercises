# Input
# rfq = {
#     "customer": "BMW",
#     "requirements": [
#         {"category": "Safety", "text": "..."},
#         {"category": "Electrical", "text": "..."},
#     ]
# }

# required_categories = [
#     "Safety",
#     "Electrical",
#     "Mechanical",
#     "Compliance",
# ]

# Input rfq: dict of customer -> string, requirements -> list(dict) with the dict of category -> string, text -> string)
# Input required: list(string)



# Output
# ["Mechanical", "Compliance"]

# list(string)



# Idea Flow-wise: 
# go through all the requirements in the rfq
# for every requirement take the category 
# put it into a set (-> so we can always add it, since it will not be added a second time if it is already in there)
# compare the new set of different categories with the list of required categories 
### this comparison will probably happen via a for loop again then 
# and if a required category is not in the set, then it will be put into the output list 


def find_missing_categories(rfq, required_categories):
    temp_set = set()
    # remember this way how to initialize a list
    missing_categories = []

    for requirement in rfq["requirements"]: 
        temp_set.add(requirement["category"])
    
    for category_req in required_categories: 
        if category_req not in temp_set:
            missing_categories.append(category_req)
    
    return missing_categories


## Nicer/leaner way
def find_missing_categories(rfq, required_categories):
    temp_set = set()
    # remember this way how to initialize a list
    missing_categories = []

    for requirement in rfq["requirements"]: 
        temp_set.add(requirement["category"])
    
    required = set(required_categories)
    
    # Important: set difference here 
    missing_categories = required - temp_set

    # have to return a list again, because set output would look like this: {"Mechanical", "Compliance"} instead of ["Mechanical", "Compliance"]
    return list(missing_categories)