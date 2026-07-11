# Input: 
# tickets = [
#     {
#         "customer": "BMW",
#         "priority": "high",
#         "title": "API timeout"
#     },
#     {
#         "customer": "Audi",
#         "priority": "low",
#         "title": "Typo"
#     },
#     {
#         "customer": "BMW",
#         "priority": "high",
#         "title": "Authentication failed"
#     },
#     {
#         "customer": "Audi",
#         "priority": "medium",
#         "title": "Invoice issue"
#     }
# ]
#
# Output: 
# {
#     "BMW": [
#         {
#             "customer": "BMW",
#             "priority": "high",
#             "title": "API timeout"
#         },
#         {
#             "customer": "BMW",
#             "priority": "high",
#             "title": "Authentication failed"
#         }
#     ],
#     "Audi": [
#         {
#             "customer": "Audi",
#             "priority": "low",
#             "title": "Typo"
#         },
#         {
#             "customer": "Audi",
#             "priority": "medium",
#             "title": "Invoice issue"
#         }
#     ]
# }

def group_by_customer(tickets):
    customers = {}

    # iterate over the list of tickets first
    for ticket in tickets: 
        customer = ticket["customer"]

        if customer not in customers: 
            customers[customer] = []

        customers[customer].append(ticket)

    return customers





def group_by_customer(tickets):
    customers = {}

    for ticket in tickets: 
        customer = ticket["customer"]

        if customer not in customers: 
            customers[customer] = []
        
        customers[customer].append(ticket)

    return customers 


from collections import defaultdict
def group_by_customer_defaultdict(tickets):
    customers = defaultdict(list)

    for ticket in tickets: 
        customer = ticket["customer"]

        customers[customer].append(ticket)

    return customers


tickets = [
    {"customer": "BMW", "priority": "high", "title": "API timeout"},
    {"customer": "Audi", "priority": "low", "title": "Typo"},
    {"customer": "BMW", "priority": "high", "title": "Authentication failed"},
]

print(group_by_customer(tickets))
print(group_by_customer([]))