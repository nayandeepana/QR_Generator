import requests

user=input("Enter the URL of your Website : ")
url=f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={user}"
r=requests.get(url)
with open("image.jpg", "wb") as f:
    f.write(r.content)
    print("!!!   Successfully Generated   !!!")
