import pandas as pd
data = {
    "Name" : ["Megha","Shiva","Ram"],
    "Age" : [20,19,20],
    "City" : ["Ahmedabad","Rajasthan","Maharashtra"]

}

df = pd.DataFrame(data)
print(df)

# using info method to get the dataset information like typr od data
print(df.info())