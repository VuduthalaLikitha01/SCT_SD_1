def convert_temperature(temp, choice):

    if choice == 1:  # Celsius
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
        print(f"{temp}°C = {fahrenheit:.2f}°F")
        print(f"{temp}°C = {kelvin:.2f} K")

    elif choice == 2:  # Fahrenheit
        celsius = (temp - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{temp}°F = {celsius:.2f}°C")
        print(f"{temp}°F = {kelvin:.2f} K")

    elif choice == 3:  # Kelvin
        celsius = temp - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{temp} K = {celsius:.2f}°C")
        print(f"{temp} K = {fahrenheit:.2f}°F")

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

print("Temperature Converter")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")

temperature = float(input("Enter temperature: "))
choice = int(input("Enter your choice (1/2/3): "))

convert_temperature(temperature, choice)
