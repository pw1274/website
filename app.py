import requests
import json

# API URL
api_url = "https://api.penpencil.co/v2/batches/neev-2025-677246/subject/physics-591199/contents?page=1&contentType=videos&tag=motion-937143"

# Headers with token
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjkxNjI4MTEuODkxLCJkYXRhIjp7Il9pZCI6IjYzZmIwMTk3Mjc5MjVhMDAxOGVhYTkyOSIsInVzZXJuYW1lIjoiNjAwNTE2MTk2MyIsImZpcnN0TmFtZSI6IkF5dXNocmFqIiwibGFzdE5hbWUiOiJTSU5HSCIsIm9yZ2FuaXphdGlvbiI6eyJfaWQiOiI1ZWIzOTNlZTk1ZmFiNzQ2OGE3OWQxODkiLCJ3ZWJzaXRlIjoicGh5c2ljc3dhbGxhaC5jb20iLCJuYW1lIjoiUGh5c2ljc3dhbGxhaCJ9LCJlbWFpbCI6InJzODY1NzIyN0BnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiLCI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3Mjg1NTgwMTF9.TIbdXKz9N3Jn1fntrhLNnVFnEzMHK0gvwX3TdX62Jdw',  # Replace with your actual token
    'Content-Type': 'application/json'
}

# Send GET request to the API with headers
response = requests.get(api_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON data
    data = response.json()

    # Save the JSON data into a local file
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)

    print("JSON data saved to 'data.json'")
else:
    print(f"Failed to fetch data: {response.status_code}")
    print(response.text)
