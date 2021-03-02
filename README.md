# geo-api
The aim of this task is to build an API (backed by any kind of database) that requires JWT authorization. The application should be able to store geolocation data in the database, based on IP address or URL - you can use https://ipstack.com/ to get geolocation data (you can obtain free API KEY here -> https://ipstack.com/signup/free). The API should be able to add, delete or provide geolocation data on the base of ip address or URL. 

## How to test
- You can see the API under this [url](https://assignment-geo-api.herokuapp.com/api/). The BrowsableAPI and debug is enabled.
  - to login use [url](https://assignment-geo-api.herokuapp.com/api/token/)
  - to get geolocation data use [url](https://assignment-geo-api.herokuapp.com/api/geolocation/) with param `ip_or_url` for example https://assignment-geo-api.herokuapp.com/api/geolocation/?ip_or_url=wp.pl
- The solution also provides [test client](simple_request.py) which will connect to heroku based app and test it with different cases:
  - without authentication
  - authenticated as admin user
  - authenticated as normal user
  
- For local testing please invoke `docker-compose up` command and the environment will be up. After that please create 2 users:
- admin with 'docker-compose run web python manage.py createsuperuser' with admin:admin details
- normal user with admin interface with following credentials user:useruser
   
