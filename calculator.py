import time

def calculate_bmi(weight, height):
    """Calculate BMI"""
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """Return BMI Category"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("       🩺 BMI CALCULATOR")
    

    name = input("Enter your name: ")
    height = float(input("Enter your height (in meters): "))
    weight = float(input("Enter your weight (in kilograms): "))

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print("\nCalculating your BMI...")
    time.sleep(1)

    print(f"\n👤 Name: {name}")
    print(f"📏 Height: {height} m")
    print(f"⚖️ Weight: {weight} kg")
    print(f"💪 BMI: {bmi:.2f}")
    print(f"✅ Category: {category}")

    # Save to file
    with open("results.txt", "a") as file:
        file.write(f"{name} - BMI: {bmi:.2f} ({category})\n")

    print("\n✅ Your result has been saved in 'results.txt'")

if __name__ == "__main__":
    main()
