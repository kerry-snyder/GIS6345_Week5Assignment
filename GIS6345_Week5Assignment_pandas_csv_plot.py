import pandas as pd

#Read the csv file containing eBird data
birds = pd.read_csv("MyEBirdData.csv")

#Display the first 10 rows of data
DataFrame = birds
DataFrame.head(10)

#Plot of the number of times each bird (by common name) appears in the data
df = pd.DataFrame(birds)
df['Common Name'].value_counts().plot(kind='bar')

#Plot of the number of lists that come from each U.S. County represented
df = pd.DataFrame(birds)
df['County'].value_counts().plot(kind='bar')

#Plot of the distance traveled on each day that data were collected
df = pd.DataFrame(birds)
df.plot.barh(x ='Date', y='Distance Traveled (km)', rot=0)

#Reads a csv file filtered down to one day of birding 
birds = pd.read_csv("MyEBirdData_Filtered.csv")

#Plot of the number of species individuals (by common name) was seen one one day
df = pd.DataFrame(birds)
df['Common Name'].value_counts().plot(kind='bar')

#Plot of the distance traveled for the eBird lists in which each bird (by common name) was seen
df = pd.DataFrame(birds)
df.plot.barh(x ='Common Name', y='Distance Traveled (km)', rot=0)
