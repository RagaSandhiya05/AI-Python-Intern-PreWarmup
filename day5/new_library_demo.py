import httpx

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = httpx.get(url, timeout=10.0)

    response.raise_for_status()

    data = response.json()

    print("Status Code:", response.status_code)
    print("Post Title:", data["title"])
    print("Post Body:", data["body"])

except httpx.HTTPError as error:
    print("Request failed:", error)
