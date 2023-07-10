import requests

# Set the desired user agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"

# Set the URL of the web page you want to scrape
url='https://www.neobyte.es/tarjeta-grafica-asus-dual-rtx3060-oc-v2-12gb-9514.html'

# Send a GET request with the specified user agent
headers = {"User-Agent": user_agent}
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the value of the desired ID from the web page
    html_content = response.text
    value = html_content.find("#btnsWishAddBuy")

    if value != -1:
        print("Value found:", value)
    else:
        print("Value not found.")
else:
    print("Request failed with status code:", response.status_code)
