def is_budget_sufficient (one_way_km,budget):
    round_trip_km = one_way_km * 2
    litres_needed = round_trip_km / 10
    total_cost = litres_needed * 2.00 
    return total_cost <= budget
print (is_budget_sufficient (100,40))
print (is_budget_sufficient(100,39))