# Input payload: 
{
    "customer": "BMW",
    "requirements": [],
}

# Output: 
{
    "status": "success",
}

# wenn customer fehlt: 
{
    "status": "error",
    "message": "Missing customer",
}

# wenn requirements fehlt: 
{
    "status": "error",
    "message": "Missing requirements",
}


def process_rfq_request(payload):
    # note: here it only checks if the key exists and not if it is empty
    if "customer" not in payload: 
        return {
            "status": "error",
            "message": "Missing customer",
        }
    if "requirements" not in payload: 
        return {
            "status": "error",
            "message": "Missing requirements",
        } 
    return {
        "status": "success",
    }


### now additional rules: string must not be empty on top of no key 
{}                       # customer key is missing
{"customer": ""}         # key exists, but value is empty
{"customer": "BMW"}      # valid value

# wenn customer empty
{
    "status": "error",
    "message": "Customer cannot be empty",
}

# wenn requirements empty
{
    "status": "error",
    "message": "Requirements cannot be empty",
}


# Solution to include the empty string checks as well: 
def process_rfq_request(payload):
    if "customer" not in payload:
        return {
            "status": "error",
            "message": "Missing customer",
        }

    if "requirements" not in payload:
        return {
            "status": "error",
            "message": "Missing requirements",
        }

    # Check empty customer here
    # check for empty string == ""
    if payload["customer"] == "": 
        return {
            "status": "error",
            "message": "Customer cannot be empty",
        }
    # Check empty requirements here
    # check for empty list == []
    if payload["requirements"] == []: 
        return {
            "status": "error",
            "message": "Requirements cannot be empty",
        }

    return {
        "status": "success",
    }


### Final version (which also includes type checks): 
def process_rfq_request(payload):
    if "customer" not in payload:
        return {
            "status": "error",
            "message": "Missing customer",
        }

    if "requirements" not in payload:
        return {
            "status": "error",
            "message": "Missing requirements",
        }

    # Type checks
    if not isinstance(payload["customer"], str):
        return {
            "status": "error",
            "message": "Customer must be a string",
        }

    if not isinstance(payload["requirements"], list):
        return {
            "status": "error",
            "message": "Requirements must be a list",
        }

    # Empty-value checks
    # include ".strip()" here since "  " is technically not empty 
    if not payload["customer"].strip():
        return {
            "status": "error",
            "message": "Customer cannot be empty",
        }

    if not payload["requirements"]:
        return {
            "status": "error",
            "message": "Requirements cannot be empty",
        }

    return {
        "status": "success",
    }





##### Nach Prüfung der Payload gehen wir nun eine Ebene tiefer 
# payload
# → customer und requirements
# → requirements ist eine Liste
# → jedes Listenelement ist ein Dictionary
# → jedes Dictionary enthält die richtigen Felder
# → jedes Feld besitzt einen gültigen Wert

def check_requirements(payload):
    for requirement in payload["requirements"]:
        if not isinstance(requirement, dict):
            return {
                "status": "error",
                "message": "Each requirement must be a dictionary",
            }

        if "category" not in requirement:
            return {
                "status": "error",
                "message": "Missing category",
            }

        if "text" not in requirement:
            return {
                "status": "error",
                "message": "Missing text",
            }

        if "priority" not in requirement:
            return {
                "status": "error",
                "message": "Missing priority",
            }

        if not isinstance(requirement["category"], str):
            return {
                "status": "error",
                "message": "Category must be a string",
            }

        if not isinstance(requirement["text"], str):
            return {
                "status": "error",
                "message": "Text must be a string",
            }

        if not isinstance(requirement["priority"], int):
            return {
                "status": "error",
                "message": "Priority must be an integer",
            }

        if not requirement["category"].strip():
            return {
                "status": "error",
                "message": "Category cannot be empty",
            }

        if not requirement["text"].strip():
            return {
                "status": "error",
                "message": "Text cannot be empty",
            }

        if requirement["priority"] not in [1, 2, 3]:
            return {
                "status": "error",
                "message": "Priority must be between 1 and 3",
            }