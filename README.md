# CricketApplication
Cricketmain app contains the logic of creating REST APIs in order to expose the teams in this application and players in each team.

Frontend app consumes RESTAPIs and renders the details in HTML templates

testing folder contains unit testcases to test REST APIs

Database used: PostgreSQL

In order to load the static data in the database, use the following command to run the script
python manage.py release_script

python manage.py runserver runs the application on local server

http://localhost:8000/ will load the application.

To run unit testcases:
1) start the development server
2) go to testing folder and run python test_unitcases.py command.
