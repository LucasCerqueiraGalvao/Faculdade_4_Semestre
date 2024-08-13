import requests

html = requests.get("https://pypi.org/project/requests/")

print(html)
print(html.text)

