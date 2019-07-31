# ProjectCynthia
A bot that can play on Pokémon Showdown

Developed with Python 3.7.3

## Setup/installation

Clone the repository with: `https://github.com/4711KingOfHearts/ProjectCynthia.git`

Setup the project as a new Python 3 virtual environment: `python3 -m venv ProjectCynthia`

Activate the newly created virtual environment: `cd ProjectCynthia; source bin/activate`

Install the required Python3 packages with: `pip install -r requirements.txt`.

## Configuration

ProjectCynthia uses the `environs` package to read its configuration from the `.env` file. At the very least, you will want to set the login credentials for your bot:
```
SD_USERNAME="username"
SD_PASSWORD="password
```
