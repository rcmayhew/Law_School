import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import pathlib
import warnings
warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)

"""
this is the module to create the graphs that lists the different pay scales for recently graduated lawyers
"""


def law_graph(data, name):
    # lists for each feature
    gradtotals = data.parse().TotalGraduatesNumber
    employedtotals = data.parse().Total
    unknowntotals = data.parse().EmploymentStatusUnknownNumber
    schooltotals = data.parse().EmployedLawSchoolNumber
    gradschooltotals = data.parse().EmployedPursuingGraduateDegreeNumber

    # sum of the list of the feature
    total_school = sum(schooltotals) + sum(gradschooltotals)
    total_graduated = sum(gradtotals)
    total_employed = sum(employedtotals) - total_school
    total_unknown = sum(unknowntotals)

    """lists the indices of the columns that contains the proper info"""
    pay_total_indices = [data.parse().columns.get_loc("Solo"),
                         71,    # location of the total of 2-10K a year
                         76,    # location of the total of 11-25K a year
                         data.parse().columns.get_loc("26-50"),
                         data.parse().columns.get_loc("51-100"),
                         data.parse().columns.get_loc("101-250"),
                         data.parse().columns.get_loc("251-500"),
                         data.parse().columns.get_loc("501-PLUS"),
                         data.parse().columns.get_loc("Unknown")]
    """This is the list of the number of lawyers in each bucket"""
    pay_total_value = []
    for index in pay_total_indices:
        pay_total_value.append(sum(data.parse().ix[:, index]))
    pay_scale = ["Solo", "2K-10K", "11K-25K", "26K-50K", "51K-100K",
                 "101K-250K", "251K-500K", "501K Plus", "Unknown"]

    """
    This is the list of employed vs unemployed. It is here to show
    there is a discrepancy between the number of report salaries and 
    the reported employment numbers.
    """
    total_known = sum(pay_total_value)
    second_list = [total_employed, total_known, total_graduated
                   - total_employed - total_unknown, total_school,
                   total_unknown]
    second_args = ["Total Employed", "Known Pay", "Total Unemployed",
                   "Still in School", "Unknown"]

    """starts the figure for both graphs"""
    fig = plt.figure(1, figsize=(20, 5))
    plt.suptitle(name)
    """this is the pay bucket graph"""
    plt.subplot(1, 2, 1)
    xs = [i for i, _ in enumerate(pay_scale)]
    plt.bar(xs, pay_total_value)
    plt.ylabel("# of Lawyers")
    plt.xlabel("Employment pay")
    plt.title("Distribution of Reported Lawyer Pay")
    plt.xticks([i for i, _ in enumerate(pay_scale)], pay_scale)
    plt.autoscale(True)
    """this is the employed graph"""
    plt.subplot(1, 2, 2)
    xss = [i for i, _ in enumerate(second_args)]
    plt.bar(xss, second_list)
    plt.ylabel("# of Lawyers")
    plt.xlabel("Employment status")
    plt.title("Employed Lawyers")
    plt.xticks([i for i, _ in enumerate(second_args)], second_args)
    """creates the files and the dir in case they have not been created"""
    dic = "Graph/"
    suf = ".png"
    file = "%s%s%s" % (dic, name, suf)
    pathlib.Path(dic).mkdir(parents=True, exist_ok=True)
    fig.savefig(file)
    plt.show()


def FTLT_graph(data, name):
    # lists for each feature
    gradtotals = data.parse().TotalGraduatesNumber
    index = data.parse().columns.get_loc("Total-FTLT")
    employedtotals = data.parse().ix[:, index]
    unknowntotals = data.parse().EmploymentStatusUnknownNumber
    schooltotals = data.parse().EmployedLawSchoolNumber
    gradschooltotals = data.parse().EmployedPursuingGraduateDegreeNumber
    bartotals = data.parse().EmployedBarPassageRequiredNumber

    # sum of the list of the feature
    total_school = sum(schooltotals) + sum(gradschooltotals)
    total_graduated = sum(gradtotals)
    total_employed = sum(employedtotals) - total_school
    total_bar = sum(bartotals)

    """lists the indices of the columns that contains the proper info"""
    pay_total_indices = [data.parse().columns.get_loc("Solo-FTLT"),
                         data.parse().columns.get_loc("2-10-FTLT"),
                         data.parse().columns.get_loc("11-25-FTLT"),
                         data.parse().columns.get_loc("26-50-FTLT"),
                         data.parse().columns.get_loc("51-100-FTLT"),
                         data.parse().columns.get_loc("101-250-FTLT"),
                         data.parse().columns.get_loc("251-500-FTLT"),
                         data.parse().columns.get_loc("501-FTLT"),
                         data.parse().columns.get_loc("Unknown-FTLT")]
    """This is the list of the number of lawyers in each bucket"""
    pay_total_value = []
    for index in pay_total_indices:
        pay_total_value.append(sum(data.parse().ix[:, index]))
    pay_scale = ["Solo", "2K-10K", "11K-25K", "26K-50K", "51K-100K",
                 "101K-250K", "251K-500K", "501K Plus", "Unknown"]

    """
    This is the list of employed vs unemployed. It is here to show
    there is a discrepancy between the number of report salaries and 
    the reported employment numbers.
    """

    non_bar = total_employed - total_bar
    # pay_total_value[1] -= non_bar

    total_known = sum(pay_total_value)
    second_list = [total_employed, total_known, non_bar, total_graduated]
    second_args = ["Total Employed", "Known Pay", "Total Working not as lawyer", "Total Graduated"]

    """starts the figure for both graphs"""
    fig = plt.figure(1, figsize=(20, 5))
    plt.suptitle("FTLT %s" % (name))
    """this is the pay bucket graph"""
    plt.subplot(1, 2, 1)
    xs = [i for i, _ in enumerate(pay_scale)]
    plt.bar(xs, pay_total_value)
    plt.ylabel("# of Lawyers")
    plt.xlabel("Employment pay")
    plt.title("Distribution of Reported Lawyer Pay")
    plt.xticks([i for i, _ in enumerate(pay_scale)], pay_scale)
    plt.autoscale(True)
    """this is the employed graph"""
    plt.subplot(1, 2, 2)
    xss = [i for i, _ in enumerate(second_args)]
    plt.bar(xss, second_list)
    plt.ylabel("# of Lawyers")
    plt.xlabel("Employment status")
    plt.title("Employed Lawyers")
    plt.xticks([i for i, _ in enumerate(second_args)], second_args)
    """creates the files and the dir in case they have not been created"""
    dic = "Graph/"
    suf = ".png"
    file = "%s%s%s" % (dic, name, suf)
    pathlib.Path(dic).mkdir(parents=True, exist_ok=True)
    fig.savefig(file)
    plt.show()

