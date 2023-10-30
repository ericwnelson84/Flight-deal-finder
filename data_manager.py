import requests
import os

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/6002465be9d0759ca74e418579ad0e41/flightFinder/sheet1'
SHEETY_USERS_ENDPOINT = 'https://api.sheety.co/6002465be9d0759ca74e418579ad0e41/flightFinder/sheet2'

BEARER = 'bearer_token_here'
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        headers = {
            "Authorization": f"Bearer {BEARER}",
        }
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["sheet1"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data


    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            headers = {
                "Authorization": f"Bearer {BEARER}",
            }
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )
            # print(response.text)

    def get_customer_emails(self):
        headers = {
            "Authorization": f"Bearer {BEARER}",
        }
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(customers_endpoint, headers=headers)
        data = response.json()
        self.customer_data = data["sheet2"]
        return self.customer_data


