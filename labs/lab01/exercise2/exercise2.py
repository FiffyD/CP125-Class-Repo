import math
def calculate_tent_cost (participants,tent_capacity,tent_price):
    tent_needed = math.ceil(participants / tent_capacity)
    total_cost = tent_needed * tent_price
    return total_cost

print(calculate_tent_cost(12,4,100))
print(calculate_tent_cost(13,4,100))