import pandas as pd

# Read the CSV file
data = pd.read_csv("train_u6lujuX_CVtuZ9i.csv")

# First 5 rows
print("FIRST 5 ROWS")
print(data.head())

print("\n----------------------")

# Shape of dataset
print("SHAPE OF DATASET")
print(data.shape)

print("\n----------------------")

# Column names
print("COLUMN NAMES")
print(data.columns)

print("\n----------------------")

# Dataset information
print("DATASET INFORMATION")
data.info()

print("\n----------------------")

# Missing values
print("MISSING VALUES")
print(data.isnull().sum())
print("\n----------------------")
print("DATA CLEANING")

# Fill missing values in categorical columns
data["Gender"] = data["Gender"].fillna(data["Gender"].mode()[0])
data["Married"] = data["Married"].fillna(data["Married"].mode()[0])
data["Dependents"] = data["Dependents"].fillna(data["Dependents"].mode()[0])
data["Self_Employed"] = data["Self_Employed"].fillna(data["Self_Employed"].mode()[0])

# Fill missing values in numerical columns
data["LoanAmount"] = data["LoanAmount"].fillna(data["LoanAmount"].median())
data["Loan_Amount_Term"] = data["Loan_Amount_Term"].fillna(data["Loan_Amount_Term"].median())
data["Credit_History"] = data["Credit_History"].fillna(data["Credit_History"].median())

print("\nMissing Values After Cleaning")
print(data.isnull().sum())
print("\n----------------------")
print("BUSINESS ANALYSIS")

# Total Loan Applications
total_applications = len(data)
print("Total Loan Applications:", total_applications)

# Approved Loans
approved_loans = len(data[data["Loan_Status"] == "Y"])
print("Approved Loans:", approved_loans)

# Rejected Loans
rejected_loans = len(data[data["Loan_Status"] == "N"])
print("Rejected Loans:", rejected_loans)

# Approval Percentage
approval_percentage = (approved_loans / total_applications) * 100
print("Approval Percentage:", round(approval_percentage, 2), "%")

# Rejection Percentage
rejection_percentage = (rejected_loans / total_applications) * 100
print("Rejection Percentage:", round(rejection_percentage, 2), "%")

# Average Applicant Income
average_income = data["ApplicantIncome"].mean()
print("Average Applicant Income:", round(average_income, 2))

# Average Loan Amount
average_loan = data["LoanAmount"].mean()
print("Average Loan Amount:", round(average_loan, 2))
print("\n----------------------")
print("GENDER ANALYSIS")

# Count Male and Female applicants
gender_count = data["Gender"].value_counts()

print(gender_count)
print("\n----------------------")
print("LOAN APPROVAL BY GENDER")

loan_gender = pd.crosstab(data["Gender"], data["Loan_Status"])

print(loan_gender)
print("\n----------------------")
print("PROPERTY AREA ANALYSIS")

urban = 0
rural = 0
semiurban = 0

for area in data["Property_Area"]:

    if area == "Urban":
        urban = urban + 1

    elif area == "Rural":
        rural = rural + 1

    else:
        semiurban = semiurban + 1

print("Urban Applicants :", urban)
print("Rural Applicants :", rural)
print("Semiurban Applicants :", semiurban)
print("\n----------------------")
print("EDUCATION ANALYSIS")

graduate = 0
not_graduate = 0

for education in data["Education"]:

    if education == "Graduate":
        graduate = graduate + 1

    else:
        not_graduate = not_graduate + 1

print("Graduate Applicants :", graduate)
print("Not Graduate Applicants :", not_graduate)
print("\n----------------------")
print("LOAN APPROVAL BASED ON EDUCATION")

graduate_approved = 0
not_graduate_approved = 0

for i in range(len(data)):

    if data["Education"][i] == "Graduate" and data["Loan_Status"][i] == "Y":
        graduate_approved = graduate_approved + 1

    elif data["Education"][i] == "Not Graduate" and data["Loan_Status"][i] == "Y":
        not_graduate_approved = not_graduate_approved + 1

print("Graduate Approved Loans :", graduate_approved)
print("Not Graduate Approved Loans :", not_graduate_approved)
print("\n----------------------")
print("SELF EMPLOYED ANALYSIS")

self_employed = 0
not_self_employed = 0

for employee in data["Self_Employed"]:

    if employee == "Yes":
        self_employed = self_employed + 1

    else:
        not_self_employed = not_self_employed + 1

print("Self Employed Applicants :", self_employed)
print("Not Self Employed Applicants :", not_self_employed)
print("\n----------------------")
print("LOAN APPROVAL BASED ON SELF EMPLOYMENT")

self_approved = 0
not_self_approved = 0

for i in range(len(data)):

    if data["Self_Employed"][i] == "Yes" and data["Loan_Status"][i] == "Y":
        self_approved = self_approved + 1

    elif data["Self_Employed"][i] == "No" and data["Loan_Status"][i] == "Y":
        not_self_approved = not_self_approved + 1

print("Self Employed Approved Loans :", self_approved)
print("Not Self Employed Approved Loans :", not_self_approved)
print("\n----------------------")
print("CREDIT HISTORY ANALYSIS")

good_credit = 0
bad_credit = 0

for credit in data["Credit_History"]:

    if credit == 1:
        good_credit = good_credit + 1

    else:
        bad_credit = bad_credit + 1

print("Good Credit History :", good_credit)
print("Bad Credit History :", bad_credit)
print("\n----------------------")
print("LOAN APPROVAL BASED ON CREDIT HISTORY")

good_credit_approved = 0
bad_credit_approved = 0

for i in range(len(data)):

    if data["Credit_History"][i] == 1 and data["Loan_Status"][i] == "Y":
        good_credit_approved = good_credit_approved + 1

    elif data["Credit_History"][i] == 0 and data["Loan_Status"][i] == "Y":
        bad_credit_approved = bad_credit_approved + 1

print("Approved with Good Credit History :", good_credit_approved)
print("Approved with Bad Credit History :", bad_credit_approved)
print("\n----------------------")
print("APPLICANT INCOME ANALYSIS")

highest_income = data["ApplicantIncome"].max()
lowest_income = data["ApplicantIncome"].min()
average_income = data["ApplicantIncome"].mean()

print("Highest Applicant Income :", highest_income)
print("Lowest Applicant Income :", lowest_income)
print("Average Applicant Income :", round(average_income, 2))
print("\n----------------------")
print("LOAN AMOUNT ANALYSIS")

highest_loan = data["LoanAmount"].max()
lowest_loan = data["LoanAmount"].min()
average_loan = data["LoanAmount"].mean()

print("Highest Loan Amount :", highest_loan)
print("Lowest Loan Amount :", lowest_loan)
print("Average Loan Amount :", round(average_loan,2))
print("\n----------------------")
print("HIGH INCOME APPLICANTS")

average_income = data["ApplicantIncome"].mean()

count = 0

for income in data["ApplicantIncome"]:

    if income > average_income:
        count = count + 1

print("Applicants earning above average income :", count)