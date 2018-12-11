# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path,  delimiter=",", skip_header=1)
#print(data)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate((data, new_record), axis = 0)
#Code starts here
print(census)


# --------------
#Code starts here
age = census[:,0]
max_age = age.max(axis=0)
min_age = age.min()
age_mean = age.mean()
age_std = age.std()
#print(age_std)


# --------------
#Code starts here
# R = census[:,2]
# print(R)

race_0 = census[census[:,2] == 0]
race_1 = census[census[:,2] == 1]
race_2 = census[census[:,2] == 2]
race_3 = census[census[:,2] == 3]
race_4 = census[census[:,2] == 4]
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
x= min(len_0,len_1,len_2,len_3,len_4)
if len_0 == x:
    minority_race = 0
if len_1 == x:
    minority_race = 1
if len_2 == x:
    minority_race =2
if len_3 == x:
    minority_race = 3
if len_4 == x:
    minority_race = 4


# --------------
#Code starts here
senior_citizens = census[census[:,0] > 60]
working_hours_sum = senior_citizens[:,6].sum()
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]


avg_pay_high = high[:,7].mean()

print(avg_pay_high)
avg_pay_low = low[:,7].mean()
print(avg_pay_low)
print(avg_pay_high == avg_pay_low)


