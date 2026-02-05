''' NAN = not a number
    None = for object data typs
'''
import pandas as pd

data = {
    "Name":['Ram','Shyam',None,'Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,None,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print("Sample DataFrame",df)

print(df.isnull().sum())
