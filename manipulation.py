from collections import Counter
from data import employee_data
import numpy as np
import pandas as pd

class Manipulation():
    def __init__(self):
        self.employee_data = employee_data

    def average_by_dept(self):
        df = pd.DataFrame(self.employee_data)
        grouped = df.groupby(['dept']) 
        average = grouped.mean()
        return  {r: kv.to_dict().get('salary') for r, kv in average.iterrows()}

    def headcount_over_time(self, dept):
        df = pd.DataFrame(self.employee_data)
        grouped = df.groupby(['date'])

        if dept:
            further_list = []
            for index, row in df.iterrows():
                if row['dept'] == dept:
                    further_list.append({'dept': row['dept'], 'salary': row['salary'], 'date': row['date']})

            df2 = pd.DataFrame(further_list)
            grouped = df2.groupby(['date'])

        
        count = grouped.count()

        return  {'data' : [{'month':r, "headcount" : kv.to_dict().get('dept')} for r, kv in count.iterrows()]}
