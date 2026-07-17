from rfq_processor import process_rfq_request


def test_process_valid_rfq():
    payload = {
        "customer": "  BMW  ",
        "requirements": [
            {
                "category": "Safety",
                "text": "Emergency stop",
                "priority": 3,
            },
            {
                "category": "Electrical",
                "text": "400V",
                "priority": 1,
            },
            {
                "category": "Mechanical",
                "text": "IP65",
                "priority": 2,
            },
        ],
    }

    result = process_rfq_request(payload)

    ## assert: tatsächliches output muss genau dem erwartetem output entsprechen
    assert result == {
        "status": "success",
        "customer": "BMW",
        "total_requirements": 3,
        "high_priority_requirements": 2,
    }

def test_rejects_invalid_priority():
    payload = {
        "customer": "BMW",
        "requirements": [
            {
                "category": "Safety",
                "text": "Emergency stop",
                "priority": 5,
            }
        ],
    }

    result = process_rfq_request(payload)

    assert result == {
        "status": "error",
        "message": "Priority must be between 1 and 3",
    }



def test_rejects_requirements_that_are_not_a_list():
    payload = {
        "customer": "BMW",
        "requirements": "Emergency stop",
    }

    result = process_rfq_request(payload)

    assert result == {
        "status": "error",
        "message": "Requirements must be a list",
    }



def test_missing_customer():
    payload = {
        "requirements": [
            {
                "category": "Safety",
                "text": "Emergency stop",
                "priority": 3,
            }
        ],
    }

    result = process_rfq_request(payload)

    assert result == {
        "status": "error",
        "message": "Missing customer",
    }


def test_empty_requirements():
    payload = {
        "customer": "BMW",
        "requirements": [],
    }

    result = process_rfq_request(payload)

    assert result == {
        "status": "error",
        "message": "Requirements cannot be empty",
    }
