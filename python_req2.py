import logging
import os
import cloudstorage as gcs
import webapp2

from google.appengine.api import app_identity

def get(self):
  bucket_name = os.environ.get('BUCKET_NAME',
                               app_identity.get_default_gcs_bucket_name())

  self.response.headers['Content-Type'] = 'text/plain'
  self.response.write('Demo GCS Application running from Version: '
                      + os.environ['CURRENT_VERSION_ID'] + '\n')
  self.response.write('Using bucket name: ' + bucket_name + '\n\n')

  def read_file(self, filename):
    self.response.write('Reading the full file contents:\n')

  gcs_file = gcs.open(filename)
  contents = gcs_file.read()
  gcs_file.close()
  self.response.write(contents)

  def list_bucket(self, bucket):

  """Create several files and paginate through them.

  Production apps should set page_size to a practical value.

  Args:
    bucket: bucket.
  """

  self.response.write('Listbucket result:\n')

  page_size = 1
  stats = gcs.listbucket(bucket + '/foo', max_keys=page_size)
  while True:
    count = 0
    for stat in stats:
      count += 1
      self.response.write(repr(stat))
      self.response.write('\n')

    if count != page_size or count == 0:
      break
    stats = gcs.listbucket(bucket + '/foo', max_keys=page_size,
                           marker=stat.filename)
                           