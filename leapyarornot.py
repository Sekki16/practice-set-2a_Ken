def is_leap_year(year):
    try:
        year = int(year)
        if year < 0:
            return "Invalid input: Year must be a positive integer."
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return f"{year} is a leap year."
        else:
            return f"{year} is not a leap year."
    except ValueError:
        return "Invalid input: Year must be a valid integer."