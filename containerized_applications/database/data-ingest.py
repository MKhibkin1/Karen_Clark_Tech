import os
import traceback
import psycopg2
from datetime import datetime

def formatLine(line):
    formatted = line.rstrip()
    formatted = filter(None, formatted.split(','))
    formatted = [chars.strip() for chars in formatted]
    return(formatted)



def addStorm(line):
    #Split line and return empty elements and whitespace 
    headerData = formatLine(line)

    #parse header line based on the hurdat documentation
    try:
        basin = headerData[0][0:2]
        atcfNumber = int(headerData[0][2:4])
        year = int(headerData[0][4:8])
        name = headerData[1]

        stormIDQuery = "INSERT INTO stormidentification (basin, atcfcyclonenumber, year, name) VALUES (%s,%s,%s, %s) RETURNING id;"
        cursor.execute(stormIDQuery, (basin, atcfNumber, year, name))
        stormID = cursor.fetchone()[0]

        stormRecordsLength = int(headerData[2])

        #return the number of lines to iterate over in the file reading line and also the header Data
        return(stormID, stormRecordsLength)
    except:
        traceback.print_exc()

def addRecords(stormID, stormRecords):

    for stormRecordLine in stormRecords:

        #Loop through contents of array 
        stormRecord = formatLine(stormRecordLine)

        #dateTimepos
        date = stormRecord[0]
        time = stormRecord[1]

        dtString = date + time
        dt = datetime.strptime(dtString, '%Y%m%d%H%M')

        #General Identifiers
        recordIdentifier = stormRecord[2]
        stormStatus = stormRecord[3]

        #GeoSpatial
        [lat, hemiLat] = stormRecord[4][0:-1], stormRecord[4][-1:] 
        [lng, hemiLng] = stormRecord[5][0:-1], stormRecord[5][-1:] 
        quadrant = hemiLat + hemiLng

        lat = float(lat)
        lng = float(lng)


        if hemiLng == "W":
            lng = lng * -1
        if hemiLat == "S":
            lat = lat * -1

        #General Measurments
        maxWind = stormRecord[6]
        minPressure = stormRecord[7]
        maxWindRadius = stormRecord[20]
        

        #Input the storm Record into the database
        stormRecordQuery = """INSERT INTO stormreading 
        (stormID,
        recordTime,
        recordID,
        status,
        lat,
        lng,
        overallquadrant,
        maxsustainedwind,
        maxwindradius,
        minimumpressure
        ) 
        VALUES (%s, %s,%s,%s, %s, %s,%s,%s, %s, %s) RETURNING id;"""

        cursor.execute(stormRecordQuery, 
            (stormID,
            dt,
            recordIdentifier,
            stormStatus, 
            lat, 
            lng, 
            quadrant, 
            maxWind, 
            minPressure,
            maxWindRadius))

        #In the future we can also parse the records
        # stormWindRecords = stormRecord[8:]
        # addStormWindReadings(stormWindRecords)

# To be potentially implement later if more details desired
# def addStormWindReadings(stormWindRecords):
#     pass

#This function can be improved up by creating a generate function to have multi threaded ingest of data based on header line
def ingestData():

    data = open('./HURDAT2-data.txt')
    line = data.readline()
    while line:
        #Reader header line and create storm in database
        [stormID, stormRecordsLength] = addStorm(line)

        #Based on header line read storm record data and put into database
        stormRecords = (data.readline() for i in range(stormRecordsLength))
        addRecords(stormID, stormRecords)
        cnx.commit()

        #go on to next group 
        line = data.readline()

    data.close()

if __name__ == "__main__":

    USER = os.getenv('POSTGRES_USER')
    PASSWORD = os.environ.get('POSTGRES_USER_PW')

    try:
        cnx = psycopg2.connect(
            host = "localhost",
            dbname = "karen_clark",
            user = USER,
            password = PASSWORD,
            port= 5432
        )

    except: 
        traceback.print_exc()

    cursor = cnx.cursor()

    ingestData()


