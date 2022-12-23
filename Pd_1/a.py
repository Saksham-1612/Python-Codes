import pandas as pd
df = pd.read_csv(r"C:\Code\Python\Pd_1\data.csv")
# pd.options.display.max_rows = 9999
# print(pd.options.display.max_rows)
# print(df.to_string())
print(df.head(10))
print("-------------------------------TAIL--------------------------")
print(df.tail(10))
print("-------------------------------Info--------------------------")
print(df.info())
