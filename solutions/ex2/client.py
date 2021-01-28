import requests
from pprint import pprint

TOKEN = "###" # Insert token here


# Get all available languages
URL_LANGUAGES = "https://google-translate1.p.rapidapi.com/language/translate/v2/languages"

headers = {
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': TOKEN,
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
}

response = requests.get(URL_LANGUAGES, headers=headers)

data = response.json()
languages = [d["language"] for d in data["data"]["languages"]]
print("Available languages:")
print(languages)


# Detect the language used in the POST data
URL_DETECT = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

payload = {"q": "Me gustan los trenes"}
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': TOKEN,
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
 }

response = requests.post(URL_DETECT, data=payload, headers=headers)
print(response.url)
resp = response.json()
language = resp["data"]["detections"][0][0]["language"]
confidence = resp["data"]["detections"][0][0]["confidence"]
print(f"Language {language} with confidence {confidence}")


def translate(text, source, target):
    # Translate text between two languages
    URL_TRANSLATE = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        "q": text,
        "source": source,
        "target": target,
    }
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept-encoding': "application/gzip",
        'x-rapidapi-key': TOKEN,
        'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }

    response = requests.post(URL_TRANSLATE, data=payload, headers=headers)
    resp = response.json()
    translated = resp["data"]["translations"][0]["translatedText"]
    print(f"Original text in {payload['source']}: {payload['q']}")
    print(f"Translated text in {payload['target']}: {translated}")
    return translated

print("\n\nTranslation")
while True:
    text = input("Text to translate: ")
    source = input("Source language: ")
    target = input("Target language: ")
    translate(text, source, target)