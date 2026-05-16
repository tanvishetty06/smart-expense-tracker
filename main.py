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
    date=input("Enter date (DD/MM/YYYY):")
    transaction={"amount":amount,"category":category,"type":transaction_type,"date":date}
    expensesappend(transaction)
    print("Transaction added successfully!")
  elif choice==2:
    print("\nTransaction History:")
    for iytem in expenses:
      print(item)
  elif choice == "3":
        credit = 0
        debit = 0
        category_totals = {}
    for item in expenses:
      if item["type"].lower() == "credit":
        credit += item["amount"]
      else:
        debit += item["amount"]
        category = item["category"]
        if category in category_totals:
          category_totals[category] += item["amount"]
        else:
          category_totals[category] = item["amount"]
    balance = credit - debit
    print(f"\nTotal Credit: Rs.{credit}")
    print(f"Total Debit: Rs.{debit}")
    print(f"Remaining Balance: Rs.{balance}")
    if category_totals:
      highest = max(category_totals, key=category_totals.get)
      lowest = min(category_totals, key=category_totals.get)
      print(f"Highest Spending Category: {highest}")
      print(f"Lowest Spending Category: {lowest}")
  elif choice==4:
    print("Thank you!")
    break
  else:
    print("Invalid choice!")
