# Google Play Developer Publishing API samples

A collection of command-line samples for the Play Developer Publishing API.

## Installation

1. Download Google APIs Client Library for Python (google-api-python-client):
  https://code.google.com/p/google-api-python-client/

  or use pip:

  ```bash
  $ pip install google-api-python-client
  ```

2. Make sure you can import the client library:

  ```bash
  $ python
  >>> import apiclient
  >>>
  ```

## First request using OAuth2: Installed application

1. Edit the `client_secrets.json` file and add the client ID and client secret.

2. Execute any of the scripts to begin the auth flow:

  ```bash
  $ python basic_list_apks.py com.myapp.package
  ```

  A browser window will open and ask you to login. Make sure the account has
  enough permissions in the Google Play Developer console.

3. Accept the permissions dialog. The browser should display

  `The authentication flow has completed.`

  Close the window and go back to the shell.

4. The script will output a list of apks.

5. The tokens will be stored in `androidpublisher.dat`. Remove this file to restart the
 auth flow.


## First request using OAuth2: Service accounts

1. Edit `basic_list_apks_service_account.py` and add the service account Email
address.

2. Copy the service account key file, generated in the Google APIs Console into
the same directory and rename it to `key.p12`.

3. Execute the script:

  ```bash
  $ python basic_list_apks_service_account.py com.myapp.package
  ```

4. The script will output a list of apks.

