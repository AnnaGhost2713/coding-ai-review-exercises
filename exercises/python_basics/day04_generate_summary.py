# Input:
# {
#     "customer": "BMW",
#     "language": "en",
#     "requirements": [...]
# }
# Type: dict of strings and list

# Output:
# {
#     "customer": "BMW",
#     "language": "en",
#     "total_requirements": 3,
#     "requirements_by_category": {
#         "Safety": 2,
#         "Electrical": 1
#     }
# }
# Type: dict of strings, int, dict (nested dict)

from collections import defaultdict
def count_requirements_by_category(requirements): 
    requirements_by_category = defaultdict(int)
    for requirement in requirements: 
        category = requirement["category"]
        requirements_by_category[category] += 1
    
    return dict(requirements_by_category)



def generate_rfq_summary(rfq): 
    rfq_summary = {}

    rfq_summary["customer"] = rfq["customer"]
    rfq_summary["language"] = rfq["language"]
    rfq_summary["total_requirements"] = len(rfq["requirements"])
    rfq_summary["requirements_by_category"] = count_requirements_by_category(rfq["requirements"])
        
    
    return rfq_summary

