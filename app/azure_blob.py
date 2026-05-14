from azure.storage.blob import BlobServiceClient
import os


AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME", "files")


def get_blob_client():
    if not AZURE_CONNECTION_STRING:
        raise ValueError("AZURE_STORAGE_CONNECTION_STRING is not set")

    service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
    container_client = service_client.get_container_client(CONTAINER_NAME)

    # Create container if it doesn't exist
    try:
        container_client.create_container()
    except Exception:
        pass

    return container_client


def upload_file_to_blob(container_client, file, filename):
    blob_client = container_client.get_blob_client(filename)
    blob_client.upload_blob(file, overwrite=True)
    return blob_client.url


def delete_file_from_blob(container_client, filename):
    blob_client = container_client.get_blob_client(filename)
    blob_client.delete_blob()
