"""
This is a project to examine the effect that different law schools have
the employment opportunities of the graduates.
"""

import pandas as pd
import graphing as gr
import data_check as dc

data_17_file = 'Data\EmploymentSummary-2017.xlsx'
data_17 = pd.ExcelFile(data_17_file)
aveBySchool = dc.genAve(data_17)
# ERROR = dc.checkdoc(data_17)
# gr.FTLT_graph(data_17, "data_2017")
# gr.law_graph(data_17, "data_2017")

# data_16_file = 'Data\EmploymentSummary-2016.xlsx'
# data_16 = pd.ExcelFile(data_16_file)
# gr.law_graph(data_16, "data_2016")

"""
obviously there is a difference between the reported data and the
actual salary data. Nearly three quarters didn't report income data
"""

"""
lets start taking a look at a correlation between school ranking 
and money after college. Then after I wast to look at pay after
school based on FirstLargestEmployment.
"""
# schools = data_17.parse().SchoolName
# print(schools)
