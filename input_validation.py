def Main():
    while(True): 
        age = input("Enter your age in numbers(1-120) : ")
        if(age.isdigit() and 1 <= int(age) <= 120):
            print(f"Your age is {age}.")
            break
        else:
            print("Invalid input. Please enter a valid age between 1 and 120.")
        







if __name__ == "__main__":
    print("library: modular_program_design")
    Main()