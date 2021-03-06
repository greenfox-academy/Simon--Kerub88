# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts listOfNumbers as an input
# it should return "true" if it contains all, otherwise print "false"

listOfNumbers = [2, 4, 6, 8, 10, 12, 14, 16]
# checklist = [4, 8, 12, 16]

def isinlist(list_elements):
    scan = 0
    for l in range(len(list_elements)):
        if list_elements[l] == 4 or list_elements[l] == 8 or list_elements[l] == 12 or list_elements[l] == 16:
            scan += 1
    if scan == 4:
        return True
    else:
        return False

print(isinlist(listOfNumbers))


# /////   Other solution   /////

listOfNumbers = [2, 4, 6, 8, 10, 12, 14, 16]
checklist = [4, 8, 12, 16, 13]

def isinlist(list_elements, check):
    factory = False
    scan = 0

    for c in check:
        for l in list_elements:
            if l == c:
                scan += 1
                if scan == len(check):
                    factory = True
    return factory



print(isinlist(listOfNumbers, checklist))
