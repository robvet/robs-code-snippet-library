# Start with dependency management and basic setup
import os
from dotenv import load_dotenv, dotenv_values
import requests
from azure.storage.blob import BlobServiceClient

# Load environment variables from the .env file
dotenv_path = 'secrets/credentials.env'
load_dotenv(dotenv_path=dotenv_path, override=True)

# Print the contents of the .env file for debugging
# env_vars = dotenv_values(dotenv_path)
# print("Contents of the .env file:")
# for key, value in env_vars.items():
#     print(f"{key}: {value}")

# Access the secrets directly from env_vars
connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = os.getenv('AZURE_STORAGE_CONTAINER_NAME')

# Print the environment variables for debugging
# print(f"Connection String: {connection_string}")
# print(f"Container Name: {container_name}")

# Validate the environment variables
if not connection_string:
    raise ValueError("AZURE_STORAGE_CONNECTION_STRING is not set or is empty.")
if not container_name:
    raise ValueError("AZURE_CONTAINER_NAME is not set or is empty.")
print('done')