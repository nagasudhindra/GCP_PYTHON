from google.auth.transport.requests import AuthorizedSession
from google.cloud import storage
from google.oauth2 import service_account

credential_data = service_account.Credentials.from_service_account_file('C:/Users/nagasudhindra.g/Desktop/python/json/mtech-daas-testdata-cbc529459fa8.json')
projects = 'mtech-daas-testdata'

##def upload_blob(bucket_name, source_file_name, destination_blob_name):
#    """Uploads a file to the bucket."""
bucket_name = "us-central1-mtech-daas-test-f2847bfc-bucket"
source_file_name = "C:/Users/nagasudhindra.g/Desktop/Desktop BKP/NSR BQ Code change/nsr/bq_sql/gtt_nr_date_insert.sql"
destination_blob_name = "gtt_nr_date_insert.sql"

storage_client = storage.Client(credentials=credential_data,project=projects)
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(destination_blob_name)

blob.upload_from_filename(source_file_name)

print(
    "File {} uploaded to {}.".format(
    source_file_name, destination_blob_name
    )
)
