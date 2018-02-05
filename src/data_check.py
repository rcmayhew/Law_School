"""
Sometimes the data is bad so this is for some small scripts to check
the accuracy of the data.
"""


def checkdata(data, goal, row=1, checkrange=4, checkskip=1,
              altjump=False, altskip=1, altstart=0, altend=0,
              verbose=False, actual=True):
    """
    Often, the data is grouped in fives, the fifth being the total
    of the prior four. this script will check the 4 prior by default

    :param data: the dataframe that has the section that has the section
    :param goal: the column index that is being checked
    :param row: default is the top row, is the row to be checked
    :param checkrange: defaults 4, stores the range of columns
                    to be checked
    :param checkskip: defaults 1, is the jump size of range
    :param altjump: marks if there is a second step size for the loop
    :param altskip: the alt step size
    :param altstart: when the alt step size starts
    :param altend: when the alt step size ends. altend - altstart
                    must be a multiple of altskip
    :param verbose: labels if you want a print out while you add the
                    columns
    :param actual: choose whether to compare the total to a column or
                    choose to simply display the total
    :return: either true if no problem
             or a tuple of the index if problem
    """

    sumcheck = 0
    goalcheck = data.parse().ix[row, goal]
    if not altjump:
        altstart = goal

    for i in range(goal - checkrange, altstart, checkskip):
        datum = data.parse().ix[row, i]
        if verbose:
            print("+ %s: (%s, %s)" % (datum, row + 2, data.parse().columns[i]))
        sumcheck += datum

    if altjump:
        for j in range(altstart, altend, altskip):
            sumcheck += data.parse().ix[row, j]

        for k in range(altend, goal, checkskip):
            sumcheck += data.parse().ix[row, k]

    if verbose:
        if actual:
            print("= %s, Actual: %s" % (sumcheck, goalcheck))
            print("\n")
        else:
            print("= %s" % sumcheck)
            print("\n")
    if not actual:
        return sumcheck
    if sumcheck == goalcheck:
        return True
    else:
        return [row + 2, goal + 1, sumcheck]


def add_index(inputs, hold):
    if isinstance(inputs, bool):
        return
    else:
        hold.append(inputs)


def checkdoc(data):
    """
    should be used to check the whole document. every year has the
    same format so I want to a script to check each one
    :param data: the dataframe that contains the document
    :return: return a list of all the problem indices
    """


    """
    DOES NOT COUNT THE FUNDED!!!! 
    """
    list_of_errors = []
    for y in range(len(data.parse().SchoolName)):

        # is 5-30 check -5 step 1
        for i in range(5, 30, 5):
            first_run = checkdata(data, i, y)
            add_index(first_run, list_of_errors)

        # 5/10/15/20/25/30/32/33/34/35 to prove 36: check -16 step 5, check -4 step 1
        second_run = checkdata(data, 36, y, 31, 5, True, 1, 31, 36)
        add_index(second_run, list_of_errors)

        # 41-151 check -5 step 1
        for j in range(41, 5, 151):
            third_run = checkdata(data, j, y)
            add_index(third_run, list_of_errors)

        # 147-150 check -85 step 5
        for k in range(147, 152):
            # print(k)
            fourth_run = checkdata(data, k, y, 85, 5, verbose=False)
            add_index(fourth_run, list_of_errors)

        # 151 needs to be checked again -5 step 1
        fifth_run = checkdata(data, 151, y)
        add_index(fifth_run, list_of_errors)

        # print(list_of_errors)
    return list_of_errors


def explore(data):
    print("Total difference between job income and job category by school")
    printout = False
    total_diff = 0
    for y in range(len(data.parse().SchoolName)):
        # goal is 107, start is 66, check -41 step 5
        income = checkdata(data, 107, y, 41, 5, verbose=printout, actual=False)
        # goal is 147, start is 111, check -36 step 5
        category = checkdata(data, 147, y, 36, 5, verbose=printout, actual=False)
        difference = income - category
        total_diff += difference
        # print("%s: \t %s" % (data.parse().SchoolName[y], differnce))
        print("%s: %s" % (difference, total_diff))


def mean(a, b):
    return (a + b)/2


def averagepay(data, row, cols):
    incomeTotal = 0
    hired = 0
    pay = []
    for index in col:
        pay.append(data.parse().ix[row, index])
    hired = sum(pay)
    incometotal = pay[0]*mean(2, 10) + pay[1]*mean(11, 25)
    + pay[2]*mean(26, 50) + pay[3]*mean(51, 100)
    + pay[4]*mean(101, 250) + pay[5]*mean(251, 500)
    + pay[6]*mean(501, 1000)
    return incometotal/hired


def incomeAve(data):

    cols = [71,  # location of the total of 2-10K a year
            76,  # location of the total of 11-25K a year
            data.parse().columns.get_loc("26-50"),
            data.parse().columns.get_loc("51-100"),
            data.parse().columns.get_loc("101-250"),
            data.parse().columns.get_loc("251-500"),
            data.parse().columns.get_loc("501-PLUS")]

    averagepays = []
    for y in range(len(data.parse().SchoolName)):
        averagepays.append(averagepay(data, y, cols))

    return zip(data.parse().SchoolNames, averagepays)