from flask import Flask, request
from config import HOST, PORT, DEBUG, GPT_MODEL, MAX_TOKENS, TEMPERATURE
from model_service import ModelService

app=Flask(__name__)

model_service=ModelService()

@app.route("/info_api", methods=["GET"])
def hello():
    valor_a_retornar={
        "success":True,
        "params":{
            "model":GPT_MODEL,
            "max_tokens":MAX_TOKENS,
            "temperature":TEMPERATURE
        }
    }
    return valor_a_retornar

@app.route("/api/v1/predict", methods=["POST"])
def predict():
    json=request.json
    prompt=json.get("prompt")

    result=model_service.predict(prompt=prompt)

    return {
        "success":True,
        "result":result
    }

@app.route("/api/v1/image", methods=["POST"])
def image():
    json=request.json
    prompt=json.get("prompt")

    result=model_service.image(prompt=prompt)

    return {
        "success":True,
        "result":result
    }







if __name__=="__main__":
    app.run(
        port=PORT,
        host=HOST,
        debug=DEBUG

    )



