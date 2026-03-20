def Calculate_Revenue(Order):
    total_orders = 0
    for order in Orders:
        total_orders += order["total"]
    return total_orders
