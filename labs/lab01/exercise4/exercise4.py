def get_hourly_rate(vehicle_type,hour):
    if vehicle_type == "Electric":
        price_hour =  2.00
    elif vehicle_type == "Hybrid":
        if hour >= 22 or hour <= 6 :
            price_hour = 2.00
        else :
            price_hour = 5.00
    else :
        price_hour = 5.00
    return price_hour
print(get_hourly_rate("Hybrid",23))
print(get_hourly_rate("Hybrid",13))
print(get_hourly_rate("Sedan",2))