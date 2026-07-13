# Input:
# rfq = {
#     "customer": "BMW",
#     "requirements": [
#         {"category": "Safety", "text": "Emergency stop", "priority": 3},
#         {"category": "Electrical", "text": "400V", "priority": 1},
#         {"category": "Mechanical", "text": "IP65", "priority": 2},
#     ]
# }

# Input: dict(customer -> string, requirements -> list(dict))

# Output:
# [
#     {"category": "Safety", "text": "Emergency stop", "priority": 3},
#     {"category": "Mechanical", "text": "IP65", "priority": 2},
#     {"category": "Electrical", "text": "400V", "priority": 1},
# ]

# Output: list(dict)


# Flow explained: 
## we take the whole requirements list from the rfq dictionary
## and put this list into our newly created list
## and then this newly created list we sort for every requirements by the priority key 

# Use function sorted(iterable, key=key, reverse=reverse)
# with iterable: Required. The sequence to sort, list, dictionary, tuple etc.
# with key: Optional. A Function to execute to decide the order. Default is None
# with reverse: Optional. A Boolean. False will sort ascending, True will sort descending. Default is False
def sort_requirements_by_priority(rfq):
    sorted_requirements = sorted(rfq["requirements"], 
                                 key = lambda requirement : requirement["priority"], 
                                 reverse = True)

    return sorted_requirements

