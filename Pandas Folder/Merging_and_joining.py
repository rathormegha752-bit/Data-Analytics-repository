''' Merging
    Syntax: pd.merge(df1,df2, on = "Column Name", how = "Type pf join")
    
    Joining ---> Concatenation
    vertically -> Row-wise
    horizontally -> Column-wise
    Syntax: df.concate([df1, df2], axis = 0, ignore_index = True)
'''
# Merging Example
import pandas as pd
df_customers = pd.DataFrame({
    'Customer_id':[1,2,3],
    'Name':['Ramesh','Suresh','Kalpesh']
})

df_orders = pd.DataFrame({
    'Customer_id':[1,2,4],
    'Order_amount':[250,450,620]
})

df_merged = pd.merge(df_customers,df_orders, on = 'Customer_id', how = 'inner')
print(df_merged)


# Conactenation example
import pandas as pd

df_region1 = pd.DataFrame({
    'Customer_id':[1,2],
    'Name':['Ram','Shyam']
})

df_region2= pd.DataFrame({
    'Customer_id':[3,4],
    'Name':['Gopal','Raju']
})

df_concat = pd.concat([df_region1, df_region2], ignore_index = True)
print(df_concat)