from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
from pyfiglet import Figlet
from termcolor import colored
from colored import fg, bg, attr

# Display banner
f = Figlet(font='slant')
print(f.renderText('Spotify Songs'))

# Load environment variables
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Function to get Spotify API token
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

# Function to get authorization header
def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

# Function to search for an artist
def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print(f"{fg(1)}No artist with this name exists :(")
        print("------------------------")
        print("")
        return None
    return json_result[0]

# Function to get songs by artist
def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

# Main execution loop
def main():
    token = get_token()
    while True:
        print(f"{fg(148)}Options:")
        print(f"1. Enter Artist Name")
        print(f"2. Exit")
        choice = input(f"Enter your choice (1 or 2): ")
        print("")

        if choice == '1':
            artist_name = input(f"{fg(148)}Enter Artist Name: ")
            print("")
            result = search_for_artist(token, artist_name)
            if result:
                artist_id = result["id"]
                songs = get_songs_by_artist(token, artist_id)
                for idx, song in enumerate(songs):
                    print(f"{fg(14)}{idx + 1}. {song['name']}")
                    print("")
            else:
                print(f"{fg(1)}No artist found. Please try again.")
                print("")
        elif choice == '2':
            print(f"{fg(2)}Exiting the program. Goodbye!")
            print("")
            break
        else:
            print(f"{fg(130)}Invalid choice. Please enter 1 or 2.")
            print("")


if __name__ == "__main__":
    main()
