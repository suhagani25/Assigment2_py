pocket_Money=float(input("enter pocket money"))
canteen=int(input("enter canteen price"))
transport=int(input("enter transport price"))
shopping=int(input("enter shopping price"))

save_Money=pocket_Money-canteen-transport-shopping

is_budget_safe=save_Money>=0

if is_budget_safe:
 print(True)
else:
    print(False)

print("pocket_Money:",pocket_Money)
print("canteen_budget:",canteen)
print("transport:",transport)
print("shopping:",shopping)
print("save_money:",save_Money)
