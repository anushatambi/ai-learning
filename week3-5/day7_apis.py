import requests
import json

response = requests.get("https://api.github.com/users/anushatambi")
if response.status_code == 200:
    data = response.json()
    print(f"Name: {data.get('name','N/A')}")
    print(f"Bio: {data.get('bio','N/A')}")
    print(f"Followers: {data.get('followers',0)}")
    print(f"Public Repos: {data.get('public_repos',0)}")
else:
    print(f"Error: {response.status_code}")


response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    data = response.json()
    print(f"Title: {data.get('title','N/A')}")
    print(f"Body: {data.get('body','N/A')}")
else:
    print(f"Error: {response.status_code}")


def fetch_github_user(username):
    try:
        response = requests.get(
            f"https://api.github.com/users/{username}",
            timeout=10  
        )
        
        if response.status_code == 200:
            data = response.json()
            return {
                "name": data.get("name", "N/A"),
                "bio": data.get("bio", "N/A"),
                "public_repos": data.get("public_repos", 0),
                "followers": data.get("followers", 0)
            }
        elif response.status_code == 404:
            return {"error": "User not found"}
        elif response.status_code == 429:
            return {"error": "Rate limited — slow down"}
        else:
            return {"error": f"Unexpected error: {response.status_code}"}

    except requests.exceptions.ConnectionError:
        return {"error": "No internet connection"}
    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Something went wrong: {e}"}

result = fetch_github_user("anushatambi")
print(result)