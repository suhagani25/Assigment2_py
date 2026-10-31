total_amount=int(input("enter amout"))
friends=int(input("enter total friends"))
tip=10/100*total_amount
final_amount=total_amount+tip
per_person_pay=final_amount/friends
print(per_person_pay)