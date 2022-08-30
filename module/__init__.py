from flask import Flask, request
from module.models.translation.TranslationModelV1 import TranslationModelV1
from module.models.translation.TranslationModelV2 import TranslationModelV2
from module.controllers.translation.translation_controller import translate_v1
from module.controllers.translation.translation_controller import translate_v2
	
from flask_pydantic import validate

app = Flask(__name__)

@app.get("/")
def root():
    return """
    <html>
    <header>
        <title>Python translator</title>
    </header>
    <body style="display:flex;justify-content:center;align-items:center;font-family:sans-serif">
        <h1>Read the documentation <a href="https://github.com/CedricRabarijohn/Flask-Python-Translator">here</a></h1>
    </body>
    </html>
    """

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
@app.post("/v1/translate")
@validate()
def translate_function_v1(body: TranslationModelV1):
    res = translate_v1(body)
    return res

if __name__ == "__main__":
    app.run(debug=True)