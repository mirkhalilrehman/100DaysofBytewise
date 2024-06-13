# 10. Temperature Converter
#     - Write a program that can convert temperatures between Celsius, Fahrenheit, and Kelvin.
#     - Expected output: If the input is 20 degrees Celsius, the output should be
#  "20 degrees Celsius is equal to 68 degrees Fahrenheit and 293.15 degrees Kelvin."


# - Celsius to Kelvin: K = °C + 273.15
# - Celsius to Fahrenheit: °F = (°C × 9/5) + 32
a=int(input('Enter temperature in celsius :'))
k=a+273.15
f=(a*(9/5))+32
print(a,' degrees Celsius is equal to',f,' degrees Fahrenheit and ',k,' degrees Kelvin.')