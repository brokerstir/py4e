'''
Zip lists to build a DataFrame
In this exercise, you're going to make a pandas DataFrame of the top three countries to win gold medals since 1896 by first building a dictionary. list_keys contains the column names 'Country' and 'Total'. list_values contains the full names of each country and the number of gold medals awarded. The values have been taken from Wikipedia.
Your job is to use these lists to construct a list of tuples, use the list of tuples to construct a dictionary, and then use that dictionary to construct a DataFrame. In doing so, you'll make use of the list(), zip(), dict() and pd.DataFrame() functions. Pandas has already been imported as pd.
Note: The zip() function in Python 3 and above returns a special zip object, which is essentially a generator. To convert this zip object into a list, you'll need to use list(). You can learn more about the zip() function as well as generators in Python Data Science Toolbox (Part 2).
'''

'''
Zip the 2 lists list_keys and list_values together into one list of (key, value) tuples. Be sure to convert the zip object into a list, and store the result in zipped.
Inspect the contents of zipped using print(). This has been done for you.
Construct a dictionary using zipped. Store the result as data.
Construct a DataFrame using the dictionary. Store the result as df.
'''

# Zip the 2 lists together into one list of (key,value) tuples: zipped
zipped = list(zip(list_keys, list_values))

# Inspect the list using print()
print(zipped)

# Build a dictionary with the zipped list: data
data = dict(zipped)

# Build and inspect a DataFrame from the dictionary: df
df = pd.DataFrame(data)
print(df)


'''
Labeling your data
You can use the DataFrame attribute df.columns to view and assign new string labels to columns in a pandas DataFrame.
In this exercise, we have imported pandas as pd and defined a DataFrame df containing top Billboard hits from the 1980s (from Wikipedia). Each row has the year, artist, song name and the number of weeks at the top. However, this DataFrame has the column labels a, b, c, d. Your job is to use the df.columns attribute to re-assign descriptive column labels.
'''

'''
Create a list of new column labels with 'year', 'artist', 'song', 'chart weeks', and assign it to list_labels. 
Assign your list of labels to df.columns.
'''

# Build a list of labels: list_labels
list_labels = ['year', 'artist', 'song', 'chart weeks']

# Assign the list of labels to the columns attribute: df.columns
df.columns = list_labels


'''
Building DataFrames with broadcasting
You can implicitly use 'broadcasting', a feature of NumPy, when creating pandas DataFrames. In this exercise, you're going to create a DataFrame of cities in Pennsylvania that contains the city name in one column and the state name in the second. We have imported the names of 15 cities as the list cities.
Your job is construct a DataFrame from the list of cities and the string 'PA'.
'''

'''
Make a string object with the value 'PA' and assign it to state.
Construct a dictionary with 2 key:value pairs: 'state':state and 'city':cities.
Construct a pandas DataFrame from the dictionary you created and assign it to df.
'''

# Make a string with the value 'PA': state
state = 'PA'

# Construct a dictionary: data
data = {'state':state, 'city':cities}

# Construct a DataFrame from dictionary data: df
df = pd.DataFrame(data)

# Print the DataFrame
print(df)


'''
The next step is to reread the same file, but simultaneously rename the columns using the names keyword input parameter, set equal to a list of new column labels. You will also need to set header=0 to rename the column labels.
Finish up by inspecting the result with df.head() and df.info() in the IPython Shell. 
pandas has already been imported and is available in the workspace as pd.
'''

'''
Use pd.read_csv() with the string 'world_population.csv' to read the CSV file into a DataFrame and assign it to df1.
Create a list of new column labels - 'year', 'population' - and assign it to the variable new_labels.
Reread the same file, again using pd.read_csv(), but this time, add the keyword arguments header=0 and names=new_labels. Assign the resulting DataFrame to df2.
Print both the df1 and df2 DataFrames to see the change in column names. This has already been done for you.
'''

# Read in the file: df1
df1 = pd.read_csv('world_population.csv')

# Create a list of the new column labels: new_labels
new_labels = ['year', 'population']

# Read in the file, specifying the header and names parameters: df2
df2 = pd.read_csv('world_population.csv', header=0, names=new_labels)

# Print both the DataFrames
print(df1)
print(df2)

'''
Delimiters, headers, and extensions
Not all data files are clean and tidy. Pandas provides methods for reading those not-so-perfect data files that you encounter far too often.
In this exercise, you have monthly stock data for four companies downloaded from Yahoo Finance. The data is stored as one row for each company and each column is the end-of-month closing price. The file name is given to you in the variable file_messy.
In addition, this file has three aspects that may cause trouble for lesser tools: multiple header lines, comment records (rows) interleaved throughout the data rows, and tab delimiters instead of commas.
Your job is to use pandas to read the data from this problematic file_messy using non-default input options with read_csv() so as to tidy up the mess at read time. Then, write the cleaned up data to a CSV file with the variable file_clean that has been prepared for you, as you might do in a real data workflow.
You can learn about the option input parameters needed by using help() on the pandas function pd.read_csv().
'''

'''
Use pd.read_csv() without using any keyword arguments to read file_messy into a pandas DataFrame df1.
Use .head() to print the first 5 rows of df1 and see how messy it is. Do this in the IPython Shell first so you can see how modifying read_csv() can clean up this mess.
Using the keyword arguments delimiter=' ', header=3 and comment='#', use pd.read_csv() again to read file_messy into a new DataFrame df2.
Print the output of df2.head() to verify the file was read correctly.
Use the DataFrame method .to_csv() to save the DataFrame df2 to the variable file_clean. Be sure to specify index=False.
Use the DataFrame method .to_excel() to save the DataFrame df2 to the file 'file_clean.xlsx'. Again, remember to specify index=False.
'''

# Read the raw file as-is: df1
df1 = pd.read_csv(file_messy)

# Print the output of df1.head()
print(df1.head())

# Read in the file with the correct parameters: df2
df2 = pd.read_csv(file_messy, delimiter=' ', header=3, comment='#')

# Print the output of df2.head()
print(df2.head())

# Save the cleaned up DataFrame to a CSV file without the index
df2.to_csv(file_clean, index=False)

# Save the cleaned up DataFrame to an excel file without the index
df2.to_excel('file_clean.xlsx', index=False)


'''
Plotting DataFrames
Comparing data from several columns can be very illuminating. Pandas makes doing so easy with multi-column DataFrames. By default, calling df.plot() will cause pandas to over-plot all column data, with each column as a single line. In this exercise, we have pre-loaded three columns of data from a weather data set - temperature, dew point, and pressure - but the problem is that pressure has different units of measure. The pressure data, measured in Atmospheres, has a different vertical scaling than that of the other two data columns, which are both measured in degrees Fahrenheit. 
Your job is to plot all columns as a multi-line plot, to see the nature of vertical scaling problem. Then, use a list of column names passed into the DataFrame df[column_list] to limit plotting to just one column, and then just 2 columns of data. When you are finished, you will have created 4 plots. You can cycle through them by clicking on the 'Previous Plot' and 'Next Plot' buttons. 
As in the previous exercise, inspect the DataFrame df in the IPython Shell using the .head() and .info() methods.
'''

'''
Plot all columns together on one figure by calling df.plot(), and noting the vertical scaling problem.
Plot all columns as subplots. To do so, you need to specify subplots=True inside .plot().
Plot a single column of dew point data. To do this, define a column list containing a single column name 'Dew Point (deg F)', and call df[column_list1].plot().
Plot two columns of data, 'Temperature (deg F)' and 'Dew Point (deg F)'. To do this, define a list containing those column names and pass it into df[], as df[column_list2].plot().
'''

# Plot all columns (default)
df.plot()
plt.show()

# Plot all columns as subplots
df.plot(subplots=True)
plt.show()

# Plot just the Dew Point data
column_list1 = ['Dew Point (deg F)']
df[column_list1].plot()
plt.show()

# Plot the Dew Point and Temperature data, but not the Pressure data
column_list2 = ['Temperature (deg F)','Dew Point (deg F)']
df[column_list2].plot()
plt.show()
