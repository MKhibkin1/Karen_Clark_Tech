
**Karen Clark Interview Question**


This is documentation for the karen Clark Interview Question. This read me includes 3 sections:
1. The original prompt of the questions.
2. Short notes detailing architecture of the solution.
3. Implementation notes and how to run and interface with solution

---
<br />

**Section 1: Original Prompt**
<br />

Use the NOAA Best Track Data (HURDAT2) to identify all hurricanes that have
made landfall in Florida since 1900.

Using a programming language of your choice, build an application to parse the HURDAT2 data, identify
the storms that made landfall in Florida, and output a report listing the name, date of landfall, and max
wind speed for each event.

You will find the HURDAT2 data set (5.9 MB file) and the HURDAT2 format specification on the NOAA
website.


Deliverables: 
Minumum: 
* Identify storms that made landfal in Florida. 
* Name of storm
* Date of landfall
* max wind speed for each event

Additional Features:
* Simple component front end that displays a US map by state
* On click of state will retrieve information requested in minimum

---
<br />

**Section 2: Architecture and Design Choices**
<br />

There are 4 components to solve the problem outlined. 
1. A postgresql database to store the data for HURDAT2
2. A short script to parse through the HURDAT2.txt file and ingest it into the database
3. A flask (python) backend to handle rest requests from the front end. 
4. A react front end to display a map of the usa and exectue fetch requests. An associated container will run express that serves this application


Design Choices: 
1. Parsing through the HURDAT2.txt file would suffice for this problem, however, it is not scalable and would not demonstrate applicants ability to anticipate growth.
2. This design choice is a consequence of design choice 1. It is actually the logic behind the original prompt. Once data is ingested it becomes trivial to parse through the existing data with a psql query
3. Flask was chosen because it has a simple boilerplate to be able to handle rest requests 
4. React was chosen because that is the requested language of the company. Express was chosen to host the application because of ease of integration. 

*Further Breakdown*
<br />
Postgresql Database: <br />
Database Name: karen_clark <br />
username: karen_clark_serviceworker01 <br />
password: Interview


Flask Backend:
Coordinate data for state boundaries was loaded through shp files for the US using the python libraries shapely and fiona. There is currently only one rest endpoint for the back end that involves passing in the state abreviation.

React Front End:
A third party component library was used to display a map in the browser.

---
<br />

**Section 3: Running and Interface**
<br />

In the future the following steps would be abstracted away in a docker container. 

Loading / interfacing with database: 
---
(Change directories to the database directory)
A tar file of the database dump is included in the database directory. There are two ways to restore the state of the database developed for this project

With PG utilities:
1. Tar file restore with 
pg_restore -d karen_clark karen_clark_DB.tar

Manually:
1. create a database karen_clark
2. Create a use with user name karen_clark_serviceworker01 and passowrd Interview
3. Run the sql scripts found database/sql_scripts/table_creation
4. Set environemnt variables:
    A. POSTGRES_USER=karen_clark_serviceworker01
    B. POSTGRES_USER_PW=Interview
5. Run data-ingest.py

Loading / interfacing with Backend:
---
(Change directories to the flask_backend directory)
1. Install the packages in requirements.txt
2. Make sure environemtn variables are set as they are in the database section
3. run main.py


Loading / interfacing with Frontend:
---
(Change directories to the react-front-end directory)
1. run yarn to install packages
2. run yarn start to start the server

to see the results go to:
http://localhost:3000

