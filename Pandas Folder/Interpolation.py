''' > interpolation ek aisi technique hoti hai jiski madad se missing value 
      ko esteemeted value se fill karta hai.
    > ye sirf numerical column mein use hota hai

    ues:
    > preserve data integrity
    > smmoth trends (time series data)
    > Avoid data loss

    Method:
    > Linear   > Quadratic   > Polynomial   > time

    Syntax: df.interpolate(method = 'Linear', axis = 0, inplace = True)
'''

import pandas as pd
data = {
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}

df = pd.DataFrame(data)
print(df)

#using interpolation method
df["Value"] = df["Value"].interpolate(method = "linear")
print(df)