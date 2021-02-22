# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
@author: bodonohoe
"""

import pandas as pd

#import data
df = pd.read_csv("C:/Users/bodonohoe/OneDrive - RSA Group/DS/Python/Salary Project/SalaryProject/glassdoor_jobs.csv")


#split salary
df["hourly"] = df["Salary Estimate"].apply(lambda x: 1 if "per hour" in x.lower() else 0)
df["employer_provided"] = df["Salary Estimate"].apply(lambda x: 1 if "employer provided salary" in x.lower() else 0)

df = df[df["Salary Estimate"] != "-1"]
salary = df["Salary Estimate"].apply(lambda x: x.split("(")[0])
minus_Kd = salary.apply(lambda x: x.replace("K", "").replace("$", ""))
min_hr = minus_Kd.apply(lambda x: x.lower().replace("per hour","").replace("employer provided salary:",""))

df["min_salary"] = min_hr.apply(lambda x: int(x.split("-")[0]))
df["max_salary"] = min_hr.apply(lambda x: int(x.split("-")[1]))
df["avg_salary"] =(df.min_salary + df.max_salary)/2


#company name
df["company_txt"] = df.apply(lambda x: x["Company Name"] if x["Rating"]<0 else x["Company Name"][:-3], axis = 1)

#state
df["job_state"] = df["Location"].apply(lambda x: x.split(",")[1])
df["same_state"] = df.apply(lambda x: 1 if x.Location == x. Headquarters else 0, axis =1)

#company age
df["age"] = df.Founded.apply(lambda x: x if x <1 else 2021 -x)

#split job spec. 
df["python_yn"] = df["Job Description"].apply(lambda x: 1 if "python" in x.lower() else 0)
df["R_yn"] = df["Job Description"].apply(lambda x: 1 if ("r studio" in x.lower()) or ("r_studio" in x.lower()) or ("rstudio" in x.lower()) else 0)
df["spark"] = df["Job Description"].apply(lambda x: 1 if "spark" in x.lower() else 0)
df["aws"] = df["Job Description"].apply(lambda x: 1 if "aws" in x.lower() else 0)
df["excel"] = df["Job Description"].apply(lambda x: 1 if "excel" in x.lower() else 0)


df_out = df.drop(["Unnamed: 0"], axis = 1)

df_out.to_csv("salary_data_cleaned.csv", index = False)



