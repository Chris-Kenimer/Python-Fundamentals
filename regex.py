import re
def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape", "arsdesnimfdomfdfu"]
    return [word for word in words if re.search(regex, word)]

print "All words that contain a \"v\""
for value in get_matching_words("v"):
    print value
print "----------"
print "All words that contain a double-\"s\""
for value in get_matching_words("ss"):
    print value

print "----------"
print "All words that end with an \"e\""
for value in get_matching_words("e$"):
    print value

print "----------"
print "All words that contain an \"b\", any character, then another \"b\""
for value in get_matching_words("b.b"):
    print value

print "----------"
print "All words that contain an \"b\", at least one character, then another \"b\""
for value in get_matching_words("b+.+b"):
    print value

print "----------"
print "All words that contain an \"b\", any number of characters (including zero), then another \"b\""
for value in get_matching_words("b+.+b"):
    print value

print "----------"
print "All words that include all five vowels in order"
for value in get_matching_words(r"a+.+e+.+i+.+o+.+u"):
    print value

print "----------"
print "All words that only use the letters in \"regular expression\" (each letter can appear any number of times)"
for value in get_matching_words("[regularexpssion]"):

    print value

print "----------"
print "All words that contain a double letter"
for value in get_matching_words(r"(.)\1"):
    print value
