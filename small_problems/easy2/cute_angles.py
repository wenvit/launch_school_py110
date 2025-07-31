'''
Cute Angles Problem Statment
Write a function that takes a floating point number representing 
an angle between 0 and 360 degrees and returns a string representing 
that angle in degrees, minutes, and seconds. You should use a 
degree symbol (°) to represent degrees, a single quote (') to 
represent minutes, and a double quote (") to represent seconds. 
There are 60 minutes in a degree, and 60 seconds in a minute.

Note: You can use the following constant to represent the degree symbol:

DEGREE = "\u00B0"

'''
import math

DEGREE = "\u00B0"
TOLERANCE = 1e-9 # tolerance for math.isclose function

def map_digits(digit):

    int_to_str_mapper = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
    }

    return int_to_str_mapper[digit]

def integer_to_string(number):
    list_of_str_digits = []

    if number == 0:
        return map_digits(number)
    else:
        while number > 0:
            digit = number % 10
            string_digit = map_digits(digit)
            list_of_str_digits.insert(0, string_digit)
            number = number // 10

        return ''.join(list_of_str_digits)
    
def dms(dd_float):

    dms_str = []

    # degrees
    deg_float = int(dd_float)
    deg_str = integer_to_string(deg_float) + DEGREE
    dms_str.append(deg_str)

    # minutes
    decimal = dd_float - deg_float
    if math.isclose(decimal, 0.0, abs_tol=TOLERANCE):
        dms_str.append("00'00\"")
        return ''.join(dms_str)
    else:
        minutes_total = decimal * 60 # total minutes
        minutes_int = int(minutes_total) # whole number portion of minutes
        minutes_str = integer_to_string(minutes_int).rjust(2, '0') + "'"
        dms_str.append(minutes_str)

    # seconds: decimal portion of minutes left 
    minutes_decimal = minutes_total - minutes_int
    seconds_int = math.floor(minutes_decimal * 60)
    seconds_str = integer_to_string(seconds_int).rjust(2, '0') + '"'
    dms_str.append(seconds_str)

    return ''.join(dms_str)


print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")