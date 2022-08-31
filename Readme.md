# <p align='center'>🌐 Python-translator 🌐</p>

<p align='center' style="font-size:25px;">🔥💯 V2 now supports multiple translations
💯🔥</p>

# 🔥 Setup
<<<<<<< Updated upstream
!! ( Go to the usage section if you want to test it right away from my server )
## Packages
```
> pip install "Flask[async]" flask-pydantic flask googletrans==3.1.0a0
```
=======

>>>>>>> Stashed changes
## Create a virtual environment for python

```
> python -m venv env
```

## Activate the virtual environment

```
> env\Scripts\activate
```

## Packages
```
> pip install "Flask[async]" flask-pydantic flask googletrans==3.1.0a0 flask-cors flask-pydantic
```

## Save all project dependencies to a file

```
> pip freeze > requirements.txt
```

## To install the dependencies mentioned in requirements.txt

```
> pip install -r requirements.txt
```

## Setting the env variable

```
> $env:FLASK_APP="module"
```
## Run the app

```
> flask run --reload
```
# 🔥 Usage

## ⭐⭐ V2 ⭐⭐

### ✅ Url

```
localhost:5000
```

or ( the deployed one )

```
https://cooood.pythonanywhere.com
```

### ✅ EndPoint

```
/v2/translate
```

### ✅ Method

```
POST
```

### ✅ Request body (raw json)

```json
{
  "texts": {
    "text1": "The first text to translate",
    "text2": "the second text to translate",
    "randomFieldName": "the third text to translate",
    "helloworld": "font icons for all projects, large or small"
  },
  "to_language": "fr"
}
```

### ✅ Response (status 200)

```json
{
  "from_language": "auto",
  "to_language": "fr",
  "translated": {
    "text1": "Le premier texte à traduire",
    "text2": "Le deuxième texte à traduire",
    "randomFieldName": "Le troisième texte à traduire",
    "helloworld": "icônes de police pour tous les projets, grands ou petits"
  }
}
```

## ⭐⭐ V1 ⭐⭐

### ✅ Url

```
localhost:8000
```

or

```
https://cooood.pythonanywhere.com
```

### ✅ EndPoint

```
/v1/translate
```

### ✅ Method

```
POST
```

### ✅ Request body (raw json)

```json
{
  "text": "Wikipedia provides all its content for free, without advertising, and without using the exploitation of the personal data of its users.",
  "to_language": "fr"
}
```

### ✅ Response (status 200)

```json
{
  "from_language": "auto",
  "to_language": "fr",
  "translated": "Wikipedia fournit tout son contenu gratuitement, sans publicité, et sans utiliser l'exploitation des données personnelles de ses utilisateurs."
}
```
