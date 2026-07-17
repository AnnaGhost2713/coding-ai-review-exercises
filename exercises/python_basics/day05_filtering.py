##############################################################
# Input: 
rfq = {
    "requirements": [
        {"category": "Safety", "text": "Emergency stop", "priority": 3},
        {"category": "Electrical", "text": "400V", "priority": 1},
        {"category": "Mechanical", "text": "IP65", "priority": 2},
    ]
}

threshold = 2

# Output: 
# [
#     {"category": "Safety", "text": "Emergency stop", "priority": 3},
#     {"category": "Mechanical", "text": "IP65", "priority": 2},
# ]

# Option 1: For Loop approach
def high_priority_requirements(rfq, threshold):
    high_priority_req = []

    for requirement in rfq["requirements"]: 
        if requirement["priority"] >= threshold: 
            high_priority_req.append(requirement)
    
    return high_priority_req

high_priority_requirements(rfq, threshold)



# Option 2: List Comprehension (most common)
def high_priority_requirements(rfq, threshold):
    high_priority_requirements = [
        requirement 
        for requirement in rfq["requirements"]
        if requirement["priority"] >= threshold
    ]

    return high_priority_requirements


# Option 3: Filter() function (least common)
def high_priority_requirements(rfq, threshold):
    high_priority_requirements = filter(
        lambda requirement: requirement["priority"] >= threshold, 
        rfq["requirements"])
    
    # filter returns filter object not a list -> have to cast it as a list
    return list(high_priority_requirements)