# --------------
# code starts here

# code for loan aprroved for self employed
loan_approved_se = bank.loc[(bank["Self_Employed"]=="Yes")  & (bank["Loan_Status"]=="Y"), ["Loan_Status"]].count()
loan_approved_se= loan_approved_se.values[0]
print(loan_approved_se)

# code for loan approved for non self employed
loan_approved_nse = bank.loc[(bank["Self_Employed"]=="No")  & (bank["Loan_Status"]=="Y"), ["Loan_Status"]].count()
loan_approved_nse= loan_approved_nse.values[0]
print(loan_approved_nse)
# percentage of loan approved for self employed
percentage_se = (loan_approved_se * 100 / 614)

# print percentage of loan approved for self employed
print(percentage_se)

#percentage of loan for non self employed
percentage_nse = (loan_approved_nse * 100 / 614)

#print percentage of loan for non self employed
print (percentage_nse)

# code ends here


# --------------
# Code starts here

avg_loan_amount = bank.pivot_table( index = ['Gender', 'Married','Self_Employed'], values = ['LoanAmount'], aggfunc = np.mean)
print(avg_loan_amount)

# code ends here



# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12)

big_loan_term = len(loan_term[loan_term >=25])

# code ends here


# --------------
# code ends here
loan_groupby = banks.groupby('Loan_Status')['ApplicantIncome','Credit_History']
mean_values = loan_groupby.agg([np.mean])


# code ends here


# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)
# code ends here


# --------------
# code starts here
# banks = bank.drop(columns = 'Loan_ID', inplace = True, axis =1)
# print(bank.isnull().sum())
# bank_mode = banks.mode().iloc[0]
# print(bank_mode)
# banks.fillna(bank_mode, inplace = True)

#code ends here



# code starts here

# load the dataset and drop the Loan_ID
banks= bank.drop(columns='Loan_ID')


# check  all the missing values filled.

print(banks.isnull().sum())

# apply mode 

bank_mode = banks.mode().iloc[0]

# Fill the missing values with 

banks.fillna(bank_mode, inplace=True)

# check again all the missing values filled.

print(banks.isnull().sum())





#code ends here


