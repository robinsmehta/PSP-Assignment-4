#employee_data_analysis.py

import pandas as pd

# Creating the DataFrame
data = {
    "EmployeeID": [101, 102, 103, 104, 105],
    "Name": ["John Smith", "Alice Brown", "Bob White", "Emma Green", "Charlie Red"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Age": [30, 28, 35, 40, 25],
    "Salary": [70000, 60000, 80000, 90000, 55000],
    "JoinDate": ["2018-07-15", "2020-03-10", "2016-11-01", "2012-05-25", "2021-06-01"],
    "ExperienceYears": [5, 3, 7, 11, 2]
}

df = pd.DataFrame(data)
df["JoinDate"] = pd.to_datetime(df["JoinDate"])

# a. Select only the Name and Salary columns
print("a. Name and Salary columns:")
print(df[["Name", "Salary"]])

# b. Filter out all employees in the "IT" department
print("\nb. Employees in IT department:")
print(df[df["Department"] == "IT"])

# c. Employees older than 30 and average salary per department
print("\nc. Employees older than 30:")
older_than_30 = df[df["Age"] > 30]
print(older_than_30)

print("\nAverage salary in each department:")
print(df.groupby("Department")["Salary"].mean())

# d. Count number of employees in each department
print("\nd. Number of employees in each department:")
print(df["Department"].value_counts())

# e. Add Bonus column (10% of Salary)
df["Bonus"] = df["Salary"] * 0.10
print("\ne. Data with Bonus column added:")
print(df[["Name", "Salary", "Bonus"]])

# f. Replace "HR" with "Human Resources"
df["Department"] = df["Department"].replace("HR", "Human Resources")
print("\nf. Replaced 'HR' with 'Human Resources':")
print(df["Department"])

# g. Employee(s) with the longest tenure
longest_tenure = df[df["JoinDate"] == df["JoinDate"].min()]
print("\ng. Employee(s) with the longest tenure:")
print(longest_tenure)

# h. SalaryCategory column
df["SalaryCategory"] = df["Salary"].apply(lambda x: "High" if x > 75000 else "Low")
print("\nh. Data with SalaryCategory:")
print(df[["Name", "Salary", "SalaryCategory"]])

# i. Check and remove duplicates in EmployeeID
print("\ni. Checking for duplicate EmployeeIDs:")
duplicates = df[df.duplicated("EmployeeID")]
print("Duplicate rows:\n", duplicates)
df = df.drop_duplicates("EmployeeID")

# j. Median age of all employees
print("\nj. Median Age of employees:")
print(df["Age"].median())
