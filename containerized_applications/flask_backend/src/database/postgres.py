import os
import psycopg2
import traceback


class HurricaneDatabase:

    def __init__(self):

        self.connectToDatabase()

    def connectToDatabase(self):
        USER = os.getenv('POSTGRES_USER')
        PASSWORD = os.environ.get('POSTGRES_USER_PW')

        try:
            self.cnx = psycopg2.connect(
                host = "localhost",
                dbname = "karen_clark",
                user = USER,
                password = PASSWORD,
                port= 5432
            )
            self.cursor = self.cnx.cursor()

        except: 
            traceback.print_exc()

    def getLandfallRecords(self):
        landfallQuery = """select distinct on(stormID.id) stormID.id, stormRecord.recordTime, stormID.name, stormRecord.maxSustainedWind, stormRecord.lat, stormRecord.lng
            from stormidentification stormID
            left join stormreading stormRecord 
            on stormRecord.stormid = stormID.id
            where date_part('year', stormRecord.recordTime) >= 1900
            and stormrecord.recordId ='L';
            """

        self.cursor.execute(landfallQuery)
        return(self.cursor.fetchall())
        
