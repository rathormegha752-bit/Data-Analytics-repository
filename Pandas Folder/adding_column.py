import pandas as pd

data = {
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print("Sample DataFrame",df)

# Adding column
df['Bonus'] = df['Salary'] *0.1
print(df)

# Updating the dataset
# kisi specific row ko column ko access kar sakte hai

print('Before Updating')
df.loc[0,'Salary'] = 50000
print(df)

print('After updating')
df['Salary'] = df['Salary']*1.05
print(df)

# Removing
# Syntax: df.drop(columns = ["Column Name"], inplace = True)
df.drop(columns = ["Performance Score"], inplace = True)
print(df)