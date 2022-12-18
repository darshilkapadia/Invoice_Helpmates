from tip import Bill, Count

amt = float(input("Hey, Enter the bill amount: $ "))
r_name = input("What is Restaurant Name: ")

tip_percent = int(input("How much would you like to tip? 10%, 12% or 18%? "))
person_count = int(input("How many people to split the bill? "))

the_bill = Bill(amt, r_name)
count1 = Count(tip_percent, person_count)

print("Each person pays: $", count1.pays(bill=the_bill,tip1=count1))