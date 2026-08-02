class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        Total = sum(distance)

        if destination < start:
            start,destination = destination, start 
        
        clockwiseDistance = sum(distance[start:destination])
        antiClockwiseDistance = Total - clockwiseDistance

        return min(clockwiseDistance, antiClockwiseDistance)