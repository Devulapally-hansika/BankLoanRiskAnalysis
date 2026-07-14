import pandas as pd
from database import save_query, create_database
create_database()

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


print("===================================")
print("       BANK LOAN RISK ANALYSIS")
print("===================================")

print("1. Search by Loan ID")
print("2. Check Loan Status")
print("3. Search by Gender")
print("4. Search by Property Area")
print("5. Search by Credit History")
print("6. Search High Income Applicants")
print("7. Search Self Employed Applicants")
print("8. Exit")


choice = int(input("Enter your choice: "))


# Search by Loan ID
if choice == 1:

    loan_id = input("Enter Loan ID: ")
    save_query("Loan ID Search", loan_id)

    result = data[data["Loan_ID"] == loan_id]

    if len(result) > 0:
        print(result)
    else:
        print("Loan ID Not Found")



# Check Loan Status
elif choice == 2:

    loan_id = input("Enter Loan ID: ")
    save_query("Loan Status Check", loan_id)

    result = data[data["Loan_ID"] == loan_id]

    if len(result) > 0:

        status = result["Loan_Status"].values[0]

        print("---------------------------")
        print("Loan ID :", loan_id)

        if status == "Y":
            print("Loan Status : Approved")
        else:
            print("Loan Status : Rejected")

        print("---------------------------")

    else:
        print("Loan ID Not Found")



# Search by Gender
elif choice == 3:

    gender = input("Enter Gender (Male/Female): ")

    result = data[data["Gender"] == gender]

    if len(result) > 0:
        print(result)

    else:
        print("No Records Found")



# Search by Property Area
elif choice == 4:

    area = input("Enter Property Area (Urban/Rural/Semiurban): ")

    result = data[data["Property_Area"] == area]

    if len(result) > 0:
        print(result)

    else:
        print("No Records Found")



# Search by Credit History
elif choice == 5:

    credit = int(input("Enter Credit History (1/0): "))

    result = data[data["Credit_History"] == credit]

    if len(result) > 0:

        print(result[[
            "Loan_ID",
            "ApplicantIncome",
            "LoanAmount",
            "Credit_History",
            "Loan_Status"
        ]])

    else:
        print("No Records Found")



# Search High Income Applicants
elif choice == 6:

    income = int(input("Enter Minimum Income: "))

    result = data[data["ApplicantIncome"] >= income]

    if len(result) > 0:

        print(result[[
            "Loan_ID",
            "ApplicantIncome",
            "LoanAmount",
            "Loan_Status"
        ]])

    else:
        print("No High Income Applicants Found")



# Search Self Employed Applicants
elif choice == 7:

    emp = input("Enter Self Employed (Yes/No): ")

    result = data[data["Self_Employed"] == emp]

    if len(result) > 0:
        print(result)

    else:
        print("No Records Found")



# Exit
elif choice == 8:

    print("Thank You")



else:

    print("Invalid Choice")