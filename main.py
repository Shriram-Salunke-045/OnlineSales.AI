# pip install pandas
# pip install pandas-profiling

import pandas as pd
from pandas_profiling import ProfileReport
df = pd.read_csv('police_department_data.csv')
print(df)

profile  = ProfileReport(df)
profile.to_file(output_file="police_department_data.csv")