Cute Angles Problem Statment
Write a function that takes a floating point number representing an angle between 0 and 360 degrees and returns a string representing that angle in degrees, minutes, and seconds. You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

Note: You can use the following constant to represent the degree symbol:

DEGREE = "\u00B0"

# PEDAC

# Define problem
1. Inputs: floating point number representing angle
   Outputs: string representing angle in degrees, minutes, seconds

2. Explicit rules 
   - Input float will be >=0.0 and <= 360.0
   - Use degree symbol (defined with provided constant) to represent degrees, single quote (')
     to represent minutes, double quote ('') to represent seconds
   - There are 60 minutes in a degree and 60 seconds in a minute

3. Implicit rules
   - The whole number part of input decimal degree is degrees.
   - The decimal part of input decimal degree is multiplied by 60. The whole number
     part of result is minutes. The decimal part is multiplied by 60 to get seconds.
     Example: 93.034773
     93 degrees
     0.034773 * 60 = 2.08638 --> 2'
     0.08638 * 60 = 5.1828 --> 5"
   - Round seconds down to nearest integer
   - Single-digit minutes & second values should be padded with leading zeroes
     in output string
   - Single and double quotes in output string will need backslash (\) escape
     character

# Test cases - provided

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

# Data Structures
Input float
Output string
List for storing pieces of output string while processing

# Algorithm

1. Calculations for converting decimal degrees to dms

 - Use int() function to extract the whole number degree portion of the float.
 - Subtract the whole number from the original float to get decimal portion.
 - If there is no decimal portion, minutes and seconds will be 0. 
 - Multiply decimal portion by 60 to get minutes. Use int() function on result to get 
   whole number minutes.
 - Subtract the whole number minutes from decimal minutes * 60 to get the decimal portion. 
   Multiply the decimal portion by 60 to get seconds. Round down to nearest integer

2. Convert to string
 - When degrees, min, seconds are calculated in steps above, pass results to the 
   integer_to_string function from previous problem.
 - Store string results in a list
 - Output in correct format with degree, minute, second symbols