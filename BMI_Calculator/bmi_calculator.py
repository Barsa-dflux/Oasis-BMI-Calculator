#BMI Calculator with Health Advice and Report Saving

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def health_advice(category):
    advice = {
        "Underweight": "You should eat a balanced diet and consult a nutritionist.",
        "Normal Weight": "Great! Maintain your healthy lifestyle.",
        "Overweight": "Regular exercise and a healthy diet are recommended.",
        "Obese": "Consult a healthcare professional for guidance."
    }
    return advice[category]

print("=" * 50)
print("         ADVANCED BMI CALCULATOR")
print("=" * 50)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (Male/Female): ")

weight = float(input("Enter your weight (kg): "))
height_cm = float(input("Enter your height (cm): "))

height_m = height_cm / 100

bmi = calculate_bmi(weight, height_m)
category = bmi_category(bmi)

print("\n" + "=" * 50)
print("               BMI REPORT")
print("=" * 50)

print(f"Name     : {name}")
print(f"Age      : {age}")
print(f"Gender   : {gender}")
print(f"Weight   : {weight} kg")
print(f"Height   : {height_cm} cm")
print(f"BMI      : {bmi:.2f}")
print(f"Category : {category}")

print("\nHealth Advice:")
print(health_advice(category))

print("=" * 50)

save = input("\nDo you want to save the report? (yes/no): ")

if save.lower() == "yes":
    with open("BMI_Report.txt", "w") as file:
        file.write("BMI REPORT\n")
        file.write("=" * 30 + "\n")
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Gender: {gender}\n")
        file.write(f"Weight: {weight} kg\n")
        file.write(f"Height: {height_cm} cm\n")
        file.write(f"BMI: {bmi:.2f}\n")
        file.write(f"Category: {category}\n")
        file.write(f"Advice: {health_advice(category)}\n")

    print("Report saved successfully as BMI_Report.txt")

print("\nThank you for using BMI Calculator!")