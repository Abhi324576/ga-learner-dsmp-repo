# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
bank = pd.read_csv(path)

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include ='number')
print(numerical_var)
# code starts here






# code ends here


# --------------
# code starts here

banks = bank.drop('Loan_ID',axis = 1)
#print(banks.isnull().sum())

bank_mode = banks.mode()
print(bank_mode)
banks.fillna(bank_mode.iloc[0],inplace=True)

print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks,'LoanAmount',['Gender', 'Married', 'Self_Employed'])
print(avg_loan_amount)


# code ends here



# --------------
# code starts here

# code for loan aprroved for self employed
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)

# code for loan approved for non self employed
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_nse)

# percentage of loan approved for self employed
percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]
# print percentage of loan approved for self employed
print(percentage_se)

#percentage of loan for non self employed
percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse=percentage_nse[0]
#print percentage of loan for non self employed
print (percentage_nse)

# code ends here


# --------------
# code starts here

def convert(num):
    num = num / 12
    return num;

loan_term = banks['Loan_Amount_Term'].apply(convert)

big_loan_term = loan_term[loan_term >=25].count()
print(big_loan_term)
# code ends here


# --------------
# code ends here

loan_groupby = banks.groupby(['Loan_Status'])['ApplicantIncome', 'Credit_History']

mean_values = loan_groupby.mean()


# code ends here


