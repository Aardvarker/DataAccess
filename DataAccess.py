# Import an HTTP library 
import requests
import json 
from pprint import pprint
entered_street = input("Enter Street:")

# Make the request 
r = requests.get('https://www.stlouis-mo.gov/powernap/stlouis/api.cfm/requests.json?',
params={'api_key':"MTU3MDIxNDg5NjMwNjAuODk1NDE4MzI4NDYx",
         'start_date': "2019-10-13",'end_date': "2019-10-13 "
}
 )
 
# The returned data 
json_response = r.json()
length = len(json_response)
print(length)
for i in range(length):
   d = json_response[i]
   if (entered_street in d['ADDRESS']& i =="ADDRESS"):
      pprint(d)
print(length)