name = str(input("Enter Name : "))

applejuice=70
mangojuice=50
bananajuice=40



qua1 = int(input("Select quantity of apple juice : "))
qua2 = int(input("Select quantity of mango juice : "))
qua3 = int(input("Select quantity of banana juice : "))

a1 = qua1 * applejuice
a2 = qua2 * mangojuice
a3 = qua3 * bananajuice

bill = a1+a2+a3
print("Bill is : ", bill)

is_weekend = True

print(name)

discount =is_weekend *  (bill *10) /100
print("Discount is : ", discount)

total = bill - discount
print("Total is : ", total)
