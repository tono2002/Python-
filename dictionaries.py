
# Dictionaries

# Dictionaries are used in order to store information in key-value pairs
# We can create multiple key-value pairs
# Once we want to acess any piece of information we can refer to it by its key
# Like a real dictionary: word -> key ; definition -> value

# In this case we're creating multiple key-value pairs 

from calendar import month


monthConversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December"
}
#    KEY : VALUE
#    Every key must be unique

# Ways for refer for the value ny its key
print(monthConversions["Mar"])
print(monthConversions.get("Dec"))

# Default value for this key
print(monthConversions.get("Ton", "Not a valid key"))

# If you try to acces a value by typing in a key that
# isn't in the dictionary, you get "none" as a result

print(monthConversions.get("Hi"))