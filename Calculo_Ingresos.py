def calculate_revenue(orders):
    total_revenue = 0
    
    for order in orders:
        total_revenue += order["total"]
    
    return total_revenue