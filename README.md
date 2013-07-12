# BufferOverflow: The Educational SO Clone

This is repo contains all code shown during the **Introduction to Django** session on **FISL14**.

To run it in development you must run:

    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py runserver

## Login with Google

In order to enable login with Google you need to get a **Client ID** and **Client SECRET** from them.

Go to https://code.google.com/apis/console/ and create a project. On that project, click on 'API Access' and create an OAuth 2 Client ID. Choose 'Web application' as the type, click 'more options' and enter http://localhost:8000/complete/google-oauth2/ as the redirect URI.

This URI works when running the local server but you need to enter the real domain of your site once you deploy to production.