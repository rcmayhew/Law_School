import pandas as pd
from matplotlib import pyplot as plt
import os
import pathlib


def law_graph(data, name):
    # unemployed = data.parse().UnEmployedSeekingNumber
    gradtotals = data.parse().TotalGraduatesNumber
    employedtotals = data.parse().Total

    total_graduated = sum(gradtotals)
    total_employed = sum(employedtotals)

    pay_total_indices = [data.parse().columns.get_loc("26-50"),
                         data.parse().columns.get_loc("51-100"),
                         data.parse().columns.get_loc("101-250"),
                         data.parse().columns.get_loc("251-500"),
                         data.parse().columns.get_loc("501-PLUS"),
                         data.parse().columns.get_loc("Unknown")]

    pay_total_value = []
    for index in pay_total_indices:
        pay_total_value.append(sum(data.parse().ix[:, index]))
    pay_scale = ["26K-50K", "51K-100K", "101K-250K", "251K-500K",
                 "501K Plus", "Unknown"]

    second_list = [total_employed, total_graduated - total_employed]
    second_args = ["Total Employed", "Total Unemployed"]

    fig = plt.figure(1, figsize=(15, 5))
    plt.suptitle(name)

    plt.subplot(1, 2, 1)
    xs = [i for i, _ in enumerate(pay_scale)]
    plt.bar(xs, pay_total_value)
    plt.ylabel("# of Lawyers")
    plt.xlabel("Employment pay")
    plt.title("Distribution of Reported Lawyer Pay")
    plt.xticks([i for i, _ in enumerate(pay_scale)], pay_scale)
    plt.autoscale(True)

    plt.subplot(1, 2, 2)
    xss = [i for i, _ in enumerate(second_args)]
    plt.bar(xss, second_list)
    plt.ylabel("# of Lawyers")
    plt.xlabel("Employment status")
    plt.title("Employed Lawyers")
    plt.xticks([i for i, _ in enumerate(second_args)], second_args)

    dic = "Graph/"
    suf = ".png"
    file = "%s%s%s" % (dic, name, suf)
    pathlib.Path(dic).mkdir(parents=True, exist_ok=True)
    # os.makedirs(os.path.dirname(dic), exist_ok=True)
    fig.savefig(file)
    plt.show()
