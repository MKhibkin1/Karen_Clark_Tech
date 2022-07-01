from flask import Flask, request, jsonify
from flask_cors import CORS
from auxilary.GeoLocator import UnitedStates
from database.postgres import HurricaneDatabase
from datetime import datetime, date
import json

app = Flask(__name__)
CORS(app)

def JSONDateFormatter(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


@app.route("/")
def route():
    return("Use this Service to query hurricane data by state")
    pass


# Basic Fetch request from front end:
# http://localhost:9999/hurricane-data?state=FL&land-fall-date&name&max-wind-speed
@app.route("/hurricane-data")
def stormData():
    state = request.args.get("state", default = None, type = str)   
    args = request.args

    if state:
        stormList = []

        #Filter the records by state
        for record in landfallRecords:
            if(US[state].containsCoordinate(record[5], record[4])):
                stormList.append(record)


        returnData = {}
        storms = []
        for storm in stormList:
            newStorm = {}
            if "land-fall-date" in args:
                landFallDate = request.args.get("land-fall-date", default = None, type = str)
                if landFallDate: 
                    #Filter to be developed for landfalldate
                    pass

                newStorm["landFallDate"] = storm[1].isoformat()

            if "name" in args:
                name = request.args.get("land-fall-date", default = None, type = str)
                if name: 
                    #Filter to be developed for name
                    pass

                newStorm["name"] = storm[2]

            if "max-wind-speed" in args:
                maxWindSpeed = request.args.get("max-wind-speed", default = None, type = str)
                if maxWindSpeed: 
                    #Filter to be developed for date
                    pass
                
                newStorm["maxWindSpeed"] = storm[3]

            storms.append(newStorm)

        returnData["storms"] = storms    
        return(jsonify(returnData))


    else:
        return(
            jsonify({"error": "State must be provided"}),
            400
        )

if __name__=="__main__":


    US = UnitedStates()
    HDB = HurricaneDatabase()
    landfallRecords = HDB.getLandfallRecords()

    app.run(host="0.0.0.0",port=9999, debug=True)

