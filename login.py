import requests
from bs4 import BeautifulSoup

header = {
    'user-agent': 'YOUR USER AGENT FROM BROWSER'
}
login_data = {
    # you can find this in the headers of the web page
    # it will look like  this
    'key' : 'value'
}
s =  requests.Session()
url = 'TARGET URL'
r = s.get(url, headers = header)
# i will use html5lib to parse the html file
soup = BeautifulSoup(r.content, 'html5lib')
login_data['form_build_id'] = soup.find('input', attrs={'name': 'form_build_id'})['value']
# the post function to the server
r = s.post(url, data=login_data, headers=header)
print(r.text)



