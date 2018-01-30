"""
This is a project to examine the effect that different law schools have
the employment opportunities of the graduates.
"""

import pandas as pd
# from matplotlib import pyplot as plt
import graphing as gr

data_16_file = 'Data\EmploymentSummary-2016.xlsx'
data_16 = pd.ExcelFile(data_16_file)
gr.law_graph(data_16, "data_2016")

data_17_file = 'Data\EmploymentSummary-2017.xlsx'
data_17 = pd.ExcelFile(data_17_file)
gr.law_graph(data_17, "data_2017")

"""
obviously there is a difference between the reported data and the
actual salary data. Nearly three quarters didn't report income data
"""
