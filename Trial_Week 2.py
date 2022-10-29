# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
#WEEK 2 (TRIAL VIDEOS)

#Topic 1: Series in PANDAS
#Serie meaning: One-dimensional "ndarray" with axis labels (including...
#..time series)

#Topic 1.1:When we print the serie, the result told us about the type of...
#...data that we get. For instance:
#We will get "data type: "object = str" if we have in the serie strings.
#We will get "data type: "int64 = int" if we have in the serie numbers.
#We will get "data type: "NaN = None Type" if we have in the serie numbers.

#Topic 1.2:The last instance is used when we want to represent the lack of data(...
#...it means "None Type" in Python or "NaN = Not a Number" on Pandas)...
#...Pandas does a conversion from "None Type" to "NaN". "Nan" is "Floting...
#...Point Value" (it means it is similar to None, but it is a special...
#...numerica value).

#Topic 1.3:It is very important to know that Pandas store "Series values" in a type...
#...array using the Numpy library (it means, save memory in comparison...
#...with Python Lists).
       
#Topic 1.4:Examples using "Python Lists"
import pandas as pd

animals =  ["lion", "fish", "dog", "cat"]
print("Topic 1.4.1:\n",pd.Series(animals))
print("\n")

animals_quimera =  ["lion", "fish", "dog", 3]
print("Topic 1.4.2:\n",pd.Series(animals_quimera))
print("\n")

numbers =  [343, 45345, 45645, 3]
print("Topic 1.4.3:\n",pd.Series(numbers))
print("\n")

numbers_quimera =  [343, 45345, 45645, None]
print("Topic 1.4.4:\n",pd.Series(numbers_quimera))
print("\n")

#Topic 1.5:Examples using "Python Dictionaries"and transforming it in a...
#..."Serie". It is important to say that when we print the result of the...
#...transformation from "Python Dictionary to Serie" the Serie will be...
#...ordered alphabetically accordingly to the words of the dictionary's keys...
#...It means that the Serie printed might be ordered differently from the...
#..original Python Dictionary.

#Topic 1.5.1.: Also it is important to say that the  dictionary's keys will...
#...be like a guide or "index" to find something in a serie.
sport = {"Golf":"Rich", "Soccer":"Poor", "Baseball":"Countryside","Sumo":"Japan"}
NewX = pd.Series(sport)
print("Topic 1.5:\n",NewX)
print("\n")

#Topic 1.6:Printing the index of my "Serie"
print ("Topic 1.6:\n",NewX.index)
print("\n")

#Topic 1.7:We can create a "Serie" joining the List of "data values" and my...
#...List of "Indexes" (it is like fragmented Python dictionary) and create a...
#..."Serie".
NewX2 = pd.Series(["Bread", "Rice", "Tofu"], index=["USA", "Panama", "Cuba"])
print("Topic 1.7:\n",NewX2)
print("\n")

#Topic 1.8:We can find something in the "Serie" by "Index Position" or by...
#..."Index Label".It means, that querying a serie:
#..By numerical index (index like Python) position  = We need to use "iloc"...
#...atribute.
#..By index label = We need to use "loc" atribute.

# In addition, it is importante to say that the "iloc" and "loc" are both...
#...attributes (it means, that they allow us to get additional information...
#...of the Python objects, icluding methods sometimes. Also they do not...
#...need "parentheses ()" to be expressed, just the "dot notation") and not...
#...methods (they are a set of instructions to be executed when they are ...
#...invoked by us by that objects. Also they do need "parentheses ()"...
#...to be executed).

#Topic 1.8.1:We are going to use the data of the "Topic 1.5". Then we are...
#...going to extract the data from index "number 2" of the Serie (it means...
#...their position accordingly with Python index).
print("Topic 1.8.1:\n",NewX.iloc[2])
print("\n")

#Topic 1.8.2:We are going to use the data of the "Topic 1.5". Then we are...
#...going to extract the data from index labeled like "Sumo"...(it means...
#...their position accordingly with Python index).
print("Topic 1.8.2:\n",NewX.loc["Sumo"])
print("\n")

#Topic 1.9:.Applyting a "For Loop" using simle Python code to sum up...
#...the values of a Panda "Serie".
NewX2 = pd.Series([100.00,200.00,34.00,6.00])
print("Topic 1.9:\n",NewX2)
print("\n")

Total = 0
for X in NewX2:
    Total = X+Total
print ("Topic 1.9.1:\n", Total)
print("\n")

Total = 0
for X in NewX2:
    Total += X
print ("Topic 1.9.2:\n",Total)
print("\n")

#Topic 1.10: Applyting a "Numpy" code to sum up the values of a Panda "Serie".
import numpy as np
print("Topic 1.10:\n",np.sum(NewX2))
print("\n")

#Topic 1.11: Applyting a "Panda" code to sum up the values of a Panda "Serie".
print("Topic 1.11:\n",NewX2.sum())
print("\n")


#Topic 1.12: Applying a "Python" code to know the time (in seconds) that...
#...takes to do the execution of the code. Therefore, we need to first...
#...import the module "import timeit"
import timeit
print("Topic 1.12:\n",timeit.timeit(stmt ="4*3"))
print("\n")

#Topic 1.12.1: The triple quotation help us to frame the entire code..
#...that we want to know the time (in seconds) of execution.

Code="""
B = 3
C = 100000
A= B*C
"""
print("Topic 1.12.1:\n",timeit.timeit(stmt =Code))
print("\n")

#Topic 1.12.2: The code "timeit.repeat" allow us to know the time (in...
#...seconds) that takes to do the execution of the code determined number...
#...of times.
print("Topic 1.12.2:\n",timeit.repeat(stmt =Code,repeat=5))
print("\n")

#Topic 1.13: The broadcasting in "Pandas" is just the applying of a procedure...
#...simultaneoulsy in a code.For instance, we want to add to all the values...
#...of the "Serie" the value of "2".
NewX3 =(NewX2+2)
print ("Topic 1.13:\n",NewX3)
print("\n")

#Topic 1.14: The "Panda" attribute ".loc" allow us also to modify the data...
#...and even add new data, like we did in the following examples.We can see..
#...that it is allow to have a mix of indexes (numbers and labels)  or mix...
#...of data in "Pandas".
#...values (numbers and labels).
NewX3.loc["Turkey"]=90
print ("Topic 1.14:\n",NewX3)
print("\n")

NewX3.loc["Roastbeef"]="Delicious"
print ("Topic 1.14.1:\n",NewX3)

#Topic 1.15: Then we create a Panda "Serie" and then append it with other...
#..."Serie".
sport2 = {"Tennis":"Nadal", "Nike":"Nadal", "Spain":"Nadal"}
NewX4 = pd.Series(sport2)
print("Topic 1.15:\n",NewX4)
print("\n")

Allsports = NewX.append(NewX4)
print("Topic 1.15.1:\n",Allsports)
print("\n")


############################################################################


#Topic 2: Data Frame Data Structure
#Topic 2.1: First, we create several "Series". Then we create a "Data Frame"...
#...that will collect all the "Series"in just one table.
purchase1 = pd.Series({"Name":"Chris","Item Purchased":"Dog Food","Cost":22.50})
purchase2 = pd.Series({"Name":"Kevyn","Item Purchased":"Kitty Litter","Cost":2.50})
purchase3 = pd.Series({"Name":"Vinod","Item Purchased":"Bird Seed","Cost":5.00})

df1 = pd.DataFrame([purchase1,purchase2,purchase3],index=["Store 1","Store 1","Store 2"])
print("Topic 2.1:\n",df1)
print("\n")

#Topic 2.2.1:If we want to get only a specific row completely we can apply..
#...the following code.The "label" are according to the "label index". In...
#...this case we will obtain two rows because there are two rows with the...
#...same label.

# It is importante to say the "iloc" and "loc" are used for row selection.
print("Topic 2.2.1:\n",df1.loc["Store 1"])
print("\n")

#Topic 2.2.2:If we want to get only a specific column completely we can apply..
#...the following code.

# It is importante to say the for column selection we use "indexing operator"...
#..."Label" based.
print("Topic 2.2.2:\n",df1["Cost"])
print("\n")

#Topic 2.3.1:If we want to get only a specific row completely we can apply..
#...the following code.The "label" are according to the "label index".
print("Topic 2.3.1:\n",df1.loc["Store 2"])
print("\n")

#Topic 2.3.2:If we want to get only a specific row completely we can apply..
#...the following code.The numbers are according to the index number...
#...(similarly to python). We can see that we want to obtain the same...
#..result that in te "Topic 2.3.1".
print("Topic 2.3.2:\n",df1.iloc[2])
print("\n")

#Topic 2.3.3:If we want to get a specific combination of "row"and "column"...
#...we can apply the following code; therefore, we can see the use of "loc...
#...code" to take in count the row, and then we put the label of the column.
print("Topic 2.3.3:\n",df1.loc["Store 1","Cost"])
print("\n")

#Topic 2.3.4:If we want to get specific "columns" we can apply the...
#...following code.
print("Topic 2.3.4:\n",df1[["Cost","Item Purchased"]])
print("\n")

#Topic 2.3.5:If we want to get specific "columns" we can apply the...
#...following code (a lil bit awkward), because we use the transpose of the...
#...Data Frame and then the rows are the columns, and the columns are the...
#...rows.
df2 = df1.T
print("Topic 2.3.5:\n",df2)
print("Topic 2.3.5.1:\n",df2["Store 2"])
print("\n")

#Topic 2.3.6:If we want to get specific "columns" and "rows" we can apply the...
#...following code using "iloc" and positions accordingly to index of rows...
#...(the last number is excluyent, like in Python) and columns.
print("Topic 2.3.6:\n",df1.iloc[0:3,2])
print("\n")

#Topic 2.3.7:If we want to delete a specific row or rows we can apply the...
#...following code. The result will be the copy of original Data Frame except...
#...that it will not show the delete row or rows.It is important to say that...
#...the code "drop" do not modify the original Data Frame, it just make a...
#...copy and modify that copy of the Data Frame.

#It is important to say that the code "drop" has two optional parameters...
#..describe in the following lines:
#First: It is called "In Place" and if it is set to True, then the Data Frame...
#...will be updated in place, instead of a copy being returned.
#Second: We can select the axes that will be deleted. By default the value...
#...es 0 (zero) for rows, but could be change to 1 (one) for columns.

print("Topic 2.3.7:\n",df1.drop("Store 1"))
print("\n")

#Topic 2.3.8:If we want to delete a specific row or rows we can apply the...
#...following code. The result will be the copy of original Data Frame except...
#...that it will not show the delete row or rows. However to avoid any...
#...confusion we can "copy" the Data Frame and then do the change to the copy...
#...of the Data Fram and in that way we do not touch the original Data Frame.
df3 =df1.copy()
print("Topic 2.3.8:\n",df3.drop("Store 1"))
print("\n")

#Topic 2.3.9:If we want to delete a specific column or columns we can apply the...
#...following code as an alternative to the code "Drop". A great difference...
#..with the code "Drop" is that the modification of the code "delete" in the...
#..."Data Frame" change permanently  and in direct way the "Data Frame".
del df3["Cost"]
print("Topic 2.3.9:\n",df3)
print("\n")

#Topic 2.3.10:If we want to add a column we can apply the...
#...following.
df3["Police"] = "Si hay"
print("Topic 2.3.10:\n",df3)
print("\n")

df4 =df1.copy()
df4["Cost_Disccount"] = ((df4["Cost"])*0.80)
print("Topic 2.3.10:\n",df4)

###########################################################################


#Topic 3: Data Frame and CSV File
#How to change the name of  columns???????????????????????????

#Topic 3.1:If we want to delete a row in CSV File we can apply the folliwing..
#...code. First we need to load the file, then we can delete the row that...
#...we want.
PokemonCSV = pd.read_csv("pokemon_data.csv")
print ("Topic 3.1:\n",PokemonCSV.head())
print("\n")

PokemonCSV1 = pd.read_csv("pokemon_data.csv",skiprows=1)
print ("Topic 3.1.1:\n",PokemonCSV1.head())
print("\n")

#Topic 3.2: If we want to find and SEE only specific set of values or elements...
#...in certain column (in this case in the column "Name"), we can...
#...search and find those values with the use of piece of phrase or word.

#In this case we need to be carefull about how to write ...
#...the words that we want to find (it means, if there is some capital...
#...letter or lowercase, we need to put it in that exactly way). And...
#...the symbol of OR(|) need to be together of words that we want to find.                                                                                                 
                                            
PokemonCSV2 = pd.read_csv("pokemon_data.csv")
Poke2 = PokemonCSV2.loc[PokemonCSV2["Type 1"].str.contains("Fire|Grass", regex = True)] 
print ("Topic 3.2:\n",Poke2)
print("\n")

#Topic 3.3: If we want apply some  filter with booleans and see what...
#...values of the data accomplish certain requistis and what other do not.The..
#...result will be expressed like a "Serie".
PokemonCSV3 = pd.read_csv("pokemon_data.csv")
Poke3 = PokemonCSV3["Attack"]>100
print ("Topic 3.3:\n",Poke3)

#Topic 3.4: If we want apply some  filter with booleans and see how many...
#...values of the data accomplish certain requistis and what other do not.The..
#...result will be expressed like a "Serie".
Poke4 = Poke3.count()
print ("Topic 3.4:\n",Poke4)
print("\n")

#Answer 1
#PokemonCSV4 = pd.read_csv("pokemon_data.csv")
#AP1 = PokemonCSV4.sort_values("Defense", ascending = False)
#print (AP1)
#AP2 = AP1.iloc[0,0]
#print(AP2)
#AP3 = AP1.index
#print (AP3)
#AP4 = AP3[0]
#print (AP4)
#print(type(AP4))
#print("\n")

#Answer 2
#PokemonCSV5 = pd.read_csv("pokemon_data.csv")
#AR1 = PokemonCSV5.loc[(PokemonCSV5["Attack"]!=49)&(PokemonCSV5["Defense"]!=49)]
#print(AR1)


#Answer 3.1
#PokemonCSV5 = pd.read_csv("pokemon_data.csv")
#print(PokemonCSV5)
#PokemonCSV5 = PokemonCSV5.loc[(PokemonCSV5["Attack"]>100)&(PokemonCSV5["Defense"]>100)]
#print(PokemonCSV5)
#PokemonCSV5["Difference1"] = abs((((PokemonCSV5["Attack"])-(PokemonCSV5["Defense"])))/(PokemonCSV5["HP"]))
#print(PokemonCSV5["Difference1"])
#PokemonCSV5= PokemonCSV5.sort_values("Difference1", ascending = False) 
#print(PokemonCSV5)
#AR2 = PokemonCSV5.index
#print(AR2)
#AR3 = AR2[0]
#print(AR3)

#Answer 3.3
#PokemonCSV5 = pd.read_csv("pokemon_data.csv")
#print(PokemonCSV5)
#PokemonCSV6 = PokemonCSV5.loc[PokemonCSV5["Attack"]>100]
#print(PokemonCSV6)
#PokemonCSV7 = PokemonCSV6.loc[PokemonCSV5["Defense"]>100]
#print(PokemonCSV7)
#PokemonCSV5["Difference1"] = abs((((PokemonCSV5["Attack"])-(PokemonCSV5["Defense"])))/(PokemonCSV5["HP"]))
#print(PokemonCSV5["Difference1"])
#PokemonCSV5= PokemonCSV5.sort_values("Difference1", ascending = False) 
#print(PokemonCSV5)
#AR2 = PokemonCSV5.index
#print(AR2)
#AR3 = AR2[0]
#print(AR3)





#Answer 4
#PokemonCSV6 = pd.read_csv("pokemon_data.csv")
#print(PokemonCSV6)
#print("\n")
#PokemonCSV6["Point"] = ((PokemonCSV6["Attack"]*3)+(PokemonCSV6["Defense"]*2)+(PokemonCSV6["HP"]*1))
#print(PokemonCSV6)
#print("\n")
#A = PokemonCSV6["Point"]
#print(A)
#print("\n")
#Points = pd.Series(A)
#print(Points)

#Answer 5
#PokemonCSV8 = pd.read_csv("pokemon_data.csv")
#print(PokemonCSV8)
#Filtro1 = PokemonCSV8.loc[(PokemonCSV8["Attack"]>50)]
#print (Filtro1)
#Filtro1["count"]=0
#S1 = Filtro1.groupby(["Legendary"]).count()["count"]
#print (S1)
#U1= S1.sort_values(ascending = False) 
#print(U1)
#W1 = U1.index
#print(W1)
#Y1 = W1[0]
#print(Y1)

#Answer 6
#PokemonCSV9 = pd.read_csv("pokemon_data.csv")
#print(PokemonCSV9)
#PokemonCSV9["Col1"] = PokemonCSV9.loc[(PokemonCSV9["Type 1"]=="Grass") & (PokemonCSV9["Attack"])>0]
#print (PokemonCSV9)
#Filtro22 = Filtro11.groupby(["Type 1"]).count()
#print (Filtro22)
#Filtro22= Filtro11.sort_values(ascending = False) 



#Answer 7
#PokemonCSV11 = pd.read_csv("pokemon_data.csv")
#print(PokemonCSV11)
#PokemonCSV11["Permut1"] = abs((PokemonCSV11["Attack"])-(PokemonCSV11["Defense"]))
#print(PokemonCSV11)
#PokemonCSV11["Permut2"] = abs(PokemonCSV11["Attack"]-PokemonCSV11["HP"])
#print(PokemonCSV11)
#Filtro70 = PokemonCSV11.loc[(PokemonCSV11["Attack"]>50)]
#print (Filtro70)
#Filtro71 = Filtro70.sort_values(["Permut1","Permut2"], ascending=False)
#print (Filtro71)
#Filtro72 = Filtro71["Name"]
#print (Filtro72)
#Filtro73 = Filtro72.iloc[0]
#print(Filtro73)

#Answer 8
#PokemonCSV10 = pd.read_csv("pokemon_data.csv")
#print(PokemonCSV10)
#Filtro81 = PokemonCSV10.loc[(PokemonCSV10["Type 1"]=="Grass") | (PokemonCSV10["Type 1"]=="Bug")]
#print (Filtro81)
#Filtro82 = Filtro81.loc[Filtro81["Name"].str.contains("Mega")] 
#print (Filtro82)
#Filtro83 = Filtro82.loc[(Filtro82["Attack"]>Filtro82["Defense"])]
#print (Filtro83)
#Filtro84 = Filtro83[["Name","Type 2"]]
#print (Filtro84)















