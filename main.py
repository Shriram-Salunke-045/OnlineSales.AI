# To install the libraries
pip install pandas
pip install pandas-profiling
pip install numpy

import pandas as pd
from pandas_profiling import ProfileReport
df = pd.read_csv('police_department_data.csv')
print(df)

# to generate a report
profile  = ProfileReport(df)
profile.to_file(output_file="police_department_data.csv")
