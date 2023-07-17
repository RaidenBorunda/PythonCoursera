# PROMPT
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours 
# worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75)


hrs = input("Enter Hours:")
h = float(hrs) # Simplify var and convert to float

rate = input("Enter Rate:")
r = float(rate) # Simplify var and convert to float

if h > 40 : # Account for overtime
    oth = h - 40
    h = 40 # Set hours to 40 now that we have overtime hours calculated
    otr = r * 1.5
    otg = oth * otr

gross = (h * r) + otg
print(gross)

# 498.75 is the desired result