
# Person Registration API - Documentation

## About the Project 🌐

The **Person Registration API** is an API built with **Django**, designed to register personal information and manage data related to individuals' careers. The API is accessed via a **RESTful** interface and can be used to register, update, query, and delete personal information of users. 🚀

This repository also includes complementary features, such as a **script for modifying the hosts file** 🖥️ (useful for local redirects during development) and an **example of Dockerization** 🐳 to make the development and execution of the API more isolated and portable.

---

## Key Features 🔑

### 1. **Person Registration API** 📝

- Allows for the registration and management of personal and career information.
- API built with **Django**, accessed through a **RESTful** interface.

### 2. **Hosts File Modification** 🗂️

- A Python script to add or remove entries in the system's **hosts** file.
- Essential for configuring local redirects during development.

### 3. **Dockerization Example** 🐳

- Includes a **Docker** example to run the API in an isolated container, simplifying the development environment.

### 4. **Automated Tests** 🧪

- The API includes automated tests to ensure that the application's features work correctly.
- Tests are executed using the **pytest** testing framework.

## Prerequisites 🔧

Before starting, make sure you have the following dependencies installed on your system:

- Python 3.6 or higher 🐍
- Docker and Docker Compose installed 🐋
- Git (if you wish to clone the repository) 📂
- Administrator/root permissions (necessary to modify the hosts file) 🔑

## Installation and Running the Project 🚀

### 1. Cloning the Repository 📥
Clone the repository to your working directory:

```bash
git clone https://github.com/Rennanbarao0/codelap
```
```bash
cd codelap
```

### 2. Installing Dependencies 📦
The project's dependencies are listed in the `requirements.txt` file. To install them, run:

```bash
pip install -r requirements.txt
```

The main dependencies include:

- **Django**: Web framework to build the API.
- **Django REST framework**: Library to create the RESTful API.

### 3. Database Configuration 🗄️
The API uses the default Django database. To configure and run the migrations, run:

```bash
python manage.py migrate
```

If you're using an external database, change the database settings in the `settings.py` file.

## Running the Project with Docker 🐳

### 1. Building the Docker Image 🏗️

In the project directory, run the command to build the Docker image:

```bash
docker-compose build
```

### 2. Starting the Container ⚙️
To start the container, run:

```bash
docker-compose up
```

### 3. Stopping the Containers 🛑
To stop the container, run:

```bash
docker-compose down
```

## Dockerfile 🐋
The Dockerfile is configured to run the API using Python 3.11. It installs the dependencies from `requirements.txt`, copies the project code, and runs the Django server.

## How to Run the Hosts File Modification Script 🖥️

The `script.py` allows for redirecting custom domains to a local IP, useful during development. This script modifies the hosts file on your system.

### How to Run the Script 🎯

#### Prerequisites:
- Python 3.6 or higher installed 🐍
- Administrator/root permissions to modify the hosts file 🔑

#### Execution:
1. Save the `script.py` in the project directory.
2. Run the script in the terminal:

```bash
python script.py
```

The script will prompt you to choose the desired action:

- **add**: Adds an entry to the hosts file.
- **remove**: Removes an existing entry.

### Example Usage 💻:
The script is already configured to add the domain `dev.codeleap.co.uk` redirected to the IP `127.0.0.1`.

- For **Windows**, run as administrator.
- For **Linux/Mac**, use `sudo`:

```bash
sudo python script.py
```

This will allow you to easily redirect the domain to the local IP during development.

## Automated Tests 🔬
The API includes automated tests to ensure that the application's features work correctly.

### Running the Tests 🏃

Use pytest to run the tests, execute:

```bash
pytest
```

The tests cover the main flows of the API, including creation, reading, updating, and deleting records. It is a practical way to ensure the API is working as expected after any modification.

---

### API Endpoints 🌍

Once the application is running, you can access the API locally by navigating to:

[https://dev.codeleap.co.uk/](https://dev.codeleap.co.uk/)  
Make sure to have your local hosts file updated to resolve the custom domain to `127.0.0.1` or the appropriate IP of the Django container.

**API Endpoints**:

- **POST /careers**: Register a new person with their career information.
- **GET /careers**: Retrieve a list of all registered people.
- **GET /careers/{id}**: Retrieve a person's details by their ID.
- **DELETE /careers/{id}**: Delete a person by their ID.

Alternatively, you can access the same endpoints using the local IP:

[https://127.0.0.1:8000/careers](https://127.0.0.1:8000/careers)
