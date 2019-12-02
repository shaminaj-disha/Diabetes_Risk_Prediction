def transHeight(x):
    if x == '5 feet 10 inch' or x == '5′ 10″' or x == "5'10''" or x == '5\'10"':
        return 1.778
    elif x == '5\'3"' or x == "5'3''" or x == '5.3':
        return 1.6002
    elif x == "5'8''" or x == "5'8" or x == '5.8' or x == '5\'8"' or x == '5 feet 8 inch' or x == '172.72 cm':
        return 1.7272
    elif x == '5.6' or x == '5.6 feet' or x == '5\'6"' or x == "5'6''":
        return 1.6764
    elif x == '6 feet' or x == '6.0"':
        return 1.8288
    elif x == '5.5' or x == "5''5'" or x == '5\'5"' or x == "5'5''" or x == '5 feet 5 inch':
        return 1.651
    elif x == '5\' 9"' or x == "5''9'" or x == "5' 9''" or x == '5.9' or x == '5feet 9 inch':
        return 1.7526
    elif x == '5.11' or x == '5 feet 11 inch':
        return 1.8034
    elif x == '5 feet 10.5 inch':
        return 1.7907
    elif x == '5.2' or x == "5'2''" or x == '5\'2"':
        return 1.5748
    elif x == '5.75':
        return 1.7145
    elif x == '5.7' or x == '5 feet 7 inch' or x == '170.18 cm':
        return 1.7018
    elif x == '5\'4"' or x == '5.4' or x == '5 feet 4 inch' or x == "5'4''":
        return 1.6256
    elif x == "5'1" or x == '5.1':
        return 1.5494
    elif x == '161.544':
        return 1.61544
    elif x == '4.1':
        return 1.2446
    elif x == '6 feet 1 inch' or x == "6'1''":
        return 1.8542
    elif x == "4'11''":
        return 1.4986

def transBMI(x):
    if x < 18.5:
        return 2
    elif x >= 18.5 and x < 25:
        return 1
    elif x >= 25 and x < 30:
        return 2
    elif x >= 30:
        return 3

def transDiabetic(x):
    if x == 0:
        return 1
    elif x == 1:
        return 2
    elif x == 2 or x == 3:
        return 3
    elif x == 4 or x == 5:
        return 4

def transNegetive(x):
    if x == 1:
        return 3
    elif x == 2:
        return 2
    elif x == 3:
        return 1

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_xls = pd.read_excel('Extended_version_2.csv.xlsx',index_col=None)
data_xls.to_csv('EXTENDED_2.csv',encoding='utf-8',index=False)

data_xls = pd.read_excel('Extended_version_3.csv.xlsx',index_col=None)
data_xls.to_csv('EXTENDED_3.csv',encoding='utf-8',index=False)

dataframe1 = pd.read_csv("DATASET_1.csv")
dataframe2 = pd.read_csv("DATASET_2.csv")
dataframe3 = pd.read_csv("DATASET_3.csv")
dataframe4 = pd.read_csv("DATASET_4.csv")
dataframe5 = pd.read_csv("DATASET_5.csv")
dataframe6 = pd.read_csv("DATASET_6.csv")

dataframe1.columns = ['ID', 'Current Place', 'Latitude', 'Longitude', 'Place of interest', 
                      'Latitude.1', 'Longitude.1', 'Food you like most', 'Leisure time activity','Future plan', 
                      'Typically your days are started at']
dataframe2.columns = ['ID', 'Current Place', 'Latitude', 'Longitude', 'Place of interest', 
                      'Latitude.1', 'Longitude.1', 'Food you like most', 'Leisure time activity','Future plan', 
                      'Typically your days are started at']
dataframe3.columns = ['ID', 'Current Place', 'Latitude', 'Longitude', 'Place of interest', 
                      'Latitude.1', 'Longitude.1', 'Food you like most', 'Leisure time activity','Future plan', 
                      'Typically your days are started at']
dataframe4.columns = ['ID', 'Current Place', 'Latitude', 'Longitude', 'Place of interest', 
                      'Latitude.1', 'Longitude.1', 'Food you like most', 'Leisure time activity','Future plan', 
                      'Typically your days are started at']
dataframe5.columns = ['ID', 'Current Place', 'Latitude', 'Longitude', 'Place of interest', 
                      'Latitude.1', 'Longitude.1', 'Food you like most', 'Leisure time activity','Future plan', 
                      'Typically your days are started at']
dataframe6.columns = ['ID', 'Current Place', 'Latitude', 'Longitude', 'Place of interest', 
                      'Latitude.1', 'Longitude.1', 'Food you like most', 'Leisure time activity','Future plan', 
                      'Typically your days are started at']


dataframe1.drop(0, axis = 0, inplace = True)
dataframe2.drop(0, axis = 0, inplace = True)
dataframe3.drop(0, axis = 0, inplace = True)
dataframe4.drop(0, axis = 0, inplace = True)
dataframe5.drop(0, axis = 0, inplace = True)
dataframe6.drop(0, axis = 0, inplace = True)

dataframe = pd.concat([dataframe1, dataframe2, dataframe3, 
                       dataframe4, dataframe5, dataframe6], ignore_index = True, sort = True)

dataframe['ID'] = dataframe['ID'].astype(np.int64)

dataframeEx1 = pd.read_csv("EXTENDED_1.csv")
dataframeEx2 = pd.read_csv("EXTENDED_2.csv")
dataframeEx3 = pd.read_csv("EXTENDED_3.csv")

dataframeEx1 = dataframeEx1.drop(['Timestamp','Score','Unnamed: 25'],axis=1)
dataframeEx2 = dataframeEx2.drop(['Timestamp','Total score'],axis=1)
dataframeEx2Temp = pd.DataFrame(dataframeEx2.iloc[:,0:54:3].values)
dataframeEx2Temp.columns = ['ID','Trying better than expected','Return more change','Not worrying about public affairs',
                            'Book lover','Book store in your area','Blood Group','Introvert or Extrovert','Concerned about life',
                            'Work time per day','Game time per day','Budget for laptop','Guilty for relaxation','Need to win to derive enjoyment',
                            'Trying more than once','Wait in line(Frustration)','Morning person','Perfectionist']


dataframeEx2 = dataframeEx2Temp
dataframeEx3 = dataframeEx3.drop(['Timestamp','Total score'],axis=1)
dataframeEx3Temp = pd.DataFrame(dataframeEx3.iloc[:,0:72:3].values)
dataframeEx3Temp.columns = ['ID','Breakfast','Tuition','Spent Childhood','Favourite Destination',
                            'Proper diet','Frequently eat fast food','Exercise','Spend on meal',"Diabetic",
                            "BP","Waist","Depression","Insecurity",
                            "Patiency","Confidence","Helpful","Song","Anger",'iPhone or smartphone',
                            'Look does not matter','Mobile games','favorite mobile game genre','Study time']
dataframeEx3 = dataframeEx3Temp


dataframeEx2['ID'] = dataframeEx2['ID'].astype(np.int64)
dataframeEx3['ID'] = dataframeEx3['ID'].astype(np.int64)


dataframeMergeTemp = pd.merge(dataframeEx1, dataframeEx2, on = "ID", how = "outer")
dataframeMerge = pd.merge(dataframeMergeTemp, dataframeEx3, on = "ID", how = "outer")
dataframeMerge.sort_values(by=['ID'])

dataset = pd.merge(dataframe, dataframeMerge, on = "ID", how = "outer")
dataset = dataset.sort_values(by=['ID'])

dataset.to_csv('D:/Codes/Python/Pattern Lab/Fahim Lab Final/Pattern Final/Dataset.csv')


column_name_dataset = ['ID','Height','Weight',"Diabetic","BP","Depression",
                   "Insecurity","Patiency","Confidence","Helpful","Song","Anger"]

mydataset = dataset[column_name_dataset]

mydataset['ID'] = mydataset['ID'].astype('object')
mydataset['Weight'] = mydataset['Weight'].astype('object')
str_cols = mydataset.select_dtypes(['object']).columns
mydataset_test = mydataset[str_cols].replace({'Yes':'3','No':'1','Maybe':'2','Normal':'1','Low':'2','High':'3'})
mydataset_test = mydataset_test.dropna()

mydataset_test=mydataset_test.replace(r'ft', 'feet', regex=True)
mydataset_test=mydataset_test.replace(r'inches', 'inch', regex=True)
mydataset_test=mydataset_test.replace(r'CM', 'cm', regex=True)

mydataset_test['Height'].unique()


mydataset_test['Height'] = mydataset_test['Height'].apply(transHeight)
mydataset_test['BMI'] = mydataset_test['Weight']/(mydataset_test['Height']*mydataset_test['Height'])


mydataset_test['BMI'] = mydataset_test['BMI'].apply(transBMI)
mydataset_test['Diabetic'] = mydataset_test['Diabetic'].apply(transDiabetic)

Diabetic_dataset = mydataset_test[['ID','BMI','Depression','Diabetic','BP']]

Diabetic_dataset['ID'] = Diabetic_dataset['ID'].astype(np.int64)
Diabetic_dataset['Depression'] = Diabetic_dataset['Depression'].astype(np.int64)
Diabetic_dataset['BP'] = Diabetic_dataset['BP'].astype(np.int64)
dia_str_cols = Diabetic_dataset.select_dtypes(['object']).columns
Diabetic_dataset[dia_str_cols] = Diabetic_dataset[dia_str_cols].astype(np.int64)


Diabetic_dataset['Diabetic_Prediction'] = (Diabetic_dataset['BMI']*35 + Diabetic_dataset['Depression']*25 + 
                Diabetic_dataset['Diabetic']*30 + Diabetic_dataset['BP']*10)/325

                
High_Dia = 0
Low_Dia = 0
Medium_Dia = 0

for i, x in Diabetic_dataset.iterrows():
    if Diabetic_dataset.loc[i,'Diabetic_Prediction'] < 0.5:
        Low_Dia += 1 
    elif Diabetic_dataset.loc[i,'Diabetic_Prediction'] >= 0.5 and Diabetic_dataset.loc[i,'Diabetic_Prediction'] < 0.62:
        Medium_Dia += 1   
    else:
        High_Dia += 1

labels = 'Low Possibilty', 'Medium Possibilty', 'High Possibility'
sizes = [Low_Dia, Medium_Dia, High_Dia]
explode = (0, 0, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')

plt.show()

Mental_status_dataset = mydataset_test[['ID',"Depression",
                   "Insecurity","Patiency","Confidence","Helpful","Song","Anger"]]

Mental_status_dataset.info()

men_str_cols = Mental_status_dataset.select_dtypes(['object']).columns
Mental_status_dataset[men_str_cols] = Mental_status_dataset[men_str_cols].astype(np.int64)

Mental_status_dataset["Depression"] = Mental_status_dataset["Depression"].apply(transNegetive)
Mental_status_dataset["Anger"] = Mental_status_dataset["Anger"].apply(transNegetive)
Mental_status_dataset["Patiency"] = Mental_status_dataset["Patiency"].apply(transNegetive)
Mental_status_dataset["Insecurity"] = Mental_status_dataset["Insecurity"].apply(transNegetive)

Mental_status_dataset['Mental_Status_Prediction'] = ((Mental_status_dataset.iloc[:,1:8]*10).sum(axis = 1, skipna = True))/210


Pos = 0
Avg = 0
Neg = 0

for i, x in Mental_status_dataset.iterrows():
    if Mental_status_dataset.loc[i,'Mental_Status_Prediction'] < 0.62:
        Neg += 1 
    elif Mental_status_dataset.loc[i,'Mental_Status_Prediction'] >= 0.62 and Mental_status_dataset.loc[i,'Mental_Status_Prediction'] < 0.8:
        Avg += 1   
    else:
        Pos += 1

labels = 'Negetive', 'Average', 'Positive'
sizes = [Neg, Avg, Pos]
explode = (0.1, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')

plt.show()


Mental_status_dataset_temp = Mental_status_dataset[['ID','Mental_Status_Prediction']]

Diabetic_dataset_temp = Diabetic_dataset[['ID','Diabetic_Prediction']]

Final_Dataset = pd.merge(mydataset_test, Diabetic_dataset_temp, on = "ID", how = "outer")
Final_Dataset = pd.merge(Final_Dataset, Mental_status_dataset_temp, on = "ID", how = "outer")


X = Final_Dataset.iloc[:, [14,13]].values

from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++',max_iter = 300,n_init = 10, random_state =0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


kmeans = KMeans(n_clusters = 6, init = 'k-means++',max_iter = 300,n_init = 10, random_state =0)
y_kmeans = kmeans.fit_predict(X)

plt.scatter(X[y_kmeans == 0,0], X[y_kmeans == 0,1], s = 100, c = 'red', label = 'Average_Low')
plt.scatter(X[y_kmeans == 1,0], X[y_kmeans == 1,1], s = 100, c = 'green', label = 'Positive_Low')
plt.scatter(X[y_kmeans == 2,0], X[y_kmeans == 2,1], s = 100, c = 'blue', label = 'Average_High')
plt.scatter(X[y_kmeans == 3,0], X[y_kmeans == 3,1], s = 100, c = 'magenta', label = 'Negetive_High')
plt.scatter(X[y_kmeans == 4,0], X[y_kmeans == 4,1], s = 100, c = 'yellow', label = 'Average_Medium')
plt.scatter(X[y_kmeans == 5,0], X[y_kmeans == 5,1], s = 100, c = 'cyan', label = 'Positive_Med_High')

plt.title('Correlation between personality and diabetic risk')
plt.ylabel('Diabetic Risk')
plt.xlabel('Personality')
plt.legend()
plt.show()


D= Final_Dataset["Depression"].value_counts()
D = D['3']

I= Final_Dataset["Insecurity"].value_counts()
I = I['3']

P= Final_Dataset["Patiency"].value_counts()
P = P['3']

C= Final_Dataset["Confidence"].value_counts()
C = C['3']

H= Final_Dataset["Helpful"].value_counts()
H = H['3']

A= Final_Dataset["Anger"].value_counts()
A = A['3']

objects = ("Depressed","Insecure","Impatient","Confident","Helpful","Infuriated")
y_pos = np.arange(len(objects))
performance = [D,I,P,C,H,A]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Number of people')
plt.title('Personality')
 
plt.show()
