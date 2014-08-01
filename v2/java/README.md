# Google Play Developer API samples

A collection of Java samples for the Play Developer API.

## Installation

1. Download the Google Play Developer API client library:
https://developers.google.com/android-publisher/libraries

2. Unzip the client library. The unzipped folder contains the
google-api-services-androidpublisher-v2.jar client library and a lib/ folder with all required
dependencies.

3. Import the Java sample code into your favorite IDE and reference all libraries in the /lib folder
as well as the google-api-services-androidpublisher-v2.jar from the sample project.

## Getting started
To use the Google Play Developer API you need to create or reuse an existing API project in the
Google Api console, https://console.developers.google.com/. You can either use the API with a client
ID for Native Application (Installed Application) or create a Service Account.

### Edit `ApplicationConfig.java` for global sample configuration

1. Specify the name of your application. If the application name is null or blank, the application
will log a warning. Suggested format is `MyCompany-Application/1.0`.

2. Specify the package name of the app as per developer console.

3. If you want to run any of the upload apk samples, please copy your apk to the `/resources` folder
and specify the apk file path, i.e. `/resources/your_apk.apk`

### First request using OAuth2: Installed application

1. Edit the `/resources/client_secrets.json` file and add the client ID, client secret and redirect
uris.

2. Execute any sample class using its `main()` method to begin the auth flow:

  A browser window will open and ask you to login. Make sure the account has
  appropriate permissions in the Google Play Developer console.

3. Accept the permissions dialog. The browser should display

  `The authentication flow has completed.`

  Close the window and go back into your IDE and check the console output.

4. The script will output a list of apks.

5. The tokens will be stored in `.store/android_publisher_api` in your home folder. Remove this file
to restart the auth flow.


### First request using OAuth2: Service accounts

1. Edit `ApplicationConfig.java` and add the service account email
address.

2. Copy the service account key file, generated in the Google APIs Console into
the same directory and rename it to `key.p12`.

3. Execute any sample class using its `main()` method in your IDE

4. The script will output a list of apks.


> You're all set and ready to run the Play Developer API samples.
Thank you for being such a great developer on Google Play, your feedback is very important to ensure
that Google continues to improve the developer experience on Play! Enjoy :-).
