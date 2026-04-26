try:
    Username = input("Enter Username: ")
    if Username == "":
        raise ValueError("Username cannot be empty.")
    
    Age =  input("Enter Age: ")
    Age = int(Age)

    if Age <= 0:
        raise ValueError("Age must be a positive integer.")

    with open("users.txt", "a") as file:
        file.write(f"{Username} - {Age}\n")
        print("\n----User information saved to file.-----")

    with open("users.txt", "r") as file:
        print("\nUsers file:")
        print(file.read())


except FileNotFoundError:
        print("File not found.")
except Exception as e:
        print("An error has occurred:", e)

finally:
       print("System complete")