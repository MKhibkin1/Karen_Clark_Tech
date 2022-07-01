
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


