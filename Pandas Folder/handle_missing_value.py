''' hum missing value ke saath 2 kaam kar sakte hai
    1- jaha null value ho vo row ya column delete kar do
        > delete karne ke liye dropna() use hogi
    2- jaha null value ho vaha koi na koi value fill kardo
        > value fill karne ke liye fillna() use hogi
'''

import pandas as pd

data = {
    "Name":['Ram','Shyam',None,'Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,None,30,29,40,25,32],
    "Salary":[50000,60000,None,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print("Sample DataFrame",df)

# # 1 we delete performance column 
# df.drop(columns = ["Performance Score"],inplace = True)
# print(df)

# 2 we fill the value 
df["Age"].fillna(df["Age"].mean(),inplace=True)
print(df)

df["Salary"].fillna(df["Salary"].mean(), inplace=True)
print(df)