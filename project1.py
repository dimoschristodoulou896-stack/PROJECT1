import requests

url = "http://project1.local/wp-json/wp/v2/posts?per_page=3"

response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    print("Τελευταία 3 άρθρα:\n")
    for post in posts:
        print("-", post["title"]["rendered"])
else:
    print("Σφάλμα API:", response.status_code)