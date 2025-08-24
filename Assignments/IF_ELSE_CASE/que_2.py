print("------profit and loss calcuator------")

cost_price=int(input("enter the cost price here : "))
selling_price=int(input("enter the selling price here : "))
if cost_price>selling_price:
    print("they got a loss of total",cost_price-selling_price,"ruppees")
else:
    print("they made a profit of total",selling_price-cost_price,"ruppees")