''' > Sorting Syntax:
       Syntax: df.sort_values(by = "Column name", True/False, inplace = True)
    > Aggregation:
        syntax:
        df["Column Name"].mean()
        df["Column Name"].sum()
        df["Column Name"].min()
        df["Column Name"].max()
        This is the agregation method use for mathematical operation

        Grouping with agrgration
        Syntax: grouped = df.grooupby("Age")["Salary"].sum()
    '''

import pandas as pd
data = {
    "Name":["Arun","Varun","Karan"],
    "Age":[40,25,38],
    "Salary":[10000,20000,30000]
}
df = pd.DataFrame(data)
print(df)

# Sorting Method
# df.sort_values(by = "Age", ascending=True, inplace = True)
# print(df)

# Sorting with multiple column
df.sort_values(by = ["Age","Salary"], ascending=[True,False] ,inplace = True)

# Aggregration
avg_salary = df["Salary"].mean()
print(avg_salary)

sum_salary = df["Salary"].sum()
print(sum_salary)

# Grouping with agregration
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)

# Multiple Grouping
grouped1 = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped1)