"""Your classmates asked you to copy some paperwork for them. You know that there are 'n'
classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0."""


def paperwork(classmates, pages):
    """Return how many pages are need to copy paperwork"""
    if classmates < 0 or pages < 0:
        res = 0
    else:
        res = pages * classmates
    return res
