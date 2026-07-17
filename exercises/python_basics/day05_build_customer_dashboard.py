# Input
rfqs = [
    {
        "customer": "BMW",
        "requirements": [
            {"category": "Safety", "priority": 3},
            {"category": "Electrical", "priority": 1},
        ],
    },
    {
        "customer": "Audi",
        "requirements": [
            {"category": "Safety", "priority": 2},
            {"category": "Mechanical", "priority": 3},
        ],
    },
]

# Output
{
    "total_customers": 2,
    "total_requirements": 4,
    "high_priority_requirements": 3,
    "top_categories": [
        ("Safety", 2),
        ("Electrical", 1),
        ("Mechanical", 1),
    ],
}


# Hint: 
# Build it step by step:
# total_customers
# total_requirements
# high_priority_requirements (priority ≥ 2)
# top_categories


### Helper function 1: get total customers
# ideal output: integer
def total_customers(rfqs):
    customers = set()
    for rfq in rfqs:  
        customers.add(rfq["customer"])
    
    return len(customers)

# other option (a bit more pythonic): 
# {} create a set 
def total_customers(rfqs):
    return len({rfq["customer"] for rfq in rfqs})


### Helper function 2: get total requirements
def total_requirements(rfqs):
    number = 0
    for rfq in rfqs: 
        number = number + len(rfq["requirements"])

    return number

# better: 
def total_requirements(rfqs):
    number = 0
    for rfq in rfqs: 
        number += len(rfq["requirements"])

    return number



### Helper function 3: get high priority requirements
def high_priority_requirements(rfqs, threshold):
    count = 0
    # Important here: need nested for loop, i.e. 2 for loops
    # firstly into one single rfq inside all of the rfqs
    # secondly into the priorities within the list of requirements
    for rfq in rfqs: 
        for requirement in rfq["requirements"]:
            if requirement["priority"] >= threshold: 
                number += 1
    
    return count



### Helper function 4: get top categories
from collections import Counter
def top_categories(rfqs):
    # put all the categories into a list
    # run counter on this list
    # important: do not use set here since counter needs duplicates to count obv!!
    categories = []
    for rfq in rfqs: 
        for requirement in rfq["requirements"]:
            categories.append(requirement["category"])
    
    return Counter(categories).most_common()

# with list comprehension
from collections import Counter
def top_categories(rfqs):

    categories = [
        requirement["category"]
        for rfq in rfqs
        for requirement in rfq["requirements"]
    ]
    
    return Counter(categories).most_common()




### Combining it all together
def customer_dashboard(rfqs):
    customer_dashboard = {}

    customer_dashboard["total_customers"] = total_customers(rfqs)
    customer_dashboard["total_requirements"] = total_requirements(rfqs)
    customer_dashboard["high_priority_requirements"] = high_priority_requirements(rfqs, threshold=2)
    customer_dashboard["top_categories"] = top_categories(rfqs)

    return customer_dashboard

