import http.client

conn = http.client.HTTPSConnection("dog.ceo")

headersList = {
         "Accept": "*/*",
          "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
          }

payload = ""

conn.request("GET", "/api/breeds/image/random", payload, headersList)
response = conn.getresponse()
result = response.read()

print(result.decode("utf-8"))
