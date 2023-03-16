
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)


@app.post("/api/response")
def api_response():
    text = request.get_json().get("message")

    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)

'''
from flask import Flask
from flask import request
import chat


app = Flask(__name__)

@app.post("/api/response")
def OpenDiscusion():
    message = request.get_json().get('message','')
    response = chat.get_response(message)
    return (response)
'''
