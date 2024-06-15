from datetime import *
import requests

pixela_endpoint = "https://pixe.la/"
USERNAME = "missbellum"
TOKEN = "3E4R5T6Y7UT6Y7U8I9O0"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=f"{pixela_endpoint}//v1/users", json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/v1/users/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "CodingGraph",
    "unit": "commit",
    "type": "float",
    "color": "momiji",
    "timezone": "Africa/Lagos"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

creation_endpoint = f"{graph_endpoint}/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

time_now = datetime.now()
pixel_data = {
    "date": time_now.strftime("%Y%m%d"),
    "quantity": input("How many hours did you do? "),
}

# can also update and delete using put and delete requests
response = requests.post(url="https://pixe.la//v1/users/missbellum/graphs/graph1", json=pixel_data, headers=headers)
print(response.text)
