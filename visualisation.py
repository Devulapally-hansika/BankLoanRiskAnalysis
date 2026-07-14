# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read Dataset
data = pd.read_csv("train_u6lujuX_CVtuZ9i.csv")

# Data Cleaning
data["Gender"] = data["Gender"].fillna(data["Gender"].mode()[0])
data["Married"] = data["Married"].fillna(data["Married"].mode()[0])
data["Dependents"] = data["Dependents"].fillna(data["Dependents"].mode()[0])
data["Self_Employed"] = data["Self_Employed"].fillna(data["Self_Employed"].mode()[0])
data["LoanAmount"] = data["LoanAmount"].fillna(data["LoanAmount"].mean())
data["Loan_Amount_Term"] = data["Loan_Amount_Term"].fillna(data["Loan_Amount_Term"].mode()[0])
data["Credit_History"] = data["Credit_History"].fillna(data["Credit_History"].mode()[0])

# Loan Approval Analysis
approved = len(data[data["Loan_Status"] == "Y"])
rejected = len(data[data["Loan_Status"] == "N"])

# Create Bar Chart
status = ["Approved", "Rejected"]
count = [approved, rejected]

plt.figure(figsize=(6,5))
plt.bar(status, count)

plt.title("Loan Approval Analysis")
plt.xlabel("Loan Status")
plt.ylabel("Number of Applicants")

plt.show()
# -----------------------------
# Gender Distribution Pie Chart
# -----------------------------

male = len(data[data["Gender"] == "Male"])
female = len(data[data["Gender"] == "Female"])

gender = ["Male", "Female"]
count = [male, female]

plt.figure(figsize=(6,6))

plt.pie(count, labels=gender, autopct="%1.1f%%", startangle=90)

plt.title("Gender Distribution of Applicants")

plt.show()
# -----------------------------
# Property Area Analysis
# -----------------------------

urban = len(data[data["Property_Area"] == "Urban"])
rural = len(data[data["Property_Area"] == "Rural"])
semiurban = len(data[data["Property_Area"] == "Semiurban"])

area = ["Urban", "Rural", "Semiurban"]
count = [urban, rural, semiurban]

plt.figure(figsize=(6,5))

plt.bar(area, count)

plt.title("Property Area Distribution")
plt.xlabel("Property Area")
plt.ylabel("Number of Applicants")

plt.show()
# -----------------------------
# Education Analysis Pie Chart
# -----------------------------

graduate = len(data[data["Education"] == "Graduate"])
not_graduate = len(data[data["Education"] == "Not Graduate"])

education = ["Graduate", "Not Graduate"]
count = [graduate, not_graduate]

plt.figure(figsize=(6,6))

plt.pie(count, labels=education, autopct="%1.1f%%", startangle=90)

plt.title("Education Distribution")

plt.show()
# -----------------------------
# Credit History Analysis
# -----------------------------

good_credit = len(data[data["Credit_History"] == 1])
bad_credit = len(data[data["Credit_History"] == 0])

credit = ["Good Credit", "Bad Credit"]
count = [good_credit, bad_credit]

plt.figure(figsize=(6,5))

plt.bar(credit, count)

plt.title("Credit History Analysis")
plt.xlabel("Credit History")
plt.ylabel("Number of Applicants")

plt.show()
# -----------------------------
# Applicant Income Distribution
# -----------------------------

plt.figure(figsize=(8,5))

plt.hist(data["ApplicantIncome"], bins=20)

plt.title("Applicant Income Distribution")
plt.xlabel("Applicant Income")
plt.ylabel("Number of Applicants")

plt.show()
# -----------------------------
# Loan Amount Distribution
# -----------------------------

plt.figure(figsize=(8,5))

plt.hist(data["LoanAmount"], bins=20)

plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")
plt.ylabel("Number of Applicants")

plt.show()
# -----------------------------
# Income vs Loan Amount
# -----------------------------

plt.figure(figsize=(8,5))

plt.scatter(data["ApplicantIncome"], data["LoanAmount"])

plt.title("Applicant Income vs Loan Amount")
plt.xlabel("Applicant Income")
plt.ylabel("Loan Amount")

plt.show()