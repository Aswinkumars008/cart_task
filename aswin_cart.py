a = 20
b = 40
c = 50
wrap_a=0
wrap_b=0
wrap_c=0
def giftpacking():
    giftpacking = input("Do you want this product wrapped as a gift (yes/no)")
    yes_choices = ['yes', 'y']
    no_choices = ['no', 'n']
    if giftpacking.lower() in yes_choices:
        return 1
    elif giftpacking.lower() in no_choices:
        return 0
a_qty = int(input("How much a do you want ?"))
if a_qty > 0:
    wrap_a = giftpacking()
b_qty = int(input("How much b do you want ?"))
if b_qty > 0:
    wrap_b = giftpacking()
c_qty = int(input("How much c do you want ?"))
if c_qty > 0:
    wrap_c = giftpacking()
if a_qty > 0:
    print("You have orderd",a_qty,"a for :$", a*a_qty)
if b_qty > 0:
    print("You have orderd",b_qty,"b for :$", b*b_qty)
if c_qty > 0:
    print("You have orderd",c_qty,"c for : $", c*c_qty)
total_amount = a_qty + b_qty + c_qty
subtotal = a*a_qty+b*b_qty+c*c_qty
print("subtotal for this purchase is : $",subtotal)
flat_10_discount = 0
bulk_5_discount = 0
bulk_10_discount = 0
tiered_50_discount = 0
discount_1 = 0
discount_2 = 0
discount_3 = 0
discount_4 = 0
if subtotal > 200:
    discount_1 = 10
    flat_10_discount = subtotal - discount_1
if a_qty >10 or c_qty > 10 or b_qty > 10:
    if a_qty > 10:
        discount_2 = (a_qty*a*5)/100
    elif b_qty > 10:
        discount_2 = (b_qty*b*5)/100
    elif c_qty > 10:
        discount_2 = (c_qty*c*5)/100
bulk_5_discount = subtotal - discount_2
if a_qty + b_qty + c_qty > 20:
    discount_3 = (subtotal * 10) / 100
    bulk_10_discount = subtotal - discount_3

if (a_qty + b_qty + c_qty > 30) and ( a_qty > 15 or b_qty > 15 or c > 15 ):
    if a_qty > 15 :
        discount_4 = ( a_qty * a * 50 ) / 100
    elif b_qty > 15 :
        discount_4 = ( b_qty * b * 50 ) / 100
    elif c_qty > 15 :
        discount_4 = ( c_qty * c * 50 ) / 100
    tiered_50_discount = subtotal - discount_4
final_discount = [ discount_1 , discount_2 , discount_3 , discount_4 ]
final_discount.sort()
discount_flag=0
if final_discount[3] == discount_1:
    discount_flag=1
    print("flat_10_discount is applied. The discount amount is : $", discount_1)
elif final_discount[3] == discount_2:
    discount_flag=2
    print("bulk_5_discount is applied. The discount amount is : $", discount_2)
elif final_discount[3] == discount_3:
    discount_flag=3
    print("bulk_10_discount is applied. The discount amount is : $", discount_3)
elif final_discount[3] == discount_4:
    discount_flag=4
    print("tiered_50_discount is applied. The discount amount is : $", discount_4)
if discount_flag == 1:
    total = flat_10_discount 
elif discount_flag == 2:
    total = bulk_5_discount 
elif discount_flag == 3:
    total = bulk_10_discount 
elif discount_flag == 4:
    total = tiered_50_discount 
else: 
    total = subtotal
total_gift_packing_fee = 0
if wrap_a == 1:
    total=total + a_qty
    total_gift_packing_fee = total_gift_packing_fee + a_qty
    print("Gift packing fee for a : $", a_qty)
if wrap_b == 1:
    total=total + b_qty
    total_gift_packing_fee = total_gift_packing_fee + b_qty
    print("Gift packing fee for b : $", b_qty)
if wrap_c == 1:
    total=total + c_qty
    total_gift_packing_fee = total_gift_packing_fee + c_qty
    print("Gift packing fee for c : $", c_qty)
if wrap_c == 1 or wrap_b == 1 or wrap_a == 1:
    print("total gift packing fee is : $", total_gift_packing_fee)
if total_amount%10 == 0:
    package_quantity = int( ( total_amount / 10 ))
    print("The shipping fee for your purchase : $", package_quantity * 5) 
else:
    package_quantity = int( ( total_amount / 10 ) +1)
    print("The shipping fee for your purchase : $", package_quantity * 5)
shipping_fee = package_quantity * 5
total = total + shipping_fee
print("Your total amount for this order is :", total)