from shapely.geometry import Polygon, shape, Point
import fiona

class UnitedStates(dict):

    def __init__(self):
        self.loadShapeFiles()
        self.activeState = None

    def __getitem__(self, key):
        self.activeState = key
        return(self)

    # Load the shape files an store in memory
    def loadShapeFiles(self):
        unitedStates = fiona.open('./resources/shapefiles/cb_2018_us_state_20m.shp')
        self.unitedStatesPolygonDictionary = {}
        for state in unitedStates:
            statePolys = []
            stateAbr = state["properties"]["STUSPS"]
            polys = state["geometry"]["coordinates"]

            if len(polys) > 1:
                for spline in polys:
                    p = Polygon(spline[0])
                    statePolys.append(p)
            else:
                p = Polygon(polys[0])
                statePolys.append(p)

            self.unitedStatesPolygonDictionary[ stateAbr ] = statePolys

    def containsCoordinate(self, *coordinates):
        if self.activeState:
            return self._searchState(coordinates)
        else: 
            self._searchAllStates(coordinates)

    def _searchAllStates(self, *coordinates):
        for state in self.unitedStatesPolygonDictionary:
            for section in self.unitedStatesPolygonDictionary[ state ] : 
                if section.contains(Point(coordinates)):
                    self.activeState = None
                    return True
        self.activeState = None
        return(False)

    def _searchState(self, *coordinates):
        for section in self.unitedStatesPolygonDictionary[self.activeState]:
            if section.contains(Point(coordinates)):
                self.activeState = None
                return True
        self.activeState = None
        return(False)