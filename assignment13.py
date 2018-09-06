import requests
response=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=text")
print(response.content)
