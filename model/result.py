from dataclasses import dataclass

@dataclass
class Result:
    resultId:int
    raceId:int
    driverId:int
    constructorId:int
    number:int
    grid:int
    position:int
    positionText:str
    positionOrder:int
    points:float
    laps:int
    time:str
    milliseconds:int
    fastestLap:int
    rank:int
    fastestLapTime:str
    fastestLapSpeed:str
    statusId:int
    year:str



    def __hash__(self):
        return hash(self.resultId)

    def __eq__(self,other):
        return self.resultId == other.resultId

