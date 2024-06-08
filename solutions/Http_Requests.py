import requests

url = "https://api.github.com/users/python"
try:
    response = requests.get(url)
    print(response.text)
except:
    print("No internet connectivity.")
