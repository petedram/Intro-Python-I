# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    # constructor
    def __init__(self, lat, long):
        # initializing instance variable
        self.lat = lat
        self.long = long

x = LatLon(1,2)

print(x.lat, x.long)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name, lat, long):
        self.name = name
        super().__init__(lat, long)
    
    def __str__(self):
        return '{self.name} {self.lat} {self.long} '.format(self=self)


y = Waypoint('home', 3, 4)
print(y.name, y.lat, y.long)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, difficulty, size, name, lat, long):
        self.difficulty = difficulty
        self.size = size
        super().__init__(name, lat, long)

    def __str__(self):
        return '{self.difficulty} {self.size} {self.name} {self.lat} {self.long}'.format(self=self)


z = Geocache('sf', 5, 6, 'hard', 100)
print(z.lat, z.long, z.difficulty, z.size, z.name)


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(1.5, 2, "Newberry Views", 44.052137, -121.41556)

# Print it--also make this print more nicely
print(geocache)
