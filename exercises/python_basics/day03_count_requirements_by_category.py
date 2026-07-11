# Input: 
# {
#     "Safety": [
#         "Emergency stop button",
#         "Not-Aus erforderlich"
#     ],
#     "Electrical": [
#         "400V supply"
#     ],
#     "Mechanical": [
#         "IP65 enclosure"
#     ]
# }
#
#
# Output: 
# {
#     "Safety": 2,
#     "Electrical": 1,
#     "Mechanical": 1
# }



## Basic Python approach
# how to count elements of a list: len(list)
def count_requirements_by_category(grouped_requirements):
    counts = {}

    for category in grouped_requirements:
        counts[category] = len(grouped_requirements[category])

    return counts


# or a better way to loop over a dictionary via .items()
# dictionaries have items 

def count_requirements_by_category(grouped_requirements):
    counts = {}

    for category, requirements in grouped_requirements.items(): 
        counts[category] = len(requirements)
    
    return counts


