import requests
import time

print(requests.post("http://127.0.0.1:5000/image", files={"image": open(r"/Users/albrino/Downloads/Old-Items/ChromeExtensionScrapingHelloWorld/images/71YXjHyWT5L._AC_SX679_.jpg", "rb")}))
time.sleep(8)

#make a request to the API GET
r=requests.get("http://127.0.0.1:5000/imageCheck?filename=trash.png")
print(r.text)