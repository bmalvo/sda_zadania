# Format a string of names like 'Bart, Lisa & Maggie'.

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'
#
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'
#
# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'

names_4 = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Stefka'}]
names_3 = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
names_2 = [{'name': 'Bart'}, {'name': 'Lisa'}]
names_1 = [{'name': 'Bart'}]


def list_of_names(names):
    names = [x["name"] for x in names]
    print(names)
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        names.insert(-1, "&")
        names = " ".join(names)
        return names
    if len(names) == 3:
        names.insert(-1, "&")
        names_first = [names[0], names[1]]
        names_second = [names[2], names[3]]
        names_first = ", ".join(names_first)
        names_second = " ".join(names_second)
        names = names_first + " " + names_second

        return names


print(list_of_names(names_3))
