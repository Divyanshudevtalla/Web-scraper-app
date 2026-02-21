#We use the requests library to get the content of the webpage
import requests as req
#We take the URL as input from the user
urlin=input("Enter the URL:")
response= req.get(urlin)
#We check if the request was successful
if response.status_code == 200:
    data= response.json()

    print("Successfully retrieved webpage content.")
else:
    print(f"Failed to retrieve webpage. Status code: {response.status_code}")
    pass