#!/usr/bin/python
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Lists all the apks for a given app."""

import argparse

from apiclient.discovery import build
import httplib2
from oauth2client import client


SERVICE_ACCOUNT_EMAIL = (
    'ENTER_YOUR_SERVICE_ACCOUNT_EMAIL_HERE@developer.gserviceaccount.com')

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('package_name',
                       help='The package name. Example: com.android.sample')


def main():
  # Load the key in PKCS 12 format that you downloaded from the Google APIs
  # Console when you created your Service account.
  f = file('key.p12', 'rb')
  key = f.read()
  f.close()

  # Create an httplib2.Http object to handle our HTTP requests and authorize it
  # with the Credentials. Note that the first parameter, service_account_name,
  # is the Email address created for the Service account. It must be the email
  # address associated with the key that was created.
  credentials = client.SignedJwtAssertionCredentials(
      SERVICE_ACCOUNT_EMAIL,
      key,
      scope='https://www.googleapis.com/auth/androidpublisher')
  http = httplib2.Http()
  http = credentials.authorize(http)

  service = build('androidpublisher', 'v3', http=http)

  # Process flags and read their values.
  flags = argparser.parse_args()

  package_name = flags.package_name

  try:

    edit_request = service.edits().insert(body={}, packageName=package_name)
    result = edit_request.execute()
    edit_id = result['id']

    apks_result = service.edits().apks().list(
        editId=edit_id, packageName=package_name).execute()

    for apk in apks_result['apks']:
      print 'versionCode: %s, binary.sha1: %s' % (
          apk['versionCode'], apk['binary']['sha1'])

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')

if __name__ == '__main__':
  main()
