# 1 Lbs = 0.45 Kg
#1 kg = 2.205 Lbs
weight = float(input("Enter your weight"))
choice = input("Enter k (Kg) or l (Lbs)")
if choice == 'k':
    final_weight = weight * 2.205
    print(f"Your weight is {final_weight} Pounds")
elif choice == 'l':
    final_weight = weight * 0.456
    print(f"Your weight is {final_weight} Kg")
else:
    print("I cannot find this option :( ")