import requests

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break
url=input('Please provide the url for the site: ')
#url = 'https://python.org/'

if not url.startswith("https://"):
    url = "https://" + url

with requests.get(url) as response:
    #html = response.text
    #more(html)

    print(f"\n The website headers of {url} are: \n , {response.headers} \n\n")

    