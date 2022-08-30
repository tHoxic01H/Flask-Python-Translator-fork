from flask import Flask, request
from module.models.translation.TranslationModelV1 import TranslationModelV1
from module.models.translation.TranslationModelV2 import TranslationModelV2
from module.controllers.translation.translation_controller import translate_v1
from module.controllers.translation.translation_controller import translate_v2
	
from flask_pydantic import validate

app = Flask(__name__)

@app.route("/",methods=["POST"])
def root():
    json_datas = request.get_json()
    return json_datas
@app.route("/ping")
async def ping():
    return {
        "message":"Pinged successfully"
    }

# Translate V2
@app.post("/v2/translate")
@validate()
def translate_function_v2(body: TranslationModelV2):
    res = translate_v2(body)
    return res

# Translate V1
@app.route("/v1/translate")
def translate_function_v1(translation_body_v1: TranslationModelV1):
    res = translate_v1(translation_body_v1)
    return res

# if __name__ == "__main__":
#     app.run(debug=True)