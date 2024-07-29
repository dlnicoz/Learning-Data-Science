import pandas as pd 

# helllo >jdheeraj sahni




# creating series using pd
# this is list
series = pd.Series([1,1,2,3,4])
# print(series)
# see differnecess
# this is dictionary
seriesa=pd.Series({})
#   print(seriesa)

# lets create dataFrame
# its is dictionary of list
data = {
        "name" : ['dher' , 'sahn' , 'jakd'],
        "age" : [21,32,42]
}

# list of dictionaries
dataa = [
        {"name":"dhhera" ,"age" :21},
        {"name":"dhhera" ,"age":33}
]

# df = pd.DataFrame(data)
df = pd.DataFrame(dataa)
# print(df)


# column operations
# df.rename(columns={"name":"full name"}, inplace = True)
# df.rename(columns={"name":"fullname" , "age":"umar"} , inplace = True)
# df.drop(columns = ['umar'] , inplace = True)
# df["height"] = ["21" , '32']
# print(df)

# row operation indexing implicit and explicit
ndata = {"name" : ["dher" , "saha"] , "age" :[20,21]}
df = pd.DataFrame(ndata)
# nd = pd.DataFrame(ndata , index=["a","b"])

# nd = pd.DataFrame(ndata , index=[32,23])
# print(nd)

# ndd = {"name":"dadd" , "age" : 44}
# nd.append(ndd , ignore_index=True)
# print(nd)

# row drop 
# df = df.drop(index=1)
# print(df.drop(index=0))


# loc and iloc label based indexing
datal = {"Name":["ss" , "dd" ,"gg"], "Age":[11,22,33] }
dfl = pd.DataFrame(datal)
# print(dfl.loc[1:7]) 
# print(dfl.iloc[0])
# print(dfl.iloc[[0,1]])

# indexing
# print(dfl[["Name" , "Age"]])
# print(dfl.iloc[2])

# slicing
# print(dfl[1:2])
# print(dfl[:2])
# print(dfl.loc[: ,"Name"])
# print(dfl.loc[:1, "Name":"Age"])
# print(dfl.iloc[1:2, 1])

# lets solve duplicates
datad = {'Name': ['Alice', 'Bob', 'Alicefe'], 'Age': [25, 30, 25]}
dfd = pd.DataFrame(datad)
# print(dfd)
# dupdata = dfd.drop_duplicates(subset=["Name"])
# print(dupdata)


# lets see aggregate function

# print("this is mean",dfd["Age"].mean())
# print("this is sum",dfd["Age"].sum())
# print("this is min",dfd["Age"].min())
# print("this is max",dfd["Age"].max())
# print("this is count",dfd.count())

# groupby aggregation

gdata = {'Name': ['Alice', 'Bob', 'Charlie', 'Alice'],
        'Age': [25, 30, 35, 25],
        'City': ['NY', 'LA', 'NY', 'LA']}
gdata1 = {'Name': ['1Alice', '1Bob', '1Charlie', 'Alice'],
        'Age': [25, 30, 35, 25],
        'City': ['NY', 'LA', 'NY', 'LA']}

gdf = pd.DataFrame(gdata)
gdf1 = pd.DataFrame(gdata1)

# grouped = gdf.groupby("City")["Age"].mean()
grouped = gdf.groupby("City")["Age"].agg(['mean' , 'sum' , 'count'])
# print(grouped)

# sorting array

# sorted = gdf.sort_values(by="Age")
sorted = gdf.sort_index()
# print(sorted)

# Concatenating

# conc = pd.concat([gdf , gdf1] , axis=1)
# conc = pd.concat([gdf , gdf1] , axis=0)
# conc = pd.concat([gdf , gdf1]  )
# print(conc)

# merging

# mergeddf = pd.merge(gdf ,gdf1 , on="Name" ,how="inner")
# print(mergeddf)

# apply method

# gdf["age_5"] = gdf["Age"].apply(lambda x: x + 5)
# print(gdf)

# filter in groupby
# filtered = df.groupby('City').filter(lambda x: x['Age'].mean() > 30)


# apply in groupbased
# def custom_func(x):
#     x['Age'] = x['Age'] - x['Age'].mean()
#     return x
#
# applied = df.groupby('City').apply(custom_func)

# melting
# metled = pd.melt(gdf, id_vars=["Name"] , value_vars=["Age"])
# print(metled)

# pivoted = df.pivot_table(values='Age', index='Name', columns='City', aggfunc='mean')
