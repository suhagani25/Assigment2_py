item1=int(input("enter 1st item price"))
item2=int(input("enter 2nd item price"))
total_price=item1+item2
discount=15/100*total_price
total_bill=total_price-discount+99
print(total_bill)


likes=int(input("enter likes"))
comment=int(input("enter comment"))
views=int(input("enter views"))
engagement=(likes+comment)/views*100
print(engagement)