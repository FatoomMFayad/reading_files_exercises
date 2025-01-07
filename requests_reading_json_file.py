import requests

# URL containing JSON data
url = "https://jsonplaceholder.typicode.com/posts/1"

# Fetch the JSON data from the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON content
    data = response.json()
    print("JSON Data:", data)
else:
    print("Failed to retrieve data. HTTP Status Code:", response.status_code)