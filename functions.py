def display_twice(username, amount, due_date):
    print(f"Hello {username}")
    print("Your bill of ${amount:2f} is due: {due_date}")

display_twice("BroCode", 42.50, "01/01")    