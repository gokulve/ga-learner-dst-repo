# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
# Importing header files
import os
#import numpy as np
#import warnings
#warnings.filterwarnings('ignore')
#os.getcwd()
#path="Census.csv"
#data=open(path,r)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(path)
print(data)

print("\nData: \n\n", data)

print("\nType of data: \n\n", type(data))

#Code starts here
census=np.concatenate((data,new_record))
print("data share:", data.shape)
print("census share:",census.shape)

#Step 2: We often associate the potential of a country based on the age distribution of the people residing there. We too want to do a simple analysis of the age distribution
#age=np.array(census[:0])
age=census[:,[0]]
print("age :",age)

max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)

print("max age:",max_age)
print("min age:",min_age)
print("mean age:",age_mean)
print("Std age:",age_std)

#Step 3: The constitution of the country tries it's best to ensure that people of all races are able to live harmoniously. Let's check the country's race distribution to identify the minorities so that the government can help them.


#print(census[:,2]==0)
#print(census[census[:,2]==0,:])


race_0=census[census[:,2]==0, :]
race_1=census[census[:,2]==1, :]
race_2=census[census[:,2]==2, :]
race_3=census[census[:,2]==3, :]
race_4=census[census[:,2]==4, :]

len_0=race_0.shape[0]
len_1=race_1.shape[0]
len_2=race_2.shape[0]
len_3=race_3.shape[0]
len_4=race_4.shape[0]

print("Print number of Race 0",race_0.shape[0])
print("Print number of Race 1",race_1.shape[0])
print("Print number of Race 2",race_2.shape[0])
print("Print number of Race 3",race_3.shape[0])
print("Print number of Race 4",race_4.shape[0])

#print("Race 0:===============================================",race_0)
#print("Race 1:===============================================",race_1)
#print("Race 2:===============================================",race_2)
#print("Race 3:===============================================",race_3)
#print("Race 4:===============================================",race_4)


#print("race_0 = ",census[extractRace(0), :])
#print("race_1 = ",census[extractRace(1), :])
#print("race_2 = ",census[extractRace(2), :])
#print("race_3 = ",census[extractRace(3), :])
#print("race_4 = ",census[extractRace(4), :])

#index of race + 1 to off set as it starts from 0 
len_race=[len_0,len_1,len_3,len_4]
minority_race=(len_race.index(min(len_race))+1)
print("Miniority Race",minority_race)

senior_citizens = census[census[:,0]>60]
#print(senior_citizens)

working_hours_sum = sum(senior_citizens[:,6])
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours = (working_hours_sum/senior_citizens_len)
print(avg_working_hours)

high=census[census[:,1]>10]
low=census[census[:,1]<=10]
print ("\nHigh: \n\n",high,"\nLow: \n\n",low)
avg_pay_high=high[:,7].mean()
print("\nAvg Pay High :",avg_pay_high)
avg_pay_low=low[:,7].mean()
print("\nAvg Pay Low :",avg_pay_low)


