# Performance repository

This repository contains the base code used for load testing for Apps components. 

# Developer Notes for setting up your environment

### Python

Install https://www.python.org/downloads/

### Locust 

1. When `Python` is installed, use pip3 to install `Locust`.
`
pip3 install locust
`

2. Now check that the package was installed.
`
locust -V
`

Check the official documentation for more information: https://docs.locust.io/en/stable/index.html

### Python-dotenv 
1. Also using pip3, install `Python-dotenv`.This project allow us to read the .env file to access the environment variables needed.
`
pip3 install python-dotenv
`

# Run Locust
1. In the root folder, open a terminal and run the following command:
`
locust --config locust.conf 
`
That should run the load tests headless. To execute it with a web interface, go to the `locust.conf` file and set the `headless` flag as false.
