"""
This is a project to examine the effect that different law schools have
the employment opportunities of the graduates.
"""

import pandas as pd
from matplotlib import pyplot as plt

data_16_file = 'C:\Data\EmploymentSummary-2016.xlsx'
data_16 = pd.ExcelFile(data_16_file)

Unemployed = data_16.parse().UnEmployedSeekingNumber
GradTotals = data_16.parse().TotalGraduatesNumber
EmployedTotals = data_16.parse().Total

Total_graduated = sum(GradTotals)
Total_employed = sum(EmployedTotals)


pay_total_indices = [data_16.parse().columns.get_loc("26-50"),
                     data_16.parse().columns.get_loc("51-100"),
                     data_16.parse().columns.get_loc("101-250"),
                     data_16.parse().columns.get_loc("251-500"),
                     data_16.parse().columns.get_loc("501-PLUS"),
                     data_16.parse().columns.get_loc("Unknown")]

pay_total_value = []
for index in pay_total_indices:
    pay_total_value.append(sum(data_16.parse().ix[:, index]))

second_list = [Total_employed, Total_graduated - Total_employed]
second_args = ["Total Employed", "Total Unemployed"]
pay_scale = ["26K-50K", "51K-100K", "101K-250K", "251K-500K",
             "501K Plus", "Unknown"]
total_reported = sum(pay_total_value)
print(total_reported)

xs = [i for i, _ in enumerate(pay_scale)]
plt.figure(1, figsize=(12, 12))
plt.subplot(211)
plt.bar(xs, pay_total_value)
plt.ylabel("# of Lawyers")
plt.xlabel("Employment Status")
plt.title("Distribution of Reported Lawyer Pay")
plt.xticks([i for i, _ in enumerate(pay_scale)], pay_scale)
plt.autoscale(True)

plt.subplot(212)
xss = [i for i, _ in enumerate(second_args)]
plt.bar(xss, second_list)
plt.xticks([i for i, _ in enumerate(second_args)], second_args)

plt.show()

"""
obviously there is a difference between the reported data and the
actual salary data. Nearly three quarters didn't report income data
"""


