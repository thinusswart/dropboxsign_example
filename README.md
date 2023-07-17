# Creating PDF files with Dropbox Sign

This is a simple example repo with a few code snippets you can use to create signable PDF files with [Dropbox Sign](https://www.dropbox.com/hellosign).

# Getting up and running

1. Clone the project from Github
2. Create a virtual environment using `python3 -m venv .venv`
3. Activate the virtual environment: `source .venv/bin/activate`
4. Install the required modules: `pip install -r requirements.txt`
5. Sign up for a [Dropbox plan](https://www.dropbox.com/one/try) that supports API access
6. Copy `config.defaults` to `config.py`
7. Fill in the values in `config.py`
8. Run `main.py`

Your Linux or Windows environment may be different from mine, so anything from Python variables, system paths, environment variables and/or the availability of `pip` might differ.

YMMV.

This is merely an example project for myself and others to play with, not a product that needs to install perfectly every time.
