### Helper functions

# Instead of doing all the checks directly in process_rfq_request() we build: 

# Für gültige Daten: 
None

# Für ungültige Daten: 
{
    "status": "error",
    "message": "...",
}

# Why none for success?
# then this can be in the main fct. later
# validation_error = validate_rfq_payload(payload)

# if validation_error:
#     return validation_error



#### HELPER FUNKTION FÜR REQUIREMENT VALIDATION: 

def validate_requirement(requirement):
    if not isinstance(requirement, dict):
        return {
            "status": "error",
            "message": "Each requirement must be a dictionary",
        }

    if "category" not in requirement:
        return {"status": "error", "message": "Missing category"}

    if "text" not in requirement:
        return {"status": "error", "message": "Missing text"}

    if "priority" not in requirement:
        return {"status": "error", "message": "Missing priority"}
    

    # Type checks 
    if not isinstance(requirement["category"], str): 
        return {"status": "error", "message": "Category must be a string"}
    
    if not isinstance(requirement["text"], str): 
        return {"status": "error", "message": "Text must be a string"}
    
    # Stricter type check for integers
    if type(requirement["priority"]) is not int:
        return {"status": "error", "message": "Priority must be an integer"}
    

    # Not empty check 
    if not requirement["category"].strip(): 
        return {"status": "error", "message": "Category cannot be empty"}
    
    if not requirement["text"].strip(): 
        return {"status": "error", "message": "Text cannot be empty"}
    
    # if not requirement["priority"] würde nur 0 ablehnen, da eine Zahl nicht wirklich leer ist
    # daher eher das Intervall aller möglicher Zahlen checken
    if requirement["priority"] not in [1, 2, 3]: 
        return {"status": "error", "message": "Priority cannot be empty"}
    

    return None


def validate_rfq_payload(payload):

    ### ÄUßERE PAYLOAD VALIDIEREN

    # 1. Ist payload ein Dictionary?
    if not isinstance(payload, dict): 
        return {"status": "error", "message": "Payload must be a dictionary"}
    
    # 2. Existiert customer?
    if "customer" not in payload: 
        return {"status": "error", "message": "Missing customer"}
    
    # 3. Ist customer ein String?
    if not isinstance(payload["customer"], str): 
        return {"status": "error", "message": "Customer must be a string"}
    
    # 4. Ist customer nach .strip() noch nicht leer?
    if not payload["customer"].strip(): 
        return {"status": "error", "message": "Customer cannot be empty"}
    
    # 5. Existiert requirements?
    if "requirements" not in payload: 
        return {"status": "error", "message": "Missing requirements"}

    # 6. Ist requirements eine Liste?
    if not isinstance(payload["requirements"], list):
        return {"status": "error", "message": "Requirements must be a list"}

    # 7. Ist requirements nicht leer?
    if not payload["requirements"]: 
        return {"status": "error", "message": "Requirements cannot be empty"}
    

    ### EINZELNE REQUIREMENTS VALIDIEREN
    for requirement in payload["requirements"]: 
        validation_error = validate_requirement(requirement)

        if validation_error: 
            return validation_error

    return None 

