# OURA API Flask Server
A Flask server allowing for the retrieval of data from OURA API.

# Usage
1. Clone the repository
2. Create a new file called `.env` in the root folder of the repository, that must contain the following fields:
    - `CLIENT_ID`
    - `CLIENT_SECRET`
3. Run the app with `flask --app ouraflask run --debug`