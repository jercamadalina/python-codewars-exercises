def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'


print(areYouPlayingBanjo("martin"))
print(areYouPlayingBanjo("Rikke"))


'''
# Details
    Create a function which answers the question "Are you playing banjo?".
    If your name starts with the letter "R" or lower case "r", you are playing banjo!
    The function takes a name as its only argument, and returns one of the following strings:
        name + " plays banjo "
        name + " does not play banjo"
    Names given are always valid strings.

# Exemplu 1
def areYouPlayingBanjo(name):
    return name + (' plays banjo' if name[0]=='r' or name[0]=='R' else ' does not play banjo')
'''
