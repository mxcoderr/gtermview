import sys
import requests
import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()
GITHUB_API_URL = "https://api.github.com/users/"

def fetch_github_profile(username):
    url = f"{GITHUB_API_URL}{username}"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        return None

def show_profile(profile):
    table = Table(title=f"GitHub Profile: {profile['login']} (ID: {profile.get('id')})")

    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    table.add_row("Name", profile.get("name", "—"))
    table.add_row("Bio", profile.get("bio") or "—")
    table.add_row("Public Repos", str(profile.get("public_repos", 0)))
    table.add_row("Followers", str(profile.get("followers", 0)))
    table.add_row("Following", str(profile.get("following", 0)))
    table.add_row("Location", profile.get("location") or "—")
    table.add_row("Blog", profile.get("blog") or "—")

    console.clear()
    console.print(Panel(table, title="GitHub TUI Viewer", subtitle="Press Ctrl+C to exit"))

def save_profile_json(username, data):
    filename = f"{username}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"JSON file saved as {filename}!")

def main(ghusername=None):
    if not ghusername:
        ghusername = input("Enter GitHub username: ")

    profile = fetch_github_profile(ghusername)
    if profile:
        show_profile(profile)
    else:
        console.print(f"[red]Error:[/red] User '{ghusername}' not found")

if __name__ == "__main__":
    username = None
    save_json = False

    if len(sys.argv) > 1:
        username = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "--json":
        save_json = True

    if username:
        profile = fetch_github_profile(username)
        if profile:
            show_profile(profile)
            if save_json:
                save_profile_json(username, profile)
        else:
            console.print(f"[red]Error:[/red] User '{username}' not found")
    else:
        main()

