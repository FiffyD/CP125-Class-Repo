def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

if __name__ == "__main__":
    year_input = int(input("Enter a year: "))
    result = is_leap_year(year_input)
    print(result)