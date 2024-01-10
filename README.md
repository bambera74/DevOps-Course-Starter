# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Installing the app using Ansible

Copy the ansible playbook and inventory files from the ansible_setup folder to a suitable location on your control host. Edit the inventory file on your control host to reflect your own inventory.

Copy the .env.j2 template file from the ansible_setup folder on your local machine to the control node using the command below:

Navigate to the folder containing the .env.j2 file in a terminal then run;
>scp .env.j2 ec2-user@{host_ip_address}:/home/ec2-user/my-templates/.env.j2

IMPORTANT NOTE: Ansible playbook currently references Module4 for the git checkout

## Testing to todo application

Add pytest as a dependency of our project by running `poetry add pytest`. This should download pytest and also update pyproject.toml for you.

test_view_model.py 
==================
has been provided to test that the ViewModel class is functioning correctly.
A sample set of data has been provided in test_view_model.py which can be extended to cover other use cases.
To execute the test simply run `poetry run pytest` from the terminal.

test_integration.py
===================
has been provided to test the integration between app.py and trello_items.py. It uses monkeypatch to patch the call the the Trello API and test that the rest of the todo app is processing card correctly.
To eexecute the test simply run pytest from the terminal. Any changes made to the request function in trello_items.py would need to be reflected in this test file too.

## Running the app in a docker container

Ensure that your .env file is in the same root folder as the Dockerfile and contains the relevant information for your instance of Trello, API key, token and board / list IDs.

## To build to docker container

Run the following commands from a machine with docker installed.

To build a prod container run the command below from the same location as the dockerfile :

docker build --target production --tag todoapp:prod .

To build a dev container run the command below from the same location as the dockerfile :

docker build --target development --tag todoapp:dev .

## To run the container

Run the following command from a machine with docker installed. 

The command must be run from the same location as the Dockerfile:

DEV : 'docker run --publish 5001:5000 --env-file .env todoapp:dev'

PROD : 'docker run --publish 5002:8000 --env-file .env todoapp:prod'

Note: add the -d flag to run in detached mode

For Dev you can then browse the site using 'http://{hostname_url or localhost}:5001'

For Prod you can then browse the site using 'http://{hostname_url or localhost}:5002'

## To run a development container with a bind mount

You may want to take advantage of the way that flask allows for dynamic reloads in your development container. To do this, you can mount the files on your local machine into the container using the bind mount command:

$ docker run --env-file ./.env -p 5001:500 --mount "type=bind,source=$(pwd)/todo_app,target=/opt/todo_app" todoapp:dev

## To exit the container running

First run the 'docker container list' command to identify the unique name of your running container.

Then use the docker stop command to stop your container. i.e. 'docker stop admiring_newton'

