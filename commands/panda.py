import requests

def get_panda():
    resp = requests.get("https://some-random-api.ml/animal/panda",)
    if 300 > resp.status_code >= 200:
        content = resp.json()
        link = content.get('image')
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    return link