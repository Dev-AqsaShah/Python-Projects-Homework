def energy():
    c: int = 299792458  # Speed of light in meters per second
    a: float = float(input("Enter mass in kilograms: "))  # Corrected variable name
    print("E = m * C^2")
    print("Mass = " + str(a) + " kg")  # Fixed variable reference and type conversion
    print("C = " + str(c) + " m/s")  # Fixed capitalization
    print("E = " + str(a * c ** 2) + " joules")  # Corrected power operator and variable name

if __name__ == "__main__":
    energy()
