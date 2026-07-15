def convert_to_F(Temp_C):
    return ((float(9)/5)*Temp_C + 32)
Temp_in_C = (36.5, 37, 37.5, 39)
Temp_in_F = list(map(convert_to_F, Temp_in_C))
print("List of temperature in Celsius : ", Temp_in_C)
print("List of temperature in Fahrenheit : ", Temp_in_F)