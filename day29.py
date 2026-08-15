import requests


def fetch_github_user(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as error:
        print(f"API Error: {error}")
        return None


username = input("Enter GitHub username: ").strip()

data = fetch_github_user(username)

if data:
    print("\nGitHub Profile")
    print("-" * 40)
    print(f"Name       : {data.get('name')}")
    print(f"Username   : {data.get('login')}")
    print(f"Repos      : {data.get('public_repos')}")
    print(f"Followers  : {data.get('followers')}")
    print(f"Following  : {data.get('following')}")