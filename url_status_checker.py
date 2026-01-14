import requests

url = input("URL: ")

if not url.startswith("http"):
    url = "https://" + url

try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
                print(f"{url} is on-line\n")
        else:
                print(f"\n{url} returned error: {response.status_code}")
except:

        print(f"{url} failed (Conection error/DNS)")
