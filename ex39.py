#create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print '-' * 100
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#print some states
print '-' * 100
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#print every state abbreviation
print '-' * 100
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

#print every city in state
print '-' * 100
for i, j in cities.items():
    print "%s has the city %s" % (i,j)

#now do both at the same time
print '-' * 100
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 100
# safely get an abbreviationby state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

#get a city with a default value
city = cities.get('TX', 'Does not Exist')
print "The city for the state 'TX' is : %s" % city
