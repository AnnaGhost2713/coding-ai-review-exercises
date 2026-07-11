# Topics
# - nested dictionaries
# - nested lists
# - defaultdict
# - production-style data processing


# Input: 
# rfqs = [
#     {
#         "customer": "BMW",
#         "language": "en",
#         "requirements": [
#             {"category": "Safety", "text": "Emergency stop button"},
#             {"category": "Electrical", "text": "400V supply"},
#         ],
#     },
#     {
#         "customer": "Siemens",
#         "language": "de",
#         "requirements": [
#             {"category": "Safety", "text": "Not-Aus erforderlich"},
#             {"category": "Mechanical", "text": "IP65 enclosure"},
#         ],
#     },
# ]
#
# Output: 
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


def group_requirements_by_category(rfqs):
    grouped_requirements = {}

    for rfq in rfqs:
        requirements = rfq["requirements"]

        for requirement in requirements:
            category = requirement["category"]
            text = requirement["text"]

            if category not in grouped_requirements:
                grouped_requirements[category] = []

            grouped_requirements[category].append(text)

    return grouped_requirements
        
### with defaultdict
from collections import defaultdict

def group_requirements_by_category(rfqs):
    grouped_requirements = defaultdict(list)

    for rfq in rfqs:

        for requirement in rfq["requirements"]:

            grouped_requirements[requirement["category"]].append(text = requirement["text"])

    return dict(grouped_requirements)