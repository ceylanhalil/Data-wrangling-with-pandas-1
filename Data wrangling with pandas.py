import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
## first importing our data
data=pd.read_csv("C:/Users/SS/OneDrive/Masaüstü/brand.csv", encoding="ISO-8859-1")

## Creating DataFrame
df=pd.DataFrame(data)

## Copieng our data set for any case
df2=df.copy

## Exploring columns of data
df.columns
df.dtypes
df.shape

## Number of columns and rows of data 
print("Our data has {} columns and {} rows".format(len(df.index),df.shape[1]))

## Statistics summary of dataset
df.describe()

## First few rows of data
df.head(5)

## Displaying all columns
pd.set_option("display.max_columns",14)
df.head(1)

## Reseting Set_option
pd.reset_option("display")

## Number of Genres/Industries
df["Genre/Industry"].value_counts()
print("By {} Conglomerate and Financial Services are outnumbered in industries".format(df["Genre/Industry"].value_counts().max()))

## Counting countries
df["Country"].value_counts()

## Setting Brand column as an index
df.set_index("Brand")

## Sorting values according to Brand Value ($M) in 2022   
df.sort_values(by="Brand Value ($M) in 2022", ascending=False).head()

## Making brand name index
df.set_index("Brand")
pd.set_option("display.max.columns",3)
df.head()

## Filtering for Conglomerate brands
congs= df[df["Genre/Industry"]=="Conglomerate"]
print(congs)


## Checking any duplicated brand

df.duplicated()

## Counting countries 
df["Country"].value_counts()

## Company that has min brand value
df[df["Brand Value ($M) in 2022"]==df["Brand Value ($M) in 2022"].min()]

##Company that has max brand value
df[df["Brand Value ($M) in 2022"]==df["Brand Value ($M) in 2022"].max()]

## Checking for missing values
df.isnull()
df.isna().sum()
print("There are no missing value")

## Sorting values as their founded year
df.sort_values(by="Founded In", ascending=True).head()

## Oldest and youngest brands
df.sort_values(by="Founded In", ascending=True).head()
df.sort_values(by="Founded In", ascending=True).tail()

## Dropping unnecessery columns
df.dtypes
df.drop(["Rating in 2022","Rating in 2021","Website"], axis=1)


## Grouping Industries and finding ındustry that has most brand value in 2022
grp_genre=df.groupby("Genre/Industry")["Brand Value ($M) in 2022"].sum()
grp_genre.sort_values(ascending=False)

## Choosing specific row by value
df.columns
df.loc[df["Brand"]=="Google"]

## sorting making some transactions
df.sort_values(by="Founded In", ascending=False)
pd.set_option("display.max_columns",3)
df.loc[(df["Brand"]=="American Express") & (df["Brand"]=="Instagram")]

## Creating pivot table for Brand Value ($M) in 2022 with columns for Genre and industry
df.pivot_table(values="Brand Value ($M) in 2022", columns="Genre/Industry", aggfunc=np.mean)

## Grouping industry and getting Brand Value ($M) in 2022 then sorting them descending order
df.groupby(["Genre/Industry"])["Brand Value ($M) in 2022"].mean().sort_values(ascending=False)


## Conversion of the %Change column from string to float data type
df["% Change"].unique()
df["change_int"]= df["% Change"].str.replace("%","")
df["change_int"]=df["change_int"].astype("float")

## Dropping %Change column 
df.drop(columns=["% Change"],inplace=True)
df.dtypes

## Companies that has more than 20 positive change 
df[df["change_int"]>=20]
df[df["change_int"]>=20].sort_values(by="change_int",ascending=False).shape[0]
print("There are {} companies that has more than 20 psitive change".format(df[df["change_int"]>=20].sort_values(by="change_int",ascending=False).shape[0]))

## Cumulative sum of brand values for 2022 year
df["Brand Value ($M) in 2022"].apply(np.cumsum)

## How many companies at which country
df.groupby(["Genre/Industry"])["Country"].value_counts().sort_values(ascending=False)

df["Brand Value ($M) in 2022"].sort_values(ascending=False).iloc[50]

df[df["Brand Value ($M) in 2022"]>31262.54]

df.groupby(["Genre/Industry"])["Brand Value ($M) in 2022"].agg(np.var,ddof=1)

df[["Brand","Brand Value ($M) in 2022"]].describe()

## Finding outliers as regards brand value column
q1_brand_value=np.quantile(df["Brand Value ($M) in 2022"],0.25)
q3_brand_value= np.quantile(df["Brand Value ($M) in 2022"], 0.75)
IQR= q3_brand_value-q1_brand_value
print(IQR)
lower_cutoff= q1_brand_value- 1.5*IQR
upper_cutoff= q3_brand_value+1.5*IQR
print(lower_cutoff,upper_cutoff)
df[(df["Brand Value ($M) in 2022"]<lower_cutoff)]## there is no outliers for lower_cutoff
df[(df["Brand Value ($M) in 2022"]<upper_cutoff)]

## Nan values
Nan_values= df[df.isna().any(axis=1)]
Nan_values

## Analyzing value diffrences of compnaies between 2022 and 2021
df["value_diff"]= df["Brand Value ($M) in 2022"]- df["Brand Value ($M) in 2021"]
df["value_diff"]= df["value_diff"].astype("float")
df.sort_values(by="value_diff", ascending=False)
df[df["value_diff"]==df["value_diff"].min()]## Alibaba.com is the company that has max negative value_diff
df[df["value_diff"]==df["value_diff"].max()]## Amazon is the company that has the max positive value_diff
df[df["value_diff"]>0]## Compnaies with positive value_diff
print("There are {} companies has psitive value_diff".format(df[df["value_diff"]>0].shape[0]))
df[df["value_diff"]<0]## Companies has negative value_diff
df[df["value_diff"]<0].value_counts("Country")
print("By {} companies China is the country that has most negative value_diff compnay".format(df[df["value_diff"]<0].value_counts("Country").loc["China"])) 




