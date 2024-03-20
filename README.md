# ollama-test-repo


Install Ollama CLI using ollama.com

Install gemma-7b using : ollama run gemma

Install Flask and requests using pip

Run ollama_api.py to deploy the API

Send a Get/POST request to the API to get the response


## Sample prompt to run on openai:

Given a dict which maps actions to reasons, can you tell me which action should be taken if a customer ends a call suddenly. Dict is : sms_magic_dict = {
    "nurture": "When a call is ended with a customer successfully send nurture messages to continue conversations with the customer",
    "reminder": "When a transaction is not completed, send reminders to the customer for completing the transactions",
    "notification": "When the client is not responding , send notifications to the client"
}