# Disinformation Narratives Project

## Project Overview

The Disinformation Narratives project aims to identify and analyze disinformation narratives across various media platforms. By leveraging machine learning and natural language processing techniques, this project seeks to uncover patterns and provide insights into the spread of false information.

## Repository Structure
```
.
├── Disinformation narratives storytelling (banking)- Reviewed.docx
├── docker-compose.yaml
├── etl/
│   ├── .DS_Store
│   ├── app/
│   │   ├── Dockerfile
│   │   ├── etl.py
│   │   └── requirements.txt
│   └── data/
│       ├── x-clustering-cluster_metadata.csv
│       ├── x-clustering.csv
│       ├── x-raw.csv
│       ├── x-related-factchecks.csv
│       ├── x-toxicity_attacks.csv
├── README.md
````

## Installation

To install this project from GitHub, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/alexgutierr/TrueFlag.git
    ```

2. Navigate to the project directory:
    ```sh
    cd TrueFlag
    ```

## Deployment with Docker

To deploy the project using Docker, follow these steps:

1. Start the services using Docker Compose:
    ```sh
    docker compose up -d
    ```

2. The services will be started in detached mode. You can check the status of the services using:
    ```sh
    docker-compose ps
    ```

## Accessing the Services

### PostgreSQL

- Host: `localhost`
- Port: `5432`
- Database: `analytics`
- User: `etl_user`
- Password: `etl_password`

You can use any PostgreSQL client to connect to the database. For example, using `psql`:
```sh
psql -h localhost -p 5432 -U etl_user -d analytics
```

### Metabase

Metabase is available at http://localhost:3000.


- **Web Interface**: Access the web interface at `http://localhost:8000`
- **API Endpoints**: Use the API endpoints to interact with the project programmatically. Documentation for the API endpoints can be found in the `docs` directory.


### pgAdmin

pgAdmin is available at http://localhost:5050.

- Login credentials:
-- Email: admin@admin.com
-- Password: admin

### ETL Process

The ETL process is defined in the etl.py script. It performs the following steps:

Loads environment variables for database connection.
Connects to the PostgreSQL database.
Lists CSV files in the /data directory.
Load the content of the CSV files into the databse creating the tables if they don't exist.


To run the ETL process manually, you can use the following command:
```sh
docker-compose run etl
```sh
