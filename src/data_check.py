"""
Sometimes the data is bad so this is for some small scripts to check
the accuracy of the data.
"""


def checkdata(data, goal, row=1, checkrange=4, checkskip=1,
              altjump=False, altskip=0, altstart=0, altend=0):
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
    :return: either true if no problem
             or a tuple of the index if problem
    """
    sumcheck = 0
    # data.parse().ix[:, index]
    goalcheck = data.parse().ix[row, goal]
    storeskip = checkskip
    for i in range(goal - checkrange, goal, checkskip):
        # print(data.parse().ix[row, i])
        print(i)
        sumcheck += data.parse().ix[row, i]
        if altjump and i + checkskip > altstart:
            checkskip = altskip
            i = altstart - checkskip
        if altjump and i == altend:
            checkskip = storeskip
    if sumcheck == goalcheck:
        return True
    else:
        return row, goal


def add_index(input, hold):
    if input:
        return
    else:
        hold.append(input)


def checkdoc(data):
    """
    should be used to check the whole document. every year has the
    same format so I want to a script to check each one
    :param data: the dataframe that contains the document
    :return: return a list of all the problem indices
    """
    list_of_errors = []
    for y in range(len(data.parse().SchoolName)):
        # is 5/10/15/20/25/30/ check -5 step 1
        """
        for i in range(5, 5, 30):
            first_run = checkdata(data, i, y)
            add_index(first_run, list_of_errors)
        """
        # 5/10/15/20/25/30/32/33/34/35 to prove 36: check -16 step 5, check -4 step 1
        second_run = checkdata(data, 36, y, 31, 5, True, 1, 32, 36)
        # print(second_run)
        # 41-151 check -5 step 1
        # 147/148/149/150 check -105 step 5
        # 150 needs to be checked again -5 step 1
    print(list_of_errors)
