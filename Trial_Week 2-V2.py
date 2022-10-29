# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:54:29 2021

@author: USUARIO
"""
#BASIC DATA PROCESSING WITH PANDAS

#We will begin our understanding:
    #The fundamentals of one of the most important toolkits Python has for data...
    #...cleaning and processing (Pandas). 
    #How to read in data into DataFrame structures
    #How to query these structures
    #Details about such structures are indexed. 

#Topic 1:Series in Panda
import pandas as pd
import numpy as np

#Series in Panda:
    #Is one of the core data structures in pandas. 
    #The items are all stored in an order and there's labels with which you...
    #...can retrieve them. 
    #An easy way to visualize this is two columns of data. The first is the...
    #...special index, a lot like keys in a dictionary. While the second column....
    #...is your actual data (it is important to note that the data column...
    #...has a label of its own and can be retrieved using the name attribute)

#We can create a series by passing in a "list" of values (when we do this,...
#...Pandas automatically assigns an index starting with zero and sets the name...
#...of the series to None. (It is important to say that we will see the values...
#...of the "index column" and "series column" and also the "type of data"...
#...in the printed result)

#Type of data:
    #Object: for strings or mix (string, integers and floats)
    #int64:for integers numbers
    #float64:for float numbers or mix (integers and floats)
        #The format of "int64" and "float64" is a kind of format that allow....
        #...to speed up the velocity of the processes in comparisons with...
        #...Lists in Python.
    
students = [1, 1, 2]
x1 = pd.Series(students)
print(x1)
print("\n")

#We can create a series by passing in a "dictionary" of values (when we do this,...
#...Pandas automatically assigns the keys of the dictionary as a index)

students_scores = {'Alice': 'Physics',
                   'Jack': 'Chemistry',
                   'Molly': 'English'}
x01 = pd.Series(students_scores)
print(x01)
print("\n")

#We can create a series by passing in a Lisf if "tuples" of values (when we do..
#...this, Pandas automatically assigns an index starting with zero.

studentsname = [("Alice","Brown"), ("Jack", "White"), ("Molly", "Green")]
x02 = pd.Series(studentsname)
print(x02)
print("\n")

#We can create a series by passing the index and values in a separate way. To...
#...specific, we first create the List of values or text of the serie an then...
#...we create the List of values or text of the index.

x03 = pd.Series(['Physics', 'Chemistry', 'English'], index=['Alice', 'Jack', 'Molly'])
print(x03)
print("\n")

#We use "None" in Pandas (it is like the "None Type" in Python) to handle...
#...missing data. In this case we mix it with....
#...string a integers. As a result, the printed result show the word "None"

students = [1, "a", None]
x2 = pd.Series(students)
print(x2)
print("\n")

#We use "None" in Pandas to handle missing data. In this case we mix it with....
#...floats and integers.As a result, the printed result show the word "NaN"...
#...(Not a Number).

    #This "NaN" is the result o the conversion of "None Type" in Python in a...
    #...special floating point number designated as "NaN". As a result, the...
    #...printed result is show as a dtype "float64".

#"NaN", is meaning is similar to "None", but it's a numeric value and treated..
#...differently for efficiency reasons.

students = [1, 1, None]
x3 = pd.Series(students)
print(x3)
print("\n")

#We can get the index of the serie and also the type of object.
x4 = pd.Series(['Physics', 'Chemistry', 'English'], index=['Alice', 'Jack', 'Molly'])
x5 = x4.index
print(x5)
print("\n")

#We can change the index of the serie. It is important to say that in this...
#...case the values of the new index will be "None" because those new indexes...
#...are different from the old indexes and they are not related with the old...
#...values.
x6 = pd.Series(['Physics', 'Chemistry', 'English'], index=['Alice', 'Jack', 'Molly'])
x7 = pd.Series(x6, index=['Alice', 'Roy', 'Bett'])
print(x7)
print("\n")

#Series in Panda:
    #Is one of the core data structures in pandas. 
    #The items are all stored in an order and there's labels with which you...
    #...can retrieve them. 
    #An easy way to visualize this is two columns of data. The first is the...
    #...special index, a lot like keys in a dictionary. While the second column....
    #...is your actual data (it is important to note that the data column...
    #...has a label of its own and can be retrieved using the name attribute)

##############################################################################

#Topic 2: Querying in Series 

#We will learn how to query and merge Series objects together, and the...
#...importance of thinking about parallelization when engaging in data science...
#... programming.

#We can get data from a Serie in the following ways: 
    #Through the position of the index (Python Index) and through the label...
    #...of the index (no matter if the index is string or a number). 
    
    #Also we can use attributes "iloc" and "loc" to get data from a Serie. 
        #Keep in mind that "iloc" and "loc" are not methods, they are...
        #...attributes so we don't use parentheses to query them, but square...
        #...brackets instead.
        #Also, "iloc" is used for position index (i.e. numbers) and "loc" is...
        #...used of labels of the index (i.e. strings).
        
#Important:
#If our index is a list of integers, Pandas can't determine automatically...
#... whether you're intending to query by index position or index label. The...
#...safer option is to be more explicit and use the iloc or loc attributes..
#...directly.

#Topic 2.1: Getting data using only the label of the index
students_classes = {'Alice': 'Physics',
                   'Jack': 'Chemistry',
                   'Molly': 'English',
                   'Sam': 'History'}
s1 = pd.Series(students_classes)
print(s1)
print("\n")

s2 = s1["Molly"]
print("Topic 2.1",s2)
print("\n")

#Topic 2.2: Getting data using only the position of the index (like Python index).
s3 = s1[2]
print("Topic 2.2:",s3)
print("\n")

#Topic 2.3: Getting data using only the "iloc" attribute.
s4 = s1.iloc[2]
print("Topic 2.3:",s4)
print("\n")

#Topic 2.4: Getting data using only the "loc" attribute.
s5 = s1.loc["Molly"]
print("Topic 2.4:",s5)
print("\n")

#Topic 2.5:
#If we know certain codes of Pandas and Numpy we can take advantage of that...
#...and achieve result in a faster way than we normal Python code. This is...
#...very helpful considering the capacity of the computers. 

    #For instance, if we want to get the average of a list of numbers, we can...
    #...to that in a tradition Python way (using "for" loop code).

grades1 = pd.Series([90, 80, 70, 60])

total1 = 0
for gradex in grades1:
    total1+=gradex
print("Topic 2.5.1:",total1/len(grades1))
print("\n")

    #For instance, Pandas and the underlying Numpy libraries support a method...
    #...of computation called "Vectorization", which works with most of the...
    #functions in the Numpy library, including the "Sum function" (Then we..
    #...just call "np.sum" and pass in an iterable item. In this case, our...
    #...Panda series).
    
    #We need to be aware of parallel computing features and start thinking in...
    #...functional programming terms. Put more simply,"vectorization" is the...
    #...ability for a computer to execute multiple instructions at once (i.e....
    #...run thousands of instructions in parallel).

import numpy as np

total2 = np.sum(grades1)
print("Topic 2.5.2:",total2/len(grades1))
print("\n")

#Topic 2.6:                                                                   
# A Related feature in Pandas and Numpy is called "broadcasting". With...
#...broadcasting, you can apply an operation to every value in the Panda Series,...
#...changing the Panda Series. 

# Let's look at the head of our series
numbers20 = [20, 40, 60, 80]
numbers21 = pd.Series(numbers20)
# And now lets just increase everything in the series by 2
numbers21+=2
print("Topic 2.6:",numbers21)
print("\n")

#Topic 2.7:
#As an alternative to the "Topic 2.6" we can also iterate through all of the...
#...items in the Panda series and increase the values directly. Pandas does...
#...support iterating through a series much like a dictionary through...
#...."iteritems()" function which returns a "label and value". 

numbers20 = [20, 40, 60, 80]
numbers22 = pd.Series(numbers20)

for label, value in numbers22.iteritems():
    numbers22.set_value(label, value+2)
    
print("Topic 2.7:",numbers22)
print("\n")

#Topic 2.8:
#In the following code we will see how fast is the code (tradition Python way) vs...
#...the "Pandas and the underlying Numpy libraries". For this, the "Python...
#...has something called the function "timeit".

    #"timeit": this function will run our code a few times to determine,..
    #...on average, how long it takes (in seconds). Also we can give "timeit" the number...
    #...of loops that you would like to run. By default, it is 1,000 loops, but...
    #...we can modify the number of times thee funcion "timeit" runs).
    
    #There are several arguments in the function "timeit" 
        #stmt: which is the statement you want to measure; it defaults to ‘pass’.
        #setup: which is the code that you run before running the "stmt"; We...
        #....generally use this to import the required modules for our code.
        #number: which is the number of executions you’d like to run the stmt.
        
    #It is very important to say that we need to put inside the "setup" all..
    #...the code, even the libraries or modules (for instance: "Panda" and...
    #..."Numpy" in this case".

# importing the required module. 
import timeit  

#Then we time the code (tradition Python way)
mycode1 = '''  
import pandas as pd
import numpy as np
numbers30 = pd.Series(np.random.randint(0,10,100))

total3 = 0
for numberx in numbers30:
    total3+=numberx
total3/len(numbers30) 
''' 
print ("Topic 2.8.1:", timeit.timeit(setup = "pass", 
                     stmt = mycode1, 
                     number = 100))  
print("\n")

# Then we time the code (using the "Pandas and the underlying Numpy libraries")
mycode2 = '''  
import pandas as pd
import numpy as np
numbers30 = pd.Series(np.random.randint(0,10,100))

total4 = np.sum(numbers30)
total4/len(numbers30)
'''  
print ("Topic 2.8.2:", timeit.timeit(setup = "pass", 
                     stmt = mycode2, 
                     number = 100))  
print("\n")

#Topic 2.9: 
#The ".loc" attribute lets us not only modify data, but also add new data..
#...as well. If the value you pass in as the index doesn't exist, then a new...
#...entry is added. 

#When we apply ".loc" to add new data, we do not need to worry about indices...
#...because they can have mixed types (string,int,float,etc.)

simples = pd.Series([1, 2, 3])

    # We could add some new value. It is important to say that this added value...
    #...be at the end of the Serie.
simples.loc['History'] = 102
print ("Topic 2.9.1:", simples)  
print("\n")

    # We could change an exisiting value or index.
simples = pd.Series([1, 2, 3])

simples.loc[0] = 102
print ("Topic 2.9.2:", simples)  
print("\n")

#Topic 2.10:
#We can have a Serie with an index that is repeated several times (that will...
#...not be a problem to print). And if we want to get an element, we will see...
#...printed the all entire Serie or the portion of the Serie that contain the...
#...same index.

#And also we can join two or more Serie in a one single...
#...Serie through the code "Append()".When we use "append()" it is important...
#...to consider: 
    #Pandas will take the series and try to infer the best data...
    #...types to use. 
    #The append method doesn't actually change the underlying Series objects,...
    #...it instead returns a new series which is made up of the two appended...#
    #...together (one below the other).
    
#Serie without repeated index
studgroup1 = pd.Series({'Alice': 'Physics',
                   'Jack': 'Chemistry',
                   'Molly': 'English',
                   'Sam': 'History'})
print ("Topic 2.10.1:", studgroup1)  
print("\n")

#Serie with repeated index                            
studgroup2 = pd.Series(['Philosophy', 'Arts', 'Math'], index=['Ary', 'Kelly', 'Kelly'])
print ("Topic 2.10.2:","\n",studgroup2)  
print("\n")

#Getting data using only the "loc" attribute.
s28 = studgroup2.loc["Kelly"]
print("Topic 2.10.3:",s28)
print("\n")

#Appending Series
studgroupjoin = studgroup1.append(studgroup2)
print ("Topic 2.10.4:", studgroupjoin)  
print("\n")

############################################################################

#Topic 3.1:Dataframe
#We can create a Dataframe in almost tha same way we create a Serie. Those...
#...ways are the followings:
    
    #Creating several series and the joining them with new indexes.It is...
    #...important to say that the indexes of the series will be the labels...
    #...of the dataframe columns (ordered alphabetically).
    
record1 = pd.Series({'Name': 'Alice',
                        'Class': 'Physics',
                        'Score': 85})
record2 = pd.Series({'Name': 'Jack',
                        'Class': 'Chemistry',
                        'Score': 82})
record3 = pd.Series({'Name': 'Helen',
                        'Class': 'Biology',
                        'Score': 90})    

df1 = pd.DataFrame([record1, record2, record3],index=['school1', 'school2', 'school1'])
print ("Topic 3.1.1:","\n", df1)  
print("\n")
    
    #Creating a list of dictionaries and the joining them with new indexes

students = [{'Name': 'Alice',
              'Class': 'Physics',
              'Score': 85},
            {'Name': 'Jack',
             'Class': 'Chemistry',
             'Score': 82},
            {'Name': 'Helen',
             'Class': 'Biology',
             'Score': 90}]

df2222 = pd.DataFrame(students, index=['school1', 'school2', 'school1'])
print ("Topic 3.1.2:","\n", df2222)  
print("\n")

#Topic 3.2:
#We can get information (a row, a specific cell or a column) from Dataframe. In...
#...this case we are going to describe how to get a row.

    #Getting information (a entire row) from Dataframe. As an answer we also obtain...
    #...the name of the row index and also the dtype of data that row (int64,...
    #...float64 or object)
    
    #It is very important to say that we use "iloc" and "loc" for row selection.
df3 = df2.loc['school2']       
print ("Topic 3.2.1:","\n", df3)  
print("\n")

    #Getting information (a entire row) from Dataframe. As an answer we...
    #...obtain a dataframe with two rows in this case (because there are two...
    #...indexes with the same label).
df4 = df1.loc['school1']       
print ("Topic 3.2.2:","\n", df4)  
print("\n")

    #We can get the type of data a that row (in this case a serie)
print(type(df1.loc['school2']))
print("\n")

    #We can get the type of data a that row (in this case a dataframe)
print(type(df2.loc['school1']))
print("\n")

#We can get information (a row, a specific cell or a column) from Dataframe. In...
#...this case we are going to describe how to get a specific cell.

    #We can get a specific cell through two parameters (a row label and a...
    #...column label). We use the indexing operator, i.e. square brackets [].
    
    #It is very important to say that we use "iloc" and "loc" for cell selection.
print(df1.loc['school2', "Name"])
print("\n")

#We can get information (a row, a specific cell or a column) from Dataframe. In...
#...this case we are going to describe how to get a specific column (to be...
#...specific there are two ways to get a column of a datafram).

    #Option 1: We can get a specific column through the indexing operator,...
    #...i.e. square brackets [], in which we put directly the label of the...
    #...column that we are interested to get.
print(df1["Score"])
print("\n")

    #Option 2: We can get a specific column in a clever way. First, we use...
    #...the transpose of the dataframe (to change the positions of rows for the...
    #...positions of the columns). Then we just select a specific row (i.e. we...
    #...select a row that was previously the column that we want it) in the...
    #...way that we previously explained to select rows.
print(df1.T)
print("\n")

df5 = df1.T.loc['Name']       
print ("Topic 3.2.3:","\n", df5)  
print("\n")

#We can get information (a row, a specific cell or a column) from Dataframe.

    #We can use ".loc" (which can take two parameters, the row index and the...
    #...list of column names). Also, the ".loc" attribute supports slicing.
    
    #If we wanted to select all rows or columns, we can use a colon to...
    #...indicate a full slice from beginning to end. 
    #We can add the row or column name in the parameter as a string. 
    #If we wanted to include multiple columns, we could do so in a list and
    #...Pandas will bring back only the columns we have asked for.

df6 = df1.loc[:,['Name', 'Score']]
print ("Topic 3.2.4:","\n", df6)  
print("\n")

#We can delete information (a row or a column) from Dataframe. We just need to..
#...be careful because some codes can overwrite the original dataframe, meanwhile...
#...other codes do not do that (at least if we do not want it).

    #We can delete a row with the code "drop". This code is very special...
    #...we have have the option to overwrite or not the original dataframe. Also...
    #...it is important to remember that by default, this code will delete...
    #... a row. That thing can be achieved modifying the following parameters:
        #inplace=False (if the value is "False" we will not modify the existing...
        #...dataframe, but if the value is "True" we will modify the existing...
        #...dataframe)
        #axis=0 ("0" for delete a row and "1" for delete a column). This is...
        #...very useful in case we have columns and rows with the same name.
        
    #Option 1: Simple way to delete a row (by default).
df7 = df1.drop('school1')
print ("Topic 3.3.1:","\n", df7)  
print("\n")

print ("Topic 3.3.2:","\n", df1)  
print("\n")

    #Option 2: Complex (i.e. specific) way to delete a row.

df8 = df1.copy()
df9 = df8.drop("school1", inplace=False, axis=0)
print ("Topic 3.3.3:","\n", df9)  
print("\n")

print ("Topic 3.3.4:","\n", df8)  
print("\n")

    #We can delete a column with the code "drop". This code is very special...
    #...we have have the option to overwrite or not the original dataframe. Also...
    #...it is important to remember that by default, this code will delete...
    #... a row. That thing can be achieved modifying the following parameters:
        #inplace=False (if the value is "False" we will not modify the existing...
        #...dataframe, but if the value is "True" we will modify the existing...
        #...dataframe)
        #axis=1 ("0" for delete a row and "1" for delete a column). This is...
        #...very useful in case we have columns and rows with the same name.
        #In the caseof columns, it is important to put the "axis=1" if we want...
        #...to delete a column

    #Option 1: Complex (i.e. specific) way to delete a column.
        
df10 = df1.copy()
df11 = df10.drop("Name", inplace=True, axis=1)
print ("Topic 3.3.5:","\n", df11)  
print("\n")

print ("Topic 3.3.6:","\n", df10)  
print("\n")

    #Option 2: Simple way to delete a column (by default). This way is directly through...
    #...the use of the indexing operator [], using the "del" keyword and the...
    #...label fo the column. This way of dropping data, however, takes...
    #...immediate effect on the DataFrame and does not return a view.
    
df12 = df1.copy()
del df12['Name']
print ("Topic 3.3.7:","\n", df12)  
print("\n")

# Finally, adding a new column to the DataFrame is through the use of the...
#...indexing operator [], using the label of the new column and the putting....
#...the content of columns.

df13 = df1.copy()
df13['Ranking'] = None
print ("Topic 3.3.8:","\n", df13)  
print("\n")

##############################################################################

#Topic 4: Dataframe Indexing and Loading

#First, we are going to learn how to import a file (in this case a CSV file)...
#...and then turn this CSV file into a dataframe through the code "read_csv()".

    #It is important to put the file that we are going to open in the folder...
    #...of thee Python file in which we are working on.                                                                      
                                                                           
df14 = pd.read_csv('Admission_Predict.csv')

    # And let's look at the first five rows (because the file has a lot of data).
df15 = df14.head()
print ("Topic 4.1:","\n", df15)  
print("\n")

#Changing the index of the dataframe

    # We notice that by default the index of the dataframe recently created from...
    #...the CSV file starts with zero [0] while the index of the CSV file "per se" not..
    #...necessarily starts with zero [0]. Therefore, to fix that situation and avoid....
    #... a misunderstanding we can take whatever column of the CSV file with....
    #...the code "index_col= "and set it as the official index of the dataframe...
    #...recently created (It is important to put the number [according to Pyhton...
    #...Index] of the column that will be the the new index)

df16 = pd.read_csv('Admission_Predict.csv', index_col=0)
df17 = df16.head()
print ("Topic 4.2:","\n", df17)  
print("\n")

#Changing the title of the columns of the dataframe

    #We have several ways to change the title of the columns.
    #We just need to be careful about the title of the columns, because...
    #...sometimes they have hidden spaces or symbols like (/, -, _, ...)
    
    #Option 1: Simple way to do the change of the columns´s labels of the dataframe.
   
        #In Pandas, we can use the rename() function. It takes a parameter...
        #...called "columns", and we need to pass into a dictionary in which the...
        #..."keys" are the "old column name" and the "value" is the "new...
        #...column name".
        
        #"Rename function" isn't modifying the dataframe. It is just a copy...
        #...of the original datafram with the changed names.

df18 = df14.copy()
df19=df18.rename(columns={'GRE Score':'GRE Score', 'TOEFL Score':'TOEFL Score',
                   'University Rating':'University Rating', 
                   'SOP': 'Statement of Purpose','LOR': 'Letter of Recommendation',
                   'CGPA':'CGPA', 'Research':'Research',
                   'Chance of Admit':'Chance of Admit'})
df20 = df19.head()
print ("Topic 4.3:","\n", df20)  
print("\n")                                   

    #Option 2.1: Fixing manually the columns´s labels  because hidden spaces...
    #...or symbols like (/, -, _, ...).
    
        #Therefore, we check first the columns´s labels using use the "columns...
        #...attribute" of dataframe to get a list.
        
df21 = df18.columns
print ("Topic 4.4:","\n", df21)  
print("\n")                                   
   
        #Then if we look at the output closely, we can see that there is...
        #...actually a space right after "LOR " title and a space right after...
        #..."Chance of Admit " title. So this bother the process of rename...
        #...through the Option 1 (i.e. the dictionary option).
        
        #In this case, one way would be to change a column title is by...
        #...including the space in the name

df22 = df18.rename(columns={'LOR ': 'Letter of Recommendation'})
df23 = df22.head()
print ("Topic 4.5:","\n", df23)  
print("\n")      

    #Option 3: We can use the "df.columns" attribute by assigning to it a...
    #...list of column names which will directly rename the columns. This will...
    #...directly modify the original dataframe and is very efficient...
    #...especially when you have a lot of columns and you only want to change...
    #...a few. This technique is also not affected by subtle errors in the...
    #...column names, a problem that we just encountered. With a list, you...
    #...can use the list´s index to change a certain value or use list...
    #....comprehension to change all of the values


    # As an example, lets change all of the column names to lower case. First...
    #...we need to get our list
df24 = df14.copy()
cols = list(df24.columns)
    # Then a little list comprehenshion
cols = [x.lower().strip() for x in cols]
    # Then we just overwrite what is already in the columns attribute
df24.columns=cols
    # And take a look at our results
df25 = df24.head()                               
print ("Topic 4.6:","\n", df25)  
print("\n")                                    
                                      
##############################################################################

#Topic 5: Querying in Dataframe

#To do Querying in Dataframe we use "Boolean masking".

#Boolean mask: is an array which can be of one dimension like a series, or...
#...two dimensions like a data frame, where each of the values in the array...
#... are either true or false. This array is essentially overlaid on top... 
#...of the data structure that we're querying. And any cell aligned with the...
#...true value will be showed into our final result as "True", and any...
#...cell aligned with a false will be showed into our final result as "False".
                                      
df26 = pd.read_csv('Admission_Predict.csv', index_col=0)
df26.columns = [x.lower().strip() for x in df26.columns]
df27 = df26.head()                                
print ("Topic 5.1:","\n", df27)  
print("\n")                                       

#We will see several ways to manipulate the data of the dataframe with the main...
#...objective to get data.

#Boolean masks are created by applying operators [] directly to the pandas...
#...Series or DataFrame objects. 

    #Option #1: We apply the Boolean Mask through operators [] and also through...
    #....other operators like "greater than", "lesser than" or "equal to" (>, <, ==)...
    #...operators. The resultant Series or Dataframe is indexed according to the...
    #...value of each cell is either True or False. 
    
        #It is important to say that the "Index" of the printed Serie or...
        #...Dataframe does not change
    
        #Underneath, pandas is applying the comparison operator you specified...
        #...through "vectorization" (so efficiently and in parallel) to all of...
        #...the values in the array you specified.
        
        # And any cell aligned with the true value will be showed into...
        #...our final result as "True", and any cell aligned with a false...
        #...will be showed into our final result as "False".
    
df28 = df26['chance of admit'] > 0.7
print ("Topic 5.2:","\n", df28)  
print("\n")                                       

        #After that we are really interested to see that comparison in the...
        #...Dataframe (and not just a "True or False" Serie). Therefore, we...
        #apply a code that "hide" the data we don't want (i.e. data that is...
        #...False). To be specific, we do this by using the ".where()"...
        #...function on the original DataFrame.
        
        #We see that the resulting Dataframe keeps only the data which met the...
        #...condition that comply with "True". All of the rows which did not...
        #....meet the condition (i.e. data that is "False") have "NaN data"....
        #...instead, but these rows were not dropped from our dataset.
        
        #It is important to say that the "Index" of the printed Serie or...
        #...Dataframe does not change
        
            #Important: In this case the "NaN data" are all the that were...
            #...considered previously as "False" (i.e. were converted the...
            #...False data in "NaNa data").
            
            #Important:"where()" doesn't drop missing values by defaul
        
df29 = df26.where(df28).head(10)                        
print ("Topic 5.3:","\n", df29)  
print("\n")                                            

    #Option #2: The same as Option #1, but with little changes described in the...
    #...following lines:
        
        #The next step is, if we don't want the "NaN" data, we use the...
        #..."dropna() function". The returned DataFrame now has all of the...
        #..."NaN" rows dropped. Notice the some values of the index are also...
        #...dropped (i.e. the indexes of data that are "False"). 
        
            #Important: In this case the "NaN data" are all the that were...
            #...considered previously as "False" (i.e. were converted the...
            #...False data in "NaNa data").
            
            #Important:"where()" doesn't drop missing values by defaul
        
df30 = df26.where(df28).dropna().head()             
print ("Topic 5.4:","\n", df30)  
print("\n")

    #Option #3: The same as Option #2, but with little changes described in the...
    #...following lines:
        
        #Despite being really handy, "where()" function isn't actually used...
        #...that often. Instead, the pandas developer created a shorthand...
        #...syntax which combines "where()" and "dropna()" function, doing...
        #...both at once, using indexing operator [] to do this (it is an...
        #...overloaded indexing operator [] which drops NaN values).
        
        #With this we get the exactly dataframe of the Option #2.

df31 = df26[df26['chance of admit'] > 0.7].head()
print ("Topic 5.5:","\n", df31)  
print("\n")

#We can print a column or several columnas at the same time.
    #Printing just one column
df32 = df26["gre score"].head()
print ("Topic 5.6:","\n", df32)  
print("\n")

    #Printing more than one column
df33 = df26[["gre score","toefl score"]].head()
print ("Topic 5.7:","\n", df33)  
print("\n")

#We can combine multiple boolean masks, such as multiple criteria. We can use...
#..."the pipe" "|" (i.e. or) and "ampersand" "&" (i.e. and) operators to...
#...handle this. We have several options to apply this thing:
    
    #Option 1:
df34 = (df26['chance of admit'] > 0.7) & (df26['chance of admit'] < 0.9)
print ("Topic 5.8:","\n", df34)  
print("\n")

    #Option 2:Another way to do this is to just get rid of the comparison...
    #....operator completely (<,>, ==), and instead use the built in functions...
    #...which mimic this approach, in this case "gt" for "greater than" and...
    #..."lt" for "lower than".
df35 = df26['chance of admit'].gt(0.7) & df26['chance of admit'].lt(0.9)
print ("Topic 5.9:","\n", df35)  
print("\n")

    #Option 3: These functions are build right into the Series and DataFrame...
    #...objects, so we can chain them too.
df36 = df26['chance of admit'].gt(0.7).lt(0.9)
print ("Topic 5.10:","\n", df36)  
print("\n")
                                      
##############################################################################

#Topic 5: Indexing in Dataframe 

#The set_index() function is a destructive process, and it doesn't keep the..
#...current index (i.e. the index that belong to the dataframe). If we want...
#...to keep the current index, we need to manually create a new column (in the...
#...same dataframe) and copy into it values from the index.

    #We can do this by using the indexing operator [] on the string that has...
    #...the column label (i.e. the column label that we want to move from...
    #...index position to other postion of the same dataframe). Then we can use...
    #...the "set_index" function to set index of the column to that we want...
    #...to put in the index position.
df37 = pd.read_csv('Admission_Predict.csv', index_col=0)

    #In this step we are setting that the index column of the original dataframe...
    #...will be inside the dataframe. In this step is very important to...
    #...put the name of the new column (i.e. the column that will receive...
    #the data that belong previously of the index).
df37['Serial Number'] = df37.index    
    
    #In this step we are setting that the index column of the new dataframe...
    #...will be determine by the name of that column.
df37 = df37.set_index('Chance of Admit ')
df38 = df37.head()                                
print ("Topic 6.1:","\n", df38)  
print("\n") 

    # We can also get rid of the index completely (i.e. create a default numbered index)...
    #...by calling the function "reset_index()".This promotes the existing index...
    #...column moves into a column of the same Dataframe.
df37 = df37.reset_index()
df39= df37.head()
print ("Topic 6.2:","\n", df39)  
print("\n") 

#The multi-level indexing allow us apply "set index" and give it a list of...
#...columns that we're interested in promoting to an index.
df40 = pd.read_csv('census.csv')
df41 = df40.head()
print ("Topic 6.3:","\n", df41)  
print("\n") 

    #In this case, we are starting in a light way, doing a simple filter (i.e....
    #...a "one column filter). It means, just watching a new dataframe, in...
    #...which the filter was applied.
    
    #It is important to say that in this code I do not apply the function...
    #...set index. Just create a filter with the column.
df42=df41[df41['SUMLEV'] == 50]
df43 = df42.head()
print ("Topic 6.4:","\n", df43)  
print("\n") 

    #In this case, we are increasing the level, doing a lil bit complex filter.
    #...(i.e a "several columns filter). In this case, we create a list of the...
    #...that we are interested to see. Then we create the new dataframe with...
    #...the selected columns.
    
    #It is important to say that in this code I do not apply the function...
    #...set index. Just create a filter with the columns.
columns_to_keep = ['STNAME','CTYNAME','BIRTHS2010','BIRTHS2011','BIRTHS2012','BIRTHS2013',
                   'BIRTHS2014','BIRTHS2015','POPESTIMATE2010','POPESTIMATE2011',
                   'POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
df44 = df42[columns_to_keep]
df45 = df44.head()
print ("Topic 6.5:","\n", df45)  
print("\n")
    
    #It is important to say that in this code I do apply the function...
    #...set index. In this case I create an index with two columns.
df46 = df44.set_index(['STNAME', 'CTYNAME'])
df47 = df46.head()
print ("Topic 6.6:","\n", df47)  
print("\n")

#We can query in a DataFrame that has two or more indexes. 
    #We saw previously that the "loc attribute" of the DataFrame can take...
    #...multiple arguments. And it could query both the row and the columns. 
    
    #When we use a MultiIndex, we must provide the arguments in order by the 
    # level we wish to query. Inside of the index, each column is called a...
    #...level and the outermost column is level zero (i.e. the column in the...
    #...index far left located is the level zero)
df48 = df46.loc['Alabama', 'Bibb County']
df47 = df48.head()
print ("Topic 6.7:","\n", df48)  
print("\n")

    # If we are interested in comparing some values that belong to the...
    #...index columns, we can pass a list of tuples describing the indices...
    #...we wish to query into "loc". 
    
    #Since we have a MultiIndex of two values...
    #...(in this example), we need to provide two values as each element of our 
    # filtering list. Each tuple should have two elements, the first element...
    #...being the first index and the second element being the second index.
df49 = df46.loc[[('Alabama', 'Bibb County'),('Alabama', 'Barbour County')]]
df50 = df49.head()
print ("Topic 6.8:","\n", df50)  
print("\n")

##############################################################################

#Topic 6: Missing Values

#Pandas handles missing values using: "None type" values.

#NumPy handles missing values using: "NaN" values. 

#When we use statistical functions on DataFrames, these functions typically...
#...ignore missing values. For instance if we try and calculate the mean...
#...value of a DataFrame, the underlying NumPy function will ignore missing...
#...values. 

#Missing values are pretty common in data cleaning activities. We wil see two...
#:..of many kinds of instances:

    #"Missing at Random": it is a kind of missing data. However there are other...
    #...variables that might be used to predict the variable which is missing.
    
    #"Missing Completely at Random (MCAR)": it is a kind of missing data...
    #...However there are not other variables that might be used to predict...
    #...the variable which is missing.
df51 = pd.read_csv('class_grades.csv')
df52 = df51.head(10)
print ("Topic 7.1:","\n", df52)  
print("\n")

#We will see several examples of functions and codes that allow us handle...
#...missing data:

    #Function #1:
    #We can use the function ".isnull()" to create a boolean mask...
    #...(i.e. to generate the same dataframe, but full of "True" if there are...
    #..."NaN" values or "False" if there are values).
df53=df51.isnull()
df54= df53.head(10)
print ("Topic 7.2:","\n", df54)  
print("\n")

    #Function #2:
    #We can use the function ".dropna()", which is able to drop all of those...
    #...rows which have any missing data (i.e. this function will eliminate...
    #...from the dataframe all the rows that have missing data. One way to...
    #...see this in a esay way is to look thee values of the index and then....
    #...see the gaps).
df55 = df51.dropna().head(10)
print ("Topic 7.3:","\n", df55)  
print("\n")

    #Function #3:
    #We can use the function ".fillna()", which is able to take the missing...
    #...values and transform it in a specific number or string (this specific...
    #....number or string is decided by the user).
    
    # Note that the inplace attribute causes pandas to fill the values...
    #...and does not return a copy of the dataframe, but instead modifies the...
    #...original dataframe we have.
df52 = df51.copy()

df51.fillna("XXX", inplace=True)
df56 = df51.head(10)
print ("Topic 7.4:","\n", df56)  
print("\n")

df52.fillna(0, inplace=True)
df57 = df52.head(10)
print ("Topic 7.5:","\n", df57)  
print("\n")

    #Function #4:
    #We can use the function ".fillna()", which is able to take the cell of missing...
    #...values and transform it in the previous non missing value or in the...
    #...next no missing value.

df58 = pd.read_csv("log.csv")
df59 = df58.head(20)
print ("Topic 7.6:","\n", df59)  
print("\n")

        #Now we establish a new column as an index and then sort the new...
        #...from low values (from the top) to high values (at the bottom). In...
        #...some way this put in order the values.
df60 = df58.set_index('time')
df61 = df60.sort_index()
df62 = df61.head(20)
print ("Topic 7.7:","\n", df62)  
print("\n")

        #Then we use the parameter "ffill" inside the function ".fillna()" to...
        #...to take the cell of missing values and transform it in the...
        #..."previous non missing values". It is important to say the selected...
        #..."previous non missing value" is the first "non missing value"...
        #...before the "missing value".
df65 = df61.copy()

df63 = df61.fillna(method='ffill')
df64 = df63.head(20)
print ("Topic 7.8:","\n", df64)  
print("\n")

        #Then we use the parameter "bfill" inside the function ".fillna()" to...
        #...to take the cell of missing values and transform it in the...
        #...next non missing values.  It is important to say the selected...
        #..."next non missing value" is the first "non missing value"...
        #...next the "missing value".
df66 = df65.fillna(method='bfill')
df67 = df66.head(20)
print ("Topic 7.9:","\n", df67)  
print("\n")

    #Function #5:
    #This function is similar to Function #3 
    #We can use the function ".replace()", to replace values (missing and...
    #...non-missing values). It allows replacement from several approaches like...
    #...value-to-value, list, dictionary, regex. 
df68 = pd.DataFrame({'A': [1, 1, 2, 3, 4],
                   'B': [3, 6, 3, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']})
print ("Topic 7.10:","\n", df68)  
print("\n")
   
        #In this case we replace (value-to-value) the number 1 for the number 100.
df69 = df68.replace(1, 100)
print ("Topic 7.11:","\n", df69)  
print("\n")

        #In this case we replace (value-to-list) the number 1 and 3 for the number...
        #...100 and 300.
df70 = df68.replace([1, 3], [100, 300])
print ("Topic 7.12:","\n", df70)  
print("\n")

        # To replace using a regex we make the first parameter to replace the...
        #...regex pattern we want to match, the second parameter the value...
        #...we want to emit upon match, and then we pass in a third parameter...
        #.."regex=True".
df71 = df58.replace(to_replace=".*.html$", value="webpage", regex=True)
print ("Topic 7.13:","\n", df71)  
print("\n")

##############################################################################

#Topic 7: Example

#API (Application Programming Interface): is a set of functions that allows...
#...applications to access data and interact with external software components...
#...,operating systems, or microservices. 

#An API delivers a user response to a system and sends the system’s response...
#...back to a user. You click “add to cart;” an API tells the site you added...
#...a product to your cart; the website puts the product in your cart,...
#...and your cart is updated.

df72=pd.read_csv("presidents.csv")
df73 = df72.head()
print ("Topic 8.1:","\n", df73)  
print("\n")

#We will see several ways to handle and treat data:

    #Option 1:
    #Using Regular Expresions (RegEx) to extract, manipulate or handle the...
    #...data that we want.
    
        #First, we make a copy of the column that we are interested (that column). Then...
        #...we can call the function "replace()" plus the Regular Expresions...
        #...(RegEx) to modify, edit or handle the content fo the copied column.
df72["First1"] = df72['President']
df72["First1"] = df72["First1"].replace("[ ].*", "", regex=True)
df74 = df72.head()
print ("Topic 8.2:","\n", df74)  
print("\n")

    #Option 2:
    #Using the "apply() function". The "apply() function" will take some arbitrary...
    #...function we have created and apply it to either a Series (a single...
    #...column) or DataFrame across all rows or columns. 
    
    #The row is a single Series object, which is a single row indexed by....
    #...column values.
    
        #In this case we create a function which just splits a string into...
        #...two pieces using a single row of data
        
def splitname(row):
    # Let's extract the firstname and create a new entry in the series
    row['First2']=row['President'].split(" ")[0]
    # Let's do the same with the last word in the string
    row['Last1']=row['President'].split(" ")[-1]
    # Now we just return the row and the pandas .apply() will take of merging...
    #....them back into a DataFrame
    return row

        # Now we apply the function that we create previously "def splitname...
        #...(row)" to the dataframe through the "apply() function" indicating...
        #...we want to apply it across columns.
df72 = df72.apply(splitname, axis='columns')
df75 = df72.head()
print ("Topic 8.3:","\n", df75)  
print("\n")

    #Option 3.1: 
    #Using the function ".extract()" plus Regular Expresions (RegEx) to...
    #...extract, manipulate or handle the data that we want.
    
        #The function ".extract()" takes a Regular Expresions (RegEx) as...
        #...input and specifically requires that we set "capture groups" that...
        #...correspond to the output columns you are interested in.
        
    #This is a "Regular Expresions (RegEx)" that match and returned groups of...
    #...strings from one column to one or more new columns.
pattern1="(^[\w]*)(?:.* )([\w]*$)"

         #Now the function ".extract()" is built into the "str attribute"...
         #...of the Series object, so we can call it using "Series.str.extract(pattern)"
df76 = df72["President"].str.extract(pattern1)
df77 = df76.head()
print ("Topic 8.4:","\n", df77)  
print("\n")

    #Option 3.2:
    #Using the function ".extract()" plus Regular Expresions (RegEx) to...
    #...extract, manipulate or handle the data that we want.
    
        #The function ".extract()" takes a Regular Expresions (RegEx) as...
        #...input and specifically requires that we set "capture groups" that...
        #...correspond to the output columns you are interested in.
        
    #This is a "Regular Expresions (RegEx)" that match and returned groups of...
    #...strings from one column to one or more new columns.
    
    #In this case we write "Regular Expresions (RegEx)" in which we explicitly....
    #...describe the column names from which we extract the information.
pattern2="(?P<First>^[\w]*)(?:.* )(?P<Last>[\w]*$)"

         #Now the function ".extract()" is built into the "str attribute"...
         #...of the Series object, so we can call it using "Series.str.extract(pattern)"
df78 = df72.copy()
df79 = df78["President"].str.extract(pattern2)
df80 = df79.head()
print ("Topic 8.5:","\n", df80)  
print("\n")

    #Other Exmple of Option 3.1:
    #Using the function ".extract()" plus Regular Expresions (RegEx) to...
    #...extract, manipulate or handle the data that we want.
    
        #We get rid of anything that isn't in the pattern of Month Day and Year.
df81 = df72.copy()

pattern3 = "([\w]{3} [\w]{1,2}, [\w]{4})"     
          
df82 = df81["Born"].str.extract(pattern3)
df83 = df82.head()
print ("Topic 8.6:","\n", df83)  
print("\n")

    #There is an issue with the previous answer, in this case the "type of...
    #...content column" that is printed, in this case the type printed is...
    #..."object", and we know that's what pandas uses when it is dealing with...
    #...string. But pandas has really interesting date/time features;...
    #...therefore, we are going to update this column to the write data type..
    #...as well.

##############################################################################

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
    
#Quiz 2 - February 14, 2021 (RMDLC)


#QUIZ #2  

#Problem #1 <--WINNER 
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj1 = pd.Series(sdata)
print ("Topic Q1.1:","\n", obj1)  
print("\n")
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj2 = pd.Series(sdata, index=states)
print ("Topic Q1.2:","\n", obj2)  
print("\n")
obj3 = pd.isnull(obj2)
print ("Topic Q1.3:","\n", obj3)  
print("\n")
print ("Topic Q1.4","\n", obj2['California'] == None)  
print("\n")

#Problem #2 <--WINNER 
d = {'1': 'Alice','2': 'Bob','3': 'Rita','4': 'Molly','5': 'Ryan'}
S = pd.Series(d)
S2 = S.iloc[0:3]
print ("Topic Q2.1","\n", S2)  
print("\n")

#Problem #3 <--I AM NOT SURE 
Prob31 = [{'Name': 'Alice',
              'Class': 'Physics',
              'Score': 85},
            {'Name': 'Jack',
             'Class': 'Chemistry',
             'Score': 82},
            {'Name': 'Helen',
             'Class': 'Biology',
             'Score': 90}]

Prob32 = pd.DataFrame(Prob31, index=['school1', 'school2', 'school1'])
print ("Topic Q3.1:","\n", Prob32)  
print("\n")

Prob33 = Prob32.rename(mapper = lambda x: x.upper(), axis=1, inplace = True)
print ("Topic Q3.3:","\n", Prob33)  
print("\n")
#Doubts!!

#Problem #4 <--WINNER 
Prob41 = [{'Name': 'Alice',
              'Class': 'Physics',
              'Score': 85},
            {'Name': 'Jack',
             'Class': 'Chemistry',
             'Score': 82},
            {'Name': 'Helen',
             'Class': 'Biology',
             'Score': 90}]

Prob42 = pd.DataFrame(Prob41, index=['school1', 'school2', 'school1'])
print ("Topic Q4.1:","\n", Prob42)  
print("\n")
Prob43 =Prob42[Prob42['Score'] > 84]
print ("Topic Q4.2:","\n", Prob43)  
print("\n")
Prob44 = Prob42.where(Prob42['Score'] > 84)
print ("Topic Q4.3:","\n", Prob44)  
print("\n")
Prob45 = Prob42.where(Prob42['Score'] > 84).dropna()
print ("Topic Q4.4:","\n", Prob45)  
print("\n")

#Problem #5 <--WINNER 
#OK

#Problem #6 <--WINNER 
Prob61 = [{'Name': 'Alice',
              'Class': 'Physics',
              'Score': 85},
            {'Name': 'Jack',
             'Class': 'Chemistry',
             'Score': 82},
            {'Name': 'Helen',
             'Class': 'Biology',
             'Score': 90}]

Prob62 = pd.DataFrame(Prob61, index=['school1', 'school2', 'school3'])
print ("Topic Q6.1:","\n", Prob62)  
print("\n")
Prob63 = Prob62.drop('school1')
print ("Topic Q6.2:","\n", Prob63)  
print("\n")
Prob64 = Prob62.drop('Name', axis = 1)
print ("Topic Q6.3:","\n", Prob64)  
print("\n")
Prob65 = Prob62.drop('Name')
print ("Topic Q6.4:","\n", Prob65)  
print("\n")
Prob66 = Prob62.drop(['school2', 'school3'])
print ("Topic Q6.5:","\n", Prob66)  
print("\n")

#Problem #7 <--WINNER 
Prob71 = pd.Series({1: 'Alice', 2: 'Jack', 3: 'Molly'})
Prob72 = pd.Series({'Alice': 1, 'Jack': 2, 'Molly': 3})
Prob73 = Prob71.loc[1]
print ("Topic Q7.1:","\n", Prob73)  
print("\n")
Prob74 = Prob72.loc[1]
print ("Topic Q7.1:","\n", Prob74)  
print("\n")
Prob75 = Prob72[1]
print ("Topic Q7.1:","\n", Prob75)  
print("\n")
Prob76 = Prob72.iloc[1]
print ("Topic Q7.1:","\n", Prob76)  
print("\n")

#Problem #8 <--WINNER 
#OK

#Problem #9 <--WINNER 
Prob81 = [{'Name': 'Alice',
              'Class': 'Physics',
              'Score': 85},
            {'Name': 'Jack',
             'Class': 'Chemistry',
             'Score': 82},
            {'Name': 'Helen',
             'Class': 'Biology',
             'Score': 90}]
Prob82 = pd.DataFrame(Prob81, index=['school1', 'school2', 'school3'])
print ("Topic Q8.1:","\n", Prob82)  
print("\n")
Prob83 = ((Prob82['Score'] > 83) & (Prob82['Score'] < 87))
print ("Topic Q8.2:","\n", Prob83)  
print("\n")
Prob84 = Prob82[(Prob82['Score'].isin(range(83, 87)))]
print ("Topic Q8.3:","\n", Prob84)  
print("\n")
Prob85 = Prob82[Prob82['Score'].gt(83) & Prob82['Score'].lt(87)]
print ("Topic Q8.5:","\n", Prob85)  
print("\n")
Prob86 = Prob82[(Prob82['Score'] > 83) & (Prob82['Score'] < 87)]
print ("Topic Q8.6:","\n", Prob86)  
print("\n")

#Problem #10 <--WINNER 
Prob101 = [{'Name': 'Alice',
              'Class': 'Physics',
              'Score': 85},
            {'Name': 'Jack',
             'Class': 'Chemistry',
             'Score': 82},
            {'Name': 'Helen',
             'Class': 'Biology',
             'Score': 90}]
Prob102 = pd.DataFrame(Prob101, index=['school1', 'school2', 'school3'])
print ("Topic Q10.1:","\n", Prob102)  
print("\n")
Prob103 = Prob102.T['school1']
print ("Topic Q10.2:","\n", Prob103)  
print("\n")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#Assignment 2 - September 16, 2020 (RMDLC)

import pandas as pd
import numpy as np
import re

#PROB #1             
Assig21 =pd.read_csv("olympics.csv")
print ("Assigment 2 Data:","\n", Assig21)  
print("\n")

#We are going to skip a row (only the row "1") and assign as a index the...
#...column "0" of my dataframe.

#In the case of "to skip row" (one of the arguments of the code "read_csv")..
#...we need to say the following: 
    #skiprows: Line numbers to skip while reading "csv file".
        #If it’s an "int" then skip that lines from top
        #If it’s a "list of int" then skip lines at those index positions
        #If it’s a "callable function" then pass each index to this function...
        #...to check if line to skipped or not.
    #It will read the given csv file by skipping the specified lines and...
    #...load remaining lines to a dataframe.

Assig23 = pd.read_csv("olympics.csv", index_col=0, skiprows=1)
print (Assig23)

#We are going to rename some of the columns of my dataframe through...
#...a slicing range along the columns 
for col in Assig23.columns:
    if col[:2] == "01":
        Assig23.rename(columns={col:"Gold"+col[4:]}, inplace=True)
    if col[:2] == "02":
        Assig23.rename(columns={col:"Silver"+col[4:]}, inplace=True)
    if col[:2] == "03":
        Assig23.rename(columns={col:"Bronze"+col[4:]}, inplace=True)
    if col[:1] == "":
        Assig23.rename(columns={col:"#"+col[1:]}, inplace=True)

#Split the index by "("
  #We can apply the code "split" (to a string) to separate a string into...
  #...substrings .
  
  #"split": returns a word, certain words or all the words that belong to...
  #...a string. 
  
  #In this case we are looking for a string separate by a blank space...
  #...and after that blank space is located a parentheses.
names_ids = Assig23.index.str.split("\s\(")

#The [0] element inside the index is the "country name" (this work very well...
#...after the split that we have done previously); therefore, we have just...
#...created a new index only with the "country name".
Assig23.index = names_ids.str[0] 

#The [1] element inside the index is the "abbreviation or ID" (this work very...
#...well after the split that we have done previously) take first 3...
#...characters from that abbreviation and put them in a new column called "ID".
Assig23["ID"] = names_ids.str[1].str[:3] 

#Drop the column "Totals"
Assig23 = Assig23.drop("Totals")

#Print only the head of the edited dataframe.
Assig24 = Assig23.head()                                   
print (Assig24)                               

#1.0.1 Question 0 (Example)                         
#What is the ﬁrst country in df?

#You should write your whole answer within the function provided....
#...The autograder will call this function and compare the return value...
#...against the correct solution value.

#This function returns the row for Afghanistan, which is a Series object...
#...The assignment question description will tell you the general format...
#...the autograder is expecting

# <--WINNER (Option with function)
def answer_zero():
    return Assig23.iloc[0]

answer_zero()                             
                     
#1.0.2 Question 1 <--WINNER (Option with function)
#Which country has won the most gold medals in summer games?
#This function should return a single string value.
                   
#Story:
    #1.We create a copy of the original database (transformed previously).
    #2.We remove the index and put it at the end of the dataframe.
    #3.We put as a new index the column "Gold" of Summer Games.
    #4.We sort the index "Gold" in a descending way and also establish this...
    #...modification as "True" in the dataframe.
    #5.Finally, choose the cell that belong to the first row and last column.

def answer_one(): 
    Assig24 = Assig23.copy()
    Assig24["States"] = Assig24.index
    Assig24 = Assig24.set_index("Gold")
    Assig24.sort_index(ascending=False, inplace=True)
    return Assig24.iloc[0,-1]

answer_one()

#1.0.3 Question 2 <--WINNER (Option with function)
#Which country had the biggest difference between their summer and winter...
#...gold medal counts?
#This function should return a single string value.

#Story:
    #1.We create a copy of the original database (transformed previously).
    #2.We remove the index and put it at the end of the dataframe.
    #3.We create a new column "Difference Gold" to show the difference...
    #...between the columns of "Gold" and "Gold.1"
    #4.We put as a new index the column "Difference Gold" 
    #5.We sort the index "Difference Gold" in a descending way and also 
    #...establish this modification as "True" in the dataframe.
    #6.Finally, choose the cell that belong to the first row and last column.
    
def answer_two(): 
    Assig25 = Assig23.copy()
    Assig25["States"] = Assig25.index
    Assig25["Difference Gold"] = abs(Assig25["Gold"] - Assig25["Gold.1"])
    Assig25 = Assig25.set_index("Difference Gold")
    Assig25.sort_index(ascending=False, inplace=True)
    return Assig25.iloc[0,-1]

answer_two()    
       
#1.0.4 Question 3 <--WINNER (Option with function)
#Which country has the biggest difference between their summer gold medal...
#...counts and winter gold medal counts relative to their total gold medal...
#...count?

#(Summer Gold − Winter Gold)/Total Gold

#Only include countries that have won at least 1 gold in both summer and winter.
#This function should return a single string value.

#Story:
    #1.We create a copy of the original database (transformed previously).
    #2.We remove the index and put it at the end of the dataframe.
    #3.We create a new column "Relative Gold" to show the difference...
    #...between the columns of ("Gold" and "Gold.1" / "Gold.2")
    #4.We put as a new index the column "Difference Gold" 
    #5.We sort the index "Relative Gold" in a descending way and also 
    #...establish this modification as "True" in the dataframe.
    #6.Then we filter the columns "Gold" and "Gold.1" to get only those...
    #...rows with values greater than zero.
    #7.We drop all the rows that do not followthe rule establish in the...
    #...point 6.
    #6.Finally, choose the cell that belong to the first row and last column.
    
def answer_three(): 
    Assig26 = Assig23.copy()
    Assig26["States"] = Assig26.index
    Assig26["Relative Gold"] = abs((Assig26["Gold"] - Assig26["Gold.1"])/Assig26["Gold.2"])
    Assig26 = Assig26.set_index("Relative Gold")
    Assig26.sort_index(ascending=False, inplace=True)
    Assig261 = (Assig26['Gold'] >0) & (Assig26['Gold.1'] >0)
    Assig262 = Assig26.where(Assig261).dropna()   
    return Assig262.iloc[0,-1]

answer_three()                                                                       
                                                     
#1.0.5 Question 4 <--WINNER (Option with function)

#Write a function that creates a Series called "Points" which is a...
#...weighted value where each gold medal (Gold.2) counts for 3 points,...
#... silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2)..
#...for 1 point. The function should return only the column (a Series object)...
#...which you created, with the country names as indices.

#This function should return a Series named Points of length 146

#Story:
    #1.We create a copy of the original database (transformed previously).
    #2.We create new columns called:
        #"Points Gold.2"
        #"Points Silver.2"
        #"Points Bronze.2"
        #"Points"
    #6.Finally, I create a list with the column "Points" (automatically the...
    #...same index that we have in the dataframe [countries names] is passed...
    #...to the Serie).

def answer_four(): 
    Assig27 = Assig23.copy()
    Assig27["Points Gold.2"] = 3*(Assig27["Gold.2"])
    Assig27["Points Silver.2"] = 2*(Assig27["Silver.2"])
    Assig27["Points Bronze.2"] = 1*(Assig27["Bronze.2"])
    Assig27["Points"] = Assig27["Points Gold.2"] + Assig27["Points Silver.2"] + Assig27["Points Bronze.2"]  
    return pd.Series(Assig27["Points"])

answer_four()                               

#1.1 Part 2 <--WINNER (Option with function)
#For the next set of questions, we will be using census data from the United..
#...States Census Bureau. 

#Counties are political and geographic subdivisions..
#...of states in the United States. This dataset contains population data...
#...for counties and states in the US from 2010 to 2015. See this document...
#...for a description of the variable names.

#The census dataset (census.csv) should be loaded as census_df. Answer...
#...questions using this as appropriate.

#1.1.1 Question 5 <--WINNER (Option with function)
#Which state has the most counties in it? (hint: consider the sumlevel...
#...key carefully! You’ll need this for future questions too...) This...
#...function should return a single string value.

#Story:
    #1.We create a copy of the original database (transformed previously).
    #2.We apply a filter using SUMLEV = 50, because in this way we eliminate..
    #...the name of the states that are not counties.
    #3.Then we use a counter of elements that are repeated in only one...
    #...column. This counter show me the name of the element and the....
    #...times it appear.
    #4.I order the values of this serie (to be specific of the number of...
    #...repetitions) from highest to lowest.
    #6.Finally, I print the index (name of the state) of the highest value.

census_df = pd.read_csv("census.csv")
census_df.head()           
                         
def answer_five():
    Assig28 = census_df.copy()
    Assig281 = Assig28[Assig28['SUMLEV'] == 50]
    Assig282 = Assig281.pivot_table(columns=["STNAME"], aggfunc='size')
    Assig283 = Assig282.sort_values(ascending=False)
    return Assig283.index[0] 

answer_five() 

#1.1.2 Question 6 <--WINNER (Option with function)

#Only looking at the three most populous counties for each state, what are...
#...the three most populous states (in order of highest population to...
#...lowest population)? Use CENSUS2010POP. This function should return a...
#...list of string values.

#Story:
    #Part 1:
    #1.We create a copy of the original database (transformed previously).
    #2.We apply a filter using SUMLEV = 50, because in this way we eliminate..
    #...the name of the states that are not counties.
    #3.We keep the most important columns.
    #4.I sort the values of this dataframe (to be specific of the column...
    #..."CENSUS2010POP") from highest to lowest.
    #5.I applied a filter in the sorted column  of "CENSUS2010POP" to keep...
    #...only the top 20 values (which I know contain the 3 counties of the...
    #...3 states of most populated).
    
    #Part2:
    #6.Then I create 3 separates dataframes (extracted from the dataframe..
    #...created in the Part 1 - Point 5), each one represent thee 3 top...
    #...states with the 3 top counties (in population) in which I reset the...
    #...index a filter only selection the 3 top rows.
    #7.I concatenate (join vertically) the 3 separates dataframes...
    #...created in the Part 2 - Point 6).
    #8.Then I delete an unnecessary column, sort the column of population,...
    #...transform the Dataframe in Serie and then the Serie in a List.
    #9.Finally, I print the list (with name of the state) from the highest...
    #...to the lowest value.

census_df = pd.read_csv("census.csv")
census_df.head()           

def answer_six():                 
    Assig29 = census_df.copy()
    Assig291 = Assig29[Assig29['SUMLEV'] == 50]
    columns_to_keep = ["STNAME","CTYNAME","CENSUS2010POP"]
    Assig292 = Assig291[columns_to_keep]
    Assig293 = Assig292.sort_values(by=['CENSUS2010POP'],ascending=False)
    Assig294 = Assig293[Assig293['CENSUS2010POP'] >= 1585873]
    
    #California
    Assig295 = Assig294[Assig294['STNAME'] == "California"]
    Assig295 = Assig295.reset_index()
    Assig296 = Assig295.iloc[0:3]
    
    #Texas
    Assig297 = Assig294[Assig294['STNAME'] == "Texas"]
    Assig297 = Assig297.reset_index()
    Assig298 = Assig297.iloc[0:3]
    
    #New York
    Assig299 = Assig294[Assig294['STNAME'] == "New York"]
    Assig299 = Assig299.reset_index()
    Assig300 = Assig299.iloc[0:3]
    
    #Concatenate
    Assig301 = [Assig296, Assig298, Assig300]
    Assig302 = pd.concat(Assig301)
    
    #Fixing Index and delete de column "index"
    del Assig302['index']
    Assig304 = Assig302.sort_values(by=['CENSUS2010POP'],ascending=False)
    Assig305 = pd.Series(Assig304["STNAME"])
    Assig306 = Assig305.tolist()
    return Assig306

answer_six() 


#1.1.3 Question 7 <--WINNER (Option with function)

import pandas as pd
import numpy as np
import re

#Which county has had the largest absolute change in population within...
#...the period 2010-2015? (Hint: population values are stored in columns...
#...POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six....
#...columns.) E.g. If County Population in the 5 year period is 100, 120, 80,...
#...105, 100, 130, then its largest change in the period would be |130-80| = 50.
#This function should return a single string value.

#Story:
    #1.We create a copy of the original database (transformed previously).
    #2.We apply a filter using SUMLEV = 50, because in this way we eliminate..
    #...the name of the states that are not counties.
    #3.We keep the most important columns.
    #4.I find the maximun and the minimun value per row and create columns...
    #....at the end of the dataframe to put them.
    #5.Then I create a new column in te dataframe to store the difference...
    #...(i.e. the column "Assig309['Difference']").
    #6.I sorted the values of the column "Assig309['Difference']" to find...
    #...the county with the greatest difference.
    #7. Finally, I print in a string format the county with the greatest...
    #...difference in population.

census_df = pd.read_csv("census.csv")
census_df.head()           

def answer_seven():                 
    Assig307 = census_df.copy()
    Assig308 = Assig307[Assig307['SUMLEV'] == 50]
    columns_to_keep = ["STNAME","CTYNAME","POPESTIMATE2010","POPESTIMATE2011","POPESTIMATE2012","POPESTIMATE2013","POPESTIMATE2014","POPESTIMATE2015"]
    Assig309 = Assig308[columns_to_keep]
    Assig309['max_value'] = Assig309.max(axis=1)
    Assig309['min_value'] = Assig309.min(axis=1)
    Assig309['Difference'] = Assig309['max_value'] - Assig309['min_value']
    Assig309 = Assig309.sort_values(by=['Difference'],ascending=False)
    return Assig309.iloc[0,1]

answer_seven() 


#1.1.4 Question 8 <--WINNER (Option with function)
#In this dataﬁle, the United States is broken up into four regions using the...
#..."REGION" column. Create a query that ﬁnds the counties that belong to...
#...regions 1 or 2, whose name starts with ’Washington’, and whose...
#...POPESTIMATE2015 was greater than their POPESTIMATE 2014. This function...
#...should return a 5x2 DataFrame with the columns = [’STNAME’, ’CTYNAME’]...
#...and the same index ID as the census_df (sorted ascending by index).    
                                           
#Story:
    #1.We create a copy of the original database (transformed previously).
    #2.We apply a filter using SUMLEV = 50, because in this way we eliminate..
    #...the name of the states that are not counties.
    #3.We keep the most important columns.
    #4.I applied a filter to keep only the rows with the REGION "1" and "2".
    #5.Then I calculate the difference between ["POPESTIMATE2015"] and...
    #...["POPESTIMATE2014"] and store that difference in a new column of the....
    #...dataframe
    #6.I sorted the values of the column "Assig314['Differ8']".
    #7.I drop all the values that are less than one in the...
    #... column "Assig314['Differ8']".
        #"df[].index" selects the index of rows which passes the condition.
    #8.I apply a filter to the column Assig314['CTYNAME'] to find all...
    #...the counties that start with the string "Washington".
    #9.We keep the most important columns again.
    #10.Finally, I print the final dataframe.
    
census_df = pd.read_csv("census.csv")
census_df.head()           

def answer_eight():                 
    
    Assig310 = census_df.copy()
    Assig311 = Assig310[Assig310['SUMLEV'] == 50]  
    columns_to_keep = ["REGION","STNAME","CTYNAME","POPESTIMATE2014","POPESTIMATE2015"]
    Assig312 = Assig311[columns_to_keep]      
    Assig313 = Assig312[Assig312['REGION'] <=2]
    Assig313["Differ8"] = Assig313["POPESTIMATE2015"] - Assig313["POPESTIMATE2014"]
    Assig314 = Assig313.sort_values(by=['Differ8'],ascending=False)
    Assig314.drop(Assig314[(Assig314['Differ8'] < 1)].index, inplace=True)
    Assig315 = Assig314.loc[(Assig314['CTYNAME'].str.startswith('Washington'))]
    columns_to_keep2 = ["STNAME","CTYNAME"]
    Assig316 = Assig315[columns_to_keep2]
    return Assig316
    
answer_eight() 


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#############################################################################
#Topics to review
    #What is the difference between "Null", "NaN" and "None" in Python, Numpy...
    #...and Pandas.
    #Vectorization instead of iterative loops
    #Parallel?
    #Use of code "isin(range(898,88999))
    #Meaning of "inplace:True / False" code
    #hash tables
    #how to download data from Jupyter Notebook (GitHub) and transform it from...
    #...CSV to MS EXCEL.
    #In what way we make code to run faster than other in Python or with Pandas..
    #...and Numpy.




























