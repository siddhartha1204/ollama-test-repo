from flask import Flask, jsonify, request
from ollama_prompt import get_gemma_response
app = Flask(__name__)


@app.route('/ollama_response', methods=['GET', 'POST'])
def price_trend_from_id():
    event_code  = request.json.get('event_code')
    print(event_code)
    out = get_gemma_response(event_code)
    if out:
        return out
    else:
        return jsonify({'error': 'event code not found'})


app.run(debug=True, port=1234, host='0.0.0.0')