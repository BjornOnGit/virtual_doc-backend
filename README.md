# virtual_doc-backend

## Description

This is a backend for a virtual doctor application. It is a RESTful API that allows users to create an account, login, and make appointments with doctors and receive diagnoses.

## Technologies

- Django
- Django Rest Framework

## Installation

Clone the repository using

```bash
git clone https://github.com/ece-505-grp-1/virtual_doc-backend.git
```

Create a virtual environment.

If you're on a linux machine, you can use the following commands:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

If you're on a windows machine, you can use the following commands:

```bash
python -m venv .venv
.venv\Scripts\activate
```

If you're on a mac, you can use the following commands:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the requirements using the following command:

```bash
    pip install -r requirements.txt
```

create a .env file in the root directory and add the following environment variables:

```bash
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
```

Replace your_secret_key with the actual secret key that can be provided on request from @BjornOnGit and your_database_url with the actual database url that can be provided on request from @BjornOnGit.

create a .gitignore file and add the following files:

``` bash
.venv/
.env
db.sqlite3
```

## Contribution

The project is open to contributions. To contribute, follow the steps below:

After installing the project, create a new branch for a feature of your choice using the following command:

```bash
git branch your_branch_name
git checkout your_branch_name
```

## Endpoints

To view the endpoints, please visit the API docs at [Virtual Doctor API docs](https://virtual-doc-api-7610edfd4b12.herokuapp.com/api/v1/docs/)

## Environment Variables

We introduced environment variables and a .env file to store them this early in order to ensure that the project is not broken by the introduction of new environment variables. This is to ensure that the project is always in a working state. Please let us know if you need to add any environment variables.

## Integrations

We are currently integrating the following services:

- Google Maps and Places API for both the laboratory and pharmacy locator
- OpenAI API Chatbot Platform for the virtual doctor chatbot

## Note

When contributing to the project, please ensure that you do not push any sensitive information to the repository. This includes the .env file and any other sensitive information.
Always create a pull request and wait for it to be reviewed before merging it to the main branch.
DO NOT PUSH DIRECTLY TO THE MAIN BRANCH.
