from google.oauth2 import service_account
from google.cloud import storage

credential_data = service_account.Credentials.from_service_account_file('C:/Users/nagasudhindra.g/Desktop/python/json/mtech-daas-testdata-cbc529459fa8.json')
projects = 'mtech-daas-testdata'
# Instantiates a client
storage_client = storage.Client(credentials=credential_data,project=projects)

buckets = storage_client.list_buckets()
for bucket in buckets:
    print(bucket.name)