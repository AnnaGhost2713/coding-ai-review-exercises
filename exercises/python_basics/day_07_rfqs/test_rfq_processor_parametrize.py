import pytest
from rfq_processor import process_rfq_request

# decorator to run the same test with different inputs
@pytest.mark.parametrize(
    # Parameter, die später in die test function unten reingegeben werden
    # jeder tupel block besteht aus genau 2 teilen, konkret s. was darin steht {}
    "payload, expected",
    [
        ( 
            # Testfall 1: 
            {
                # Teil 1: payload
                "customer": "BMW",
                "requirements": "Emergency stop",
            },
            {
                # Teil 2: expected
                "status": "error",
                "message": "Requirements must be a list",
            },
        ),

        (
            # Testfall 2: 
            {
                "requirements": [
                    {
                        "category": "Safety",
                        "text": "Emergency stop",
                        "priority": 3,
                    }
                ],
            },
            {
                "status": "error",
                "message": "Missing customer",
            },
        ),
        (
            # Testfall 3: 
            {
                "customer": "BMW",
                "requirements": [],
            },
            {
                "status": "error",
                "message": "Requirements cannot be empty",
            },
        ),
    ],
)
def test_rejects_invalid_payloads(payload, expected):
    result = process_rfq_request(payload)

    assert result == expected