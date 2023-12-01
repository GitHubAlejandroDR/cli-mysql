<img src="image_readme.jpg" alt="Alt Text" style="width:100%; height:200px;">

# MySQL | Python | Command Line Interface

## Table of Contents

- [Project Description](#project-description)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [How to use](#how-to-use)


# Project Description

Python-based CLI for interacting with a local MySQL database.

This project is an adaptation of a Biological Databases course final project. Additionaly of the queries implemented for the database interaction through the CLI aplication, there are an extended queries SQL document (add link). 

# Project Structure

- **`/cli`**: Main Python file and predefined queries/ for the database connection and text based command line interface

  - **`/queries`**: Python module with SQL queries for interacting with the database

- **`/database`**: MySQL files, data, and entity relation schema

  - **`/MySQL_Workbench`**: MySQL Workbench files to reproduce the database
  - **`/data`**: Table data used

- **`/docs`**: Project report and extended SQL queries document 

# Technologies

| **Component**           | **Technology** |
|-------------------------|----------------|
| Programming Language    | Python         |
| Database                | MySQL          |
| Dependencies Management | Poetry         |

# Getting Started

## Prerequisites

Before you begin working with this project, make sure you have the following prerequisites installed on your system:

- [MySQL](https://dev.mysql.com/downloads/installer/): MySQL is used as data storage and data base management system. You can install MySQL by following the [MySQL website](https://dev.mysql.com/downloads/installer/).

- [Python](https://www.python.org/downloads/): This project is developed in Python, and you'll need Python 3.6 or higher. You can download Python from the official [Python website](https://www.python.org/downloads/).

- [Poetry](https://python-poetry.org/): Poetry is used for managing project dependencies and packaging. You can install Poetry by following the [official installation instructions](https://python-poetry.org/docs/#installation).

Once you've installed all the prerequisites, you can proceed with setting up and working with this project.

## Installation

## How to Use

To get the project up and running, follow these installation steps:

1. **Clone the project repository**:

   ```shell
   git clone https://github.com/GitHubAlejandroDR/cli-mysql.git

2. Change Directory:

   ```shell
   cd cli-mysql

3. Install Dependencies:

Ensure you have Poetry installed. If not, install it following the official instructions.

Install the project's dependencies using Poetry. It will read the pyproject.toml file to manage the dependencies:

```shell
   poetry install
```

4. Activate Virtual Environment:

```shell
  poetry shell
```

 5. Load the MySQL model Workbench
    
The MySQL is stored in `/database/MySQL_Workbench`

 7. Import the data

Each table has associated a .csv or .json file. Match the name of the file with the name of the table in the data base. 

The data is stored in `/database/data`

 8. Insert your database parameters

```python
  connection = mysql.connector.connect(
    host="",
    user="",
    password="",
    database="",
)
```

 8. Execute `main.py` and interact with the database.
