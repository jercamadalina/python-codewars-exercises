def how_much_i_love_you(nb_petals):
    phrases = {0: "I love you",
               1: "a little",
               2: "a lot",
               3: "passionately",
               4: "madly",
               5: "not at all"}
    return phrases[(nb_petals - 1) % 6]


print(how_much_i_love_you(7), "I love you")
print(how_much_i_love_you(3), "a lot")
print(how_much_i_love_you(6), "not at all")


'''
# Details
    Who remembers back to their time in the schoolyard, when girls would take a flower and tear its
    petals, saying each of the following phrases each time a petal was torn:
        I love you
        a little
        a lot
        passionately
        madly
        not at all
    When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.
    Your goal in this kata is to determine which phrase the girls would say for a flower of a given
    number of petals, where nb_petals > 0.

# Exemplu 1
def how_much_i_love_you(nb_petals):
    return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1]

# Exemplu 2
def how_much_i_love_you(nb_petals):
    n = nb_petals % 6
    if n == 1:
        return "I love you"
    if n == 2:
        return "a little"
    if n == 3:
        return "a lot"
    if n == 4:
        return "passionately"
    if n == 5:
        return "madly"
    if n == 0:
        return "not at all"
'''
