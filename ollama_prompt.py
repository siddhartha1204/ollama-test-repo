import requests

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"


sms_magic_dict = {
    "nurture": "When a call is ended with a customer successfully send nurture messages to continue conversations with the customer",
    "reminder": "When a transaction is not completed, send reminders to the customer for completing the transactions",
    "notification": "When the client is not responding , send notifications to the client"
}

call_codes = {
 'call_ended': "Customer ended the call after completing the discussion with the agent",
 'call_hangup': "Customer hung up on the call abruptly",
 'call_disconnected': "Call disconnected due to network issues"
}


def get_gemma_response(event_code):
    system_prompt = 'Your goal is to reply as an agent to a customer using sms'
    conversation_string = call_codes.get(event_code, None)

    if not conversation_string:
        return None

    ollama_prompt = f"{system_prompt}: {conversation_string}"

    ollama_data = {
        "model": "gemma",
        "prompt": ollama_prompt,
        "stream": False,
        "keep_alive": "10m",
    }

    response = requests.post(OLLAMA_ENDPOINT, json=ollama_data)
    return response.json()["response"]