# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path)

loan_status = data['Loan_Status'].value_counts()

loan_status.plot(kind='bar')


#Code starts here


# --------------
#Code starts here

# property_and_loan = data.groupby(['Property_Area','Loan_Status'])

property_and_loan=data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan=property_and_loan.size().unstack()
property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))

# property_and_loan.size().unstack()

# property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))

#Changing the x-axis label
plt.xlabel('Property_Area')

#Changing the y-axis label
plt.ylabel('Loan_Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)



# --------------
#Code starts here

education_and_loan=data.groupby(['Education', 'Loan_Status'])
education_and_loan=education_and_loan.size().unstack()
education_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))


plt.xlabel('Education')

plt.ylabel('Loan_Status')

plt.xticks(rotation=45)



# --------------
#Code starts here
graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']

graduate['LoanAmount'].plot(kind='density',label='Graduate')

not_graduate['LoanAmount'].plot(kind='density',label=' Not Graduate')








#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here

# fig = plt.figure()
# ax_1 = fig.add_subplot(221)
# ax_2 = fig.add_subplot(222, sharex=ax_1, sharey=ax_1)
# ax_3 = fig.add_subplot(223, sharex=ax_1, sharey=ax_1)


fig, (ax_1,ax_2,ax_3) = plt.subplots(3, 1, sharex=True, sharey=True)


plt.title('ApplicantIncome')
plt.xlabel('ApplicantIncome')
plt.ylabel('LoanAmount')
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'],color='red')




plt.title('CoapplicantIncome')
plt.xlabel('CoapplicantIncome')
plt.ylabel('LoanAmount')
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'],color='green')


data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']


plt.title('TotalIncome')
plt.xlabel('TotalIncome')
plt.ylabel('LoanAmount')
ax_1.scatter(data['TotalIncome'],data['LoanAmount'],color='blue')




