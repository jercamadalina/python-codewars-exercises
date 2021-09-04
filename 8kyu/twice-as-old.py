def twice_as_old(dad_years_old, son_years_old):
    twice_sons_age = 2*son_years_old
    difference = dad_years_old - twice_sons_age
    return abs(difference)


print(twice_as_old(36, 7), 22)
print(twice_as_old(55, 30), 5)
print(twice_as_old(42, 21), 0)
print(twice_as_old(22, 1), 20)
print(twice_as_old(29, 0), 29)


'''
# Details
    Your function takes two arguments:
    current father's age(years)
    current age of his son(years)
    Сalculate how many years ago the father was twice as old as his son ( or in how many years he will be
    twice as old).

def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old-2*son_years_old)
'''
