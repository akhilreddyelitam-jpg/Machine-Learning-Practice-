import pandas as pd
#dataframes
data = {
    "Name": ["Akhil", "Rahul", "Priya", "Sneha", "Arjun",
             "Kiran", "Manoj", "Divya", "Ravi", "Anu"],

    "Salary": [30000, 45000, 50000, 35000, 60000,
               40000, 55000, 48000, 32000, 65000],

    "Department": ["IT", "HR", "Finance", "IT", "Sales",
                   "HR", "IT", "Finance", "Sales", "IT"],

    "Age": [22, 25, 28, 24, 30, 26, 29, 27, 23, 32]
}
print(data)

df=pd.DataFrame(data)
print(df)
print(df.head())#default the parameter is 5 so the output is 1-4 ,head means from starting
print(df.tail())#defailt the parameter is 5 from last
print(df.iloc[1:3])# it will work in series and dataframes also
print(df.loc[1:3,["Age","Department"]])#when we what certain column so we use lock

print(df["Age"])#it is used when we just want saparate columnor row

df.drop("Age",axis=1,inplace=True)# axis is 1 because we want to drop column //if we want to drop row so axis is 0 it dont change orginal dataframe until we keep inplace=True
print(df)
print(df.shape)#give the no of rows and columns
print(df.info())#it give infromation 
print(df.describe())# it will give   count salary    10.000000  mean   46000.000000 std    11869.662543 min    30000.000000 25%    36250.000000 50%    46500.000000 75%    53750.000000 max    65000.000000'''


#broadcasting
df["Salary"]= df["Salary"]+5000
print(df["Salary"])# it will increasing without any error


#renameing the coloumns
df.rename(columns={"Department":"dept"},inplace=True)
print(df)

#unique
print(df["dept"].unique())# it give unque values from dept 
# when we want to count of how many members have in each department
print(df["dept"].value_counts())


df["promoted_salary"]= df["Salary"]*10;# it is also broadcasting rule and it add new column
print(df)

#data cleaning
print(df.isnull().sum())# it gives how many null values ARE Present //sum() and it will add
print(df.dropna())# it will drop all null rows 
print(df.dropna( how = "any"))# any row that had any null value to will drop
print(df.dropna( how = "all"))#if all the vaalues in any row are null that will drop other wise it will dont touch

## missing values geeting rid we use ->dropna() //for filling we use->fillna()
#print(df.fillna(0))#it will all missing values with zeros it is not recommended it use zero
print(df["Salary"].fillna(df["Salary"].mean(),inplace=True))# inplace true means it wll change oringal dataset //we also use median()
#forward fill and backword fill
#df["Salary"].fillna(method="ffill") ffill is-> forward filling before null value what value is present that value is printed but sometimes it gives errors because the before may be null
#df["Salary"].fillna(method="bfill") ffill is-> backword filling 

#we want to change cells values so we use
df["Name"]=df["Name"].replace("Rahul","mallareddy")
print(df)

# Duplicates;
df_dup=df[df.duplicated(keep="first")]# it will remove duplicate rows from start //keep="last" it will remove duplicates from last
print(df_dup)

df=df.drop_duplicates()# it will drop the duplicates
print(df)

#invalid values
#lambda
df["promoted_salary"]=df["promoted_salary"].apply(lambda x:x/10 if x > 650000 else x)
print(df)


#lambda  apply
def multiplying_salary(x):
    return x*2

df["Salary"]=df["Salary"].apply(multiplying_salary)
print(df)

#lambda
df["Salary"]=df["Salary"].apply(lambda x:x/2)
print(df)


#joins and merges
# joins -> left ,right,outer,inner
department_info={
    "Department":["HR","IT","Finace"],
    "Location":["New york","San frsncisso","Chicago"],
    "Manager":["Laura","Steve","Nina"]
}
df2=pd.DataFrame(department_info)
print(df2)
#concat
print(pd.concat([df,df2])) # 
print(pd.concat([df,df2],axis=1))

#print(pd.merge(df,df2,on="dept"))



#importing File
data = pd.read_excel(r"C:\Users\akhil\Downloads\archive\Air quality information.xlsx")

print(data.head())
print(data.shape)
print(data.info())




























