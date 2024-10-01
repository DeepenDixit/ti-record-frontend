# Project Title

## Description

This frontend project is designed to filter and process records from JSON file. To filter records from SQL or Mongo, we just ned to change endpoint in `.env` file.

## Features

- Uses react where needed
- Uses MUI where needed
- Has login page and also capability to configure default password
- Capable to logout
- Interact with backend project/api to get records
- Shows loader on form submission
- Shows record in JQuery datatable which alloows to sort on any coulmn
- Has download button as well, to get flat CSV
- Logging and error handling
- Python codebase is fully secured and well writen and readable
- Python codebase uses well known pre-commit hooks to achieve security in code

## Setup

### Prerequisites

- Python
- React and other ackages
- webpack, to build js
- MongoDB (Optional)
- MySQL (Optional)

### Installation

1. Clone the repository:
2. Create a virtual environment and activate it:
3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    pip install -r dev-requirements.txt
    npm install
    npx webpack --config webpack.config.js
    ```

4. Set up environment variables:

    Create a `.env` file referring `.env.sample` file

### Commands

1. Once you confirm that your host is abe to make connection to backend API, start the flask app.

    ```sh
    python main.py
    ```