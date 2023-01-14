
class Point:
    
    
    def __init__(self, x, y):
        
        self.__x = x
        self.__y = y
        
        def distance_to_origin(self):
            
            return (self.__x **2 + self.__y **2) ** .5
        

p = Point(0,1)


print(p.distance_to_origin())