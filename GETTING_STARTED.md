# GETTING STARTED

## Requirements

The following are required to be installed on the system to use this project.

- Python 2.7

  - Developed in [Python 2.7.1](https://www.python.org/download/releases/2.7/)

- PIP (Python 2.7)

- [Virtualenv](https://virtualenv.pypa.io/) **or** [VirtualenvWrapper](https://virtualenvwrapper.readthedocs.io/)

  - Allows multiple python environments on the same machine without conflict

- [NPM 6.4.1](https://www.npmjs.com/get-npm)

## Installing Requirements

### Python 2.7

- Macs with [Homebrew](https://brew.sh/): `brew install python`
- Ubuntu: `sudo apt-get install python`

### PIP (Python 2.7)

- Macs with Homebrew: `brew install python-pip`
- Ubuntu: `sudo apt-get install python-pip`


### Virtualenv or VirtualenvWrapper

- Follow instructions instructions from links above for specific OS installations

## Setup Environment

1. Download and install all requirements

2. Create a new virtual environment for this project

  - For virtualenv: `virtualenv {env_path} -p $(which python)`
  - For virtualenvwrapper: `mkvirtualenv {env_name} -p $(which python)`

3. Activate the created virtual environment

  - For virtualenv: `source {env_path}/bin/activate`
  - For virtualenvwrapper: `workon {env_name}`

4. Check to see if environment is setup
  - Check to see if virtualenv is active: `which python`
  - Check Python version: `python --version`

5. Install package requirements for project
  - `pip install -r requirements.txt`
  - `npm install`
