# In this file all necessary info about pandas libraries

# import pandas as pd
#
# mydataset = {
#     'cars' : [
#     "bmw" , "volvo" , "ford"
#     ],
#     "passings":[3,6,5]
# }
#
# myvar =pd.DataFrame(mydataset)
# print(myvar)
# print(pd.__version__)

# import pandas as pd 
#
# a = [1,8,3]
# myvar =pd.Series(a)
# print(myvar)
# print(myvar[1])


# import pandas as pd 
# calories = {"day1":420 , "day2":410 , "day3":320}
# a = [1,8,3]
# myvar =pd.Series(calories , index =["a","b","c"])
# myvar = pd.Series(calories)
# print(myvar)


# import pandas as pd
#
# data = {
#     "calories" :[320,432,124,232],
#     "duration" :[39,43,12,43]
# }

# df = pd.DataFrame(data)
# here can also use index
# print(df)
# df = pd.DataFrame(data,index = ["day1","day2","day3","day4"])
# print(df)


# lets learn about row
# print(df.loc[[0, 1]])


# lets learn about importing csv files

# import pandas as pd
#
# df = pd.read_csv('./data.csv')
# print(df)


# more about output into string
# import pandas as pd
#
# df = pd.read_csv("./data.csv")
#
# print(df.to_string())

# how many entries should see

# import pandas as pd
# pd.options.display.max_rows = 999
# df = pd.read_csv("./data.csv")
# print(df)
# lets try to import json
# import pandas as pd
# df = pd.read_json("./demo.json")
# print(df.to_string())



# viewing the data

# import pandas as pd
#
# df = pd.read_csv("./data.csv")

# print(df.head())
# print(df.tail())
# print(df.info())

# lets learn Data cleaning

# import pandas as pd 
#
# df = pd.read_csv("./data.csv")
# # df.dropna(inplace=True)
# df["Calories"].fillna(139 , inplace=True)
# print(df.to_string())

# mean median and mode

# import pandas as pd 
# df = pd.read_csv("./data.csv")
#
# x = df["Calories"].mean()
# df["Calories"].fillna(x,inplace = True)
# same as median and mode


# lets learn cleaning data of wrong format
# import pandas as pd 
# df = pd.read_csv("data.csv")
# # df['Date'] = pd.to_datetime(df['Date'])
# df.dropna(subset=['Date'] , inplace =True)
# print(df.to_string())

# replacing values
# df.loc[4,'duration'] = 48

# for x in df.index:
#     if df.loc[x,'duration'] > 120:
#         df.loc[x,'duration'] = 120

# removing rows 

# for x in df.index:
#     if df.loc[x,"duration"] > 120:
#         df.drop(x,inplace=True)

# removing duplicates

# print(df.duplicated())
# df.drop_duplicates(inplace = True)

# correlation
# df.corr()

# plotting and visualization

# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv("./data.csv")
# df.plot()
# plt.show()

# scatter plot
# df.plot(king = "scatter",x = 'durations',y = 'Calories')
# plt.show()

# histogram
# df.plot(king = "hist")
# plt.show()
