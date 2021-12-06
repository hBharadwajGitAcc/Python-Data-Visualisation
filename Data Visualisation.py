import pandas as pd
import numpy as np


data = pd.read_csv("C:\\Users\\user\\Downloads\\customer_churn.csv")


import matplotlib.pyplot as plt
%matplotlib inline


# Task 1 
data["Contract"].value_counts()
data["Contract"].unique()
data["Contract"].nunique()

contract_type = data.Contract.value_counts().sort_values(ascending=False)

fig = plt.figure(figsize = (10,5))
contract_type.plot(kind='bar', color="orange")
plt.title("Distribution of contract")
plt.xlabel("Contract type of Customer")
plt.ylabel("Count")
plt.show()

        ### or ###

a = data["Contract"].value_counts()
type(a)
a.dtype
a1 = a.to_dict()
names = list(a1.keys())
values = list(a1.values())

fig = plt.figure(figsize = (10,5))
plt.bar(names,values, color="orange", width = 0.25)
plt.title("Distribution of contract")
plt.xlabel("Contract type of Customer")
plt.ylabel("Count")
plt.show()


        ### or ###

import seaborn as sns
sns.countplot(x ='Contract', data = data, hue="Contract") 
sns.countplot(x ='Contract', data = data, color = "orange") 




# Task 2
data["MonthlyCharges"].value_counts()

df1 = pd.Categorical(data["MonthlyCharges"])
df2 = data.MonthlyCharges.astype('category')

df1.value_counts().sort_values(ascending=False)
df2.value_counts().sort_values(ascending=False)

fig = plt.figure(figsize = (10,5))
data.MonthlyCharges.hist(color="forestgreen")
plt.title("Distribution of Monthly Charges")
plt.xlabel("Monthly Charges Incurred")
plt.ylabel("Count")
plt.grid(False)
plt.show()


# One can use pandas "cut" fuction to get more granular look at data.

df0 = data["MonthlyCharges"]
# Set up bins
bin = [10,29,40,120]
# Use pd.cut function can attribute the values into its specific bins
category = pd.cut(df0,bin)
category = category.to_frame()
category.columns = ['range']
# Concatenate MonthlyCharges and its bin
df_new = pd.concat([df0,category],axis = 1)
sns.countplot(x ='range', data = df_new) 


df = data["MonthlyCharges"]
labels = ["10-28","28-30","30-40","40-50","50-60", "60-70","70-80","80-90","90-100","100-110","110-120"]
bins = [10,28,30,40,50,60,70,80,90,100,110,120]         
df['mc'] = pd.cut(df,bins = bins,labels =labels)
pd.crosstab(df.mc,df.mc).plot(kind="bar")




# Task 3
plt.figure(figsize=(14,6))
plt.scatter(x=data["tenure"], y=data["TotalCharges"].dropna(), c='indigo', s=200)
plt.legend(['tenure','TotalCharges'],loc='best')
plt.title("Total Charges vs Tenure")
plt.xlabel("Tenure of the Customer")
plt.ylabel("Total Charges Incurred")
plt.grid(False)
plt.show()




# Task 4
plt.figure(figsize=(14,6))
sns.boxplot(x="PaymentMethod", y="MonthlyCharges", hue="PaymentMethod", data=data, color="olive")
plt.title("Monthly Charges vs Payment Method")
plt.xlabel("Payment Method of Customer", fontsize=12)
plt.ylabel("Monthly Charges Incurred", fontsize=12)
plt.grid(False)
plt.show()

