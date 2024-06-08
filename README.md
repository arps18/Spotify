# Spotify Top Artist Songs

![image](https://github.com/arps18/Spotify/assets/47818179/f1fdd2b5-662c-4906-91ee-1c789033343b)

# Spotify Artist Search

This project is a Python-based terminal application that allows you to search for an artist on Spotify and retrieve their top tracks. The application uses the Spotify Web API to fetch data and requires authentication via a client ID and client secret.

## Features

- Display a banner using ASCII art
- Prompt the user to enter an artist name
- Authenticate with the Spotify API using client credentials
- Search for an artist on Spotify
- Retrieve and display the top tracks for the artist

## Prerequisites

- Python 3.6 or higher
- Spotify Developer Account

## Setup Instructions

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/spotify-artist-search.git
   cd spotify-artist-search
   ```

2. **Create and Activate a Virtual Environment:**

   On macOS and Linux:

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:

   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Required Libraries:**

   ```txt
   python-dotenv
   requests
   pyfiglet
   termcolor
   colored
   ```

4. **Set Up Environment Variables:**

   Create a `.env` file in the project directory and add your Spotify API credentials:

   ```env
   CLIENT_ID=your_spotify_client_id
   CLIENT_SECRET=your_spotify_client_secret
   ```

   Replace `your_spotify_client_id` and `your_spotify_client_secret` with your actual Spotify API credentials.

5. **Run the Application:**

   ```sh
   python main.py
   ```

## Notes

- Ensure you have a Spotify Developer Account and have created an application to get your `CLIENT_ID` and `CLIENT_SECRET`.
- The script uses `dotenv` to manage environment variables, making it easier to keep sensitive information secure.


