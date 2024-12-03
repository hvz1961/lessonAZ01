import pandas as pd

# data = [1, 2, 3, 4, 5]
# series = pd.Series(data)
# print(series)

# data = {
#     "Name" : ["Alex", "Bob", "Anna", "Den"],
#     "Age" : [22, 38, 45, 18],
#     "City" : ["New York", "LA", "Chicago", "Moscow"]
# }
#
# df = pd.DataFrame(data)
# print(df)

# df = pd.read_csv("gym_members_exercise_tracking.csv")
# print(df.head(5))
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df["Age"])
# print(df[["Age", "Gender"]])
# print(df.loc[56])
# print(df.loc[56, "Calories_Burned"])
# print(df[df["Calories_Burned"] > 1100])

# df["Test"] = [new for new in range(973)]
# print(df)
#
# df.drop("Test", axis=1, inplace=True)
# print(df)

# df.drop(972, axis=0, inplace=True)
# print(df)

# df.to_csv("output.csv", index=False)

df = pd.read_csv("dz (1).csv")
print(df)

df.fillna(0, inplace=True)
print(df)

group = df.groupby("City")["Salary"].mean()
print(group)

df.to_csv("dz(2).csv",index=False)
















