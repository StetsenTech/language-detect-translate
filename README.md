# Language Detect and Translate

Language Detect and Translate is a sample full stack project that takes user
input and detects what language it is and sends to the Google Cloud Translation
API to get translated.

## Documentation

- [Getting Started](GETTING_STARTED.md) - Walks through setting up this project

## Running Project

- Be sure to follow all instructions in [Getting Started](GETTING_STARTED.md) readme.
- In the route directory of the project, run the following commands
  - `invoke db.migrate` - Creates and/or run migrations on database
  - `invoke app.run` - Starts the application
    - Note: Currently runs on port 5000

## Plans

- [ ] Refactor routes to use Flask-ClassFul
- [ ] Set up Notebooks with examples
- [ ] Add tests using PyTest