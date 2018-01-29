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
pay_scale = ["26-50", "51-100", "101-250", "251-500",
             "501 Plus", "Unknown"]

print(pay_total_value)


xs = [i + 0.1 for i, _ in enumerate(pay_scale)]
plt.bar(xs, pay_total_value)
plt.ylabel("# of Employed Lawyers")
plt.xlabel("Pay Scales")
plt.title("Distribution of Lawyer Pay")
plt.xticks([i for i, _ in enumerate(pay_scale)], pay_scale)

plt.show()
