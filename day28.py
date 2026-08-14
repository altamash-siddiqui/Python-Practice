import requests


def get_github_user(username):
    """Fetch GitHub profile information using GitHub's public API."""

    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return response.json()

        if response.status_code == 404:
            print("\n❌ GitHub user not found.")
            return None

        print(f"\n⚠️ API Error: {response.status_code}")
        return None

    except requests.exceptions.Timeout:
        print("\n⏱️ Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("\n🌐 Internet connection error.")

    except requests.exceptions.RequestException as error:
        print(f"\n❌ Request failed: {error}")

    return None


def display_profile(profile):
    """Display GitHub profile information in a clean format."""

    if not profile:
        return

    print("\n" + "=" * 60)
    print("              GITHUB DEVELOPER PROFILE")
    print("=" * 60)

    print(f"👤 Name           : {profile.get('name') or 'Not available'}")
    print(f"🔗 Username       : {profile.get('login')}")
    print(f"📍 Location       : {profile.get('location') or 'Not available'}")
    print(f"📝 Bio            : {profile.get('bio') or 'Not available'}")
    print(f"📦 Repositories   : {profile.get('public_repos', 0)}")
    print(f"👥 Followers      : {profile.get('followers', 0)}")
    print(f"👤 Following      : {profile.get('following', 0)}")
    print(f"⭐ GitHub URL     : {profile.get('html_url')}")

    print("=" * 60)


def main():
    print("\n" + "=" * 60)
    print("        🚀 GITHUB PROFILE ANALYZER")
    print("=" * 60)

    print("\nThis program uses the GitHub API to analyze a profile.")

    while True:
        username = input("\nEnter GitHub username (or 'exit' to quit): ").strip()

        if username.lower() == "exit":
            print("\n👋 Program closed. Keep coding!")
            break

        if not username:
            print("⚠️ Username cannot be empty.")
            continue

        profile = get_github_user(username)

        if profile:
            display_profile(profile)

            print("\n📊 Quick Analysis")

            repositories = profile.get("public_repos", 0)
            followers = profile.get("followers", 0)

            if repositories >= 50:
                repo_level = "🔥 Highly Active Developer"
            elif repositories >= 20:
                repo_level = "🚀 Active Developer"
            elif repositories >= 5:
                repo_level = "💻 Growing Developer"
            else:
                repo_level = "🌱 Beginner / Early Stage"

            if followers >= 100:
                community_level = "🌟 Strong Community Presence"
            elif followers >= 25:
                community_level = "👍 Good Community Presence"
            else:
                community_level = "📈 Community Still Growing"

            print(f"Developer Level  : {repo_level}")
            print(f"Community        : {community_level}")

            print("\n" + "-" * 60)
            print("Would you like to analyze another profile?")
            print("-" * 60)


if __name__ == "__main__":
    main()