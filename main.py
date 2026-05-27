import streamlit as st
import pandas as pd
import os
st.title("Smart Expense Tracker")
file = "expenses.csv"
if os.path.exists(file):
  df = pd.read_csv(file)
else:
  df = pd.DataFrame(columns=["Type", "Category", "Amount"])
                      
expense_type = st.selectbox("Type", ["Income", "Expense"])

category = st.text_input("Category")

amount = st.number_input("Amount", min_value=0.0)

if st.button("Add Transaction"):
  new_data = {"Type": expense_type,"Category": category,"Amount": amount}
  df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
  df.to_csv(file, index=False)
  st.success("Transaction Added Successfully!")

st.subheader("Transactions")

st.dataframe(df)

income = df[df["Type"] == "Income"]["Amount"].sum()

expense = df[df["Type"] == "Expense"]["Amount"].sum()

balance = income - expense

st.subheader("Summary")

st.write("Total Income:", income)

st.write("Total Expense:", expense)

st.write("Balance:", balance)
