import pandas as pd
data = {
    "Name" : ["Megha","Trusha","Tejashree"],
    "Age" : [20,19,20],
    "City" : ["Ahmedabad","Rajasthan","Maharashtra"]

}

df = pd.DataFrame(data)
print(df)

# df.to_csv("Output.csv", index=False)
# df.to_excel("Output.xlsx", index=False)
df.to_json("Output.json", index=False)