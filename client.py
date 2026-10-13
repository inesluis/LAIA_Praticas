import requests

response = requests.post(
    "http://localhost:8000/predict",
    json={"features": [5.1, 3.5, 1.4, 0.2]},
)

print(response.json())

response = requests.post(
    "http://localhost:8000/predict-batch",
    json={"features": [[5.1, 3.5, 1.4, 0.2], [6.7, 3.0, 5.2, 2.3]]},
)

print(response.json())