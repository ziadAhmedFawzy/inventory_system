sell_pay = input("sell or buy : ")
inventory = 0
_sum_ = 0

if sell_pay.lower() == "buy":
    date = input("enter the date : ")
    # sum_input_product
    purchases_unit = input("purchases unit : ")
    purchases_price = input("purchases price : ")
    # add to inventory
    inventory = inventory + int(purchases_unit)
    _sum_ = _sum_ + float(purchases_price) * int(purchases_unit)
    print("date : " + date)
    print("purchases unit : " + purchases_unit)
    print("purchases price : " + purchases_price)
    print("inventory : " + str(inventory) + " x " + str(purchases_price) + " = " + str(_sum_))
elif sell_pay.lower() == "sell":
    sell_unit = input("enter unit of sell :")
    if inventory >= int(sell_unit):
        data = input("enter date : ")
        inventory = inventory - int(sell_unit)
        new_price = input("enter your price :")
        sum_sell = int(sell_unit) * int(new_price)
        print("date : " + data)
        print("date : " + data)
        print("sell of unit : " + sell_unit + " x " + new_price + " = " + str(sum_sell))
        print("inventory :" + str(inventory))
elif sell_pay.lower() == "sell and buy" or sell_pay.lower() == "buy and sell":
    date_a = input("enter the date : ")
    purchases_unit = input("purchases unit : ")
    purchases_price = input("purchases price : ")
    inventory = inventory + int(purchases_unit)
    _sum_ = _sum_ + float(purchases_price) * int(purchases_unit)
    print("date : " + date_a)
    print("purchases unit : " + purchases_unit)
    print("purchases price : " + purchases_price)
    print("inventory : " + str(inventory) + " x " + str(purchases_price) + " = " + str(_sum_))
    sell_unit = input("enter unit of sell :")
    if inventory >= int(sell_unit):
        data_b = input("enter date : ")
        inventory = inventory - int(sell_unit)
        new_price = input("enter your price :")
        sum_sell = int(sell_unit) * int(new_price)
        print("date : " + data_b)
        print("date : " + data_b)
        print("sell of unit : " + sell_unit + " x " + new_price + " = " + str(sum_sell))
        print("inventory :" + str(inventory))
    else:
        print("your inventory is less than the sell of unit")
