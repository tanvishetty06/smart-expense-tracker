expenses=[]
while True:
  print("\nSMART EXPENSE TRACKER")
  print("\n1.Add Transactions")
  print("\n2.View Transactions")
  print("\n3.Show Balance")
  print("\n4.Exit")
  choice=int(input("Enter your choice:"))
  if choice==1:
    amount=float(input("Enter amount:"))
    category=input("Enter category:")
    transaction_type=input("Credit or Debit:")
    transaction={"amount":amount,"category":category,"type":transaction_type}
    expensesappend(transaction)
    print("Transaction added successfully!")
  elif choice==2:
    print("\nTransaction History:")
    for iytem in expenses:
      print(item)
  elif choice==3:
    credit=0
    debit=0
    for item in expenses:
      if item["type"].lower()=="credit":
        credit+=item["amount"]
      else:
        debit+=item["amount"]
    balance=credit-debit
    print("Total Credit:Rs",credit)
    print("Total Debit:Rs",debit)
    print("Remaining Balance:Rs",balance)
  elif choice==4:
    print("Thank you!")
    break
  else:
    print("Invalid choice!")
