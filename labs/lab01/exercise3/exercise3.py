def validate_entry(name,pin):
    if name == "Director" and pin == 1122:
        return bool(True)
    elif name == "Security" and pin == 9900:
        return bool(True)
    else :
        return bool(False)

print(validate_entry("Director",1122))
print(validate_entry("Director",9900))
print(validate_entry("director",1122))