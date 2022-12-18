from tip import Bill, Count

amt = float(input("Hey, Enter the bill amount: $ "))
restaurant_name = input("What is Restaurant Name: ")

tip_percent = int(input("How much would you like to tip? 10%, 12% or 18%? "))
head_count = int(input("How many people to split the bill? "))

the_bill = Bill(amount=amt, r_name=restaurant_name)
count1 = Count(tip=tip_percent, people=head_count)

print("Each person pays: $", count1.pays(bill=the_bill,tip1=count1))