import pandas as pd
from database import create_application_table, save_application
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
data = pd.read_csv("train_u6lujuX_CVtuZ9i.csv")

# Display first 5 rows
print("First 5 Rows")
print(data.head())

# Display dataset shape
print("\nDataset Shape")
print(data.shape)

# Display column names
print("\nColumns")
print(data.columns)

# ----------------------------
# Data Cleaning
# ----------------------------

data["Gender"] = data["Gender"].fillna(data["Gender"].mode()[0])
data["Married"] = data["Married"].fillna(data["Married"].mode()[0])
data["Dependents"] = data["Dependents"].fillna(data["Dependents"].mode()[0])
data["Self_Employed"] = data["Self_Employed"].fillna(data["Self_Employed"].mode()[0])
data["LoanAmount"] = data["LoanAmount"].fillna(data["LoanAmount"].mean())
data["Loan_Amount_Term"] = data["Loan_Amount_Term"].fillna(data["Loan_Amount_Term"].mode()[0])
data["Credit_History"] = data["Credit_History"].fillna(data["Credit_History"].mode()[0])

print("\nMissing Values After Cleaning")
print(data.isnull().sum())

# ----------------------------
# Encoding
# ----------------------------

data["Gender"] = data["Gender"].map({"Male": 1, "Female": 0})

data["Married"] = data["Married"].map({"Yes": 1, "No": 0})

data["Education"] = data["Education"].map({
    "Graduate": 1,
    "Not Graduate": 0
})

data["Self_Employed"] = data["Self_Employed"].map({
    "Yes": 1,
    "No": 0
})

data["Property_Area"] = data["Property_Area"].map({
    "Urban": 2,
    "Semiurban": 1,
    "Rural": 0
})

data["Loan_Status"] = data["Loan_Status"].map({
    "Y": 1,
    "N": 0
})

data["Dependents"] = data["Dependents"].replace("3+", 3)
data["Dependents"] = data["Dependents"].astype(int)

print("\nFirst 5 Rows After Encoding")
print(data.head())

# ----------------------------
# Features and Target
# ----------------------------

X = data.drop(["Loan_ID", "Loan_Status"], axis=1)
y = data["Loan_Status"]

# ----------------------------
# Train Test Split
# ----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ----------------------------
# Create Model
# ----------------------------

model = RandomForestClassifier(random_state=42)

# ----------------------------
# Train Model
# ----------------------------

model.fit(X_train, y_train)
create_application_table()

# ----------------------------
# Test Accuracy
# ----------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

# =====================================================
# Loan Prediction
# =====================================================

print("\n========== LOAN PREDICTION ==========")

gender = input("Enter Gender (Male/Female): ")
married = input("Enter Married (Yes/No): ")
dependents = input("Enter Dependents (0/1/2/3+): ")
education = input("Enter Education (Graduate/Not Graduate): ")
self_employed = input("Enter Self Employed (Yes/No): ")

applicant_income = int(input("Enter Applicant Income: "))
coapplicant_income = float(input("Enter Coapplicant Income: "))
loan_amount = float(input("Enter Loan Amount: "))
loan_term = float(input("Enter Loan Amount Term: "))
credit_history = int(input("Enter Credit History (1/0): "))

property_area = input("Enter Property Area (Urban/Semiurban/Rural): ")

# ----------------------------
# Convert User Input
# ----------------------------

if gender == "Male":
    gender = 1
else:
    gender = 0

if married == "Yes":
    married = 1
else:
    married = 0

if education == "Graduate":
    education = 1
else:
    education = 0

if self_employed == "Yes":
    self_employed = 1
else:
    self_employed = 0

if property_area == "Urban":
    property_area = 2
elif property_area == "Semiurban":
    property_area = 1
else:
    property_area = 0

if dependents == "3+":
    dependents = 3
else:
    dependents = int(dependents)

# ----------------------------
# Create User Data
# ----------------------------

user_data = pd.DataFrame([{
    "Gender": gender,
    "Married": married,
    "Dependents": dependents,
    "Education": education,
    "Self_Employed": self_employed,
    "ApplicantIncome": applicant_income,
    "CoapplicantIncome": coapplicant_income,
    "LoanAmount": loan_amount,
    "Loan_Amount_Term": loan_term,
    "Credit_History": credit_history,
    "Property_Area": property_area
}])

# ----------------------------
# Prediction
# ----------------------------

prediction = model.predict(user_data)

print("\n========== RESULT ==========")

if prediction[0] == 1:
    result = "Approved"
    print("Loan Approved")
else:
    result = "Rejected"
    print("Loan Rejected")

save_application(
    gender,
    married,
    dependents,
    education,
    self_employed,
    applicant_income,
    coapplicant_income,
    loan_amount,
    loan_term,
    credit_history,
    property_area,
    result
)

print("\nApplicant Details Saved Successfully.")