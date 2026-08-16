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
    
    #OOP Integration
    
    class GitHubProfile:

     def __init__(self, data):
        self.name = data.get("name")
        self.username = data.get("login")
        self.repos = data.get("public_repos", 0)
        self.followers = data.get("followers", 0)
        self.following = data.get("following", 0)

    def display(self):
        print("\n" + "=" * 50)
        print("           GITHUB PROFILE")
        print("=" * 50)

        print(f"Name       : {self.name or 'Not Available'}")
        print(f"Username   : {self.username}")
        print(f"Repositories: {self.repos}")
        print(f"Followers  : {self.followers}")
        print(f"Following  : {self.following}")

        print("=" * 50)


# Example data
profile_data = {
    "name": "Altamash Siddiqui",
    "login": "altamash-siddiqui",
    "public_repos": 25,
    "followers": 40,
    "following": 30
}

profile = GitHubProfile(profile_data)
profile.display()

#Developer Activity Analyzer

def analyze_developer(profile):
    repos = profile.repos
    followers = profile.followers

    print("\n📊 DEVELOPER ANALYSIS")
    print("-" * 40)

    if repos >= 50:
        print("Repository Activity : 🔥 Excellent")
    elif repos >= 20:
        print("Repository Activity : 🚀 Strong")
    elif repos >= 5:
        print("Repository Activity : 👍 Growing")
    else:
        print("Repository Activity : 🌱 Beginner")

    if followers >= 100:
        print("Community Presence  : 🌟 Excellent")
    elif followers >= 25:
        print("Community Presence  : 👍 Good")
    else:
        print("Community Presence  : 📈 Growing")

    activity_score = min(repos * 2 + followers, 100)

    print(f"Developer Score     : {activity_score}/100")


analyze_developer(profile)