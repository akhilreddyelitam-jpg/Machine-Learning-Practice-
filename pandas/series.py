import pandas as pd
s=pd.Series([12,13,3,14])
print(s)
s.name="calaries"
print(s)
print(s[0])
print( s[0:2] )

#iloc = location based indexing
print(s.iloc[3])
print(s.iloc[[1,2]])


#indexing
index=["apple","banana","grapes","strawberry"]
s.index=index
print(s)

print(s['grapes'])
#print(s.iloc['grapes'])error

print(s.loc['grapes'])

#lock= label based indexing , your start as well as stop value both are included in the output
print(s["banana":"straberry"])

#how to make dictory to series
fruits = {
    "Apple": 0.3,
    "Banana": 1.1,
    "Mango": 0.8,
    "Orange": 0.9,
    "Grapes": 0.7,
    "Papaya": 0.5,
    "Guava": 2.6,
    "Pineapple": 0.5,
    "Strawberry": 0.7,
    "Kiwi": 1.1
}
s2=pd.Series(fruits,name="protein")
print(s2)

#conditional selection:
print(s2[s2>1])

#logical operators
print(s2[(s2>0.5) &(s2<2)])

#modifing the series
s2["mango"]=5.0
print(s2)






















