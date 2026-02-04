# step 1:
account = {
    'pin':4511,
    'accountbalance':484848,
    'username':'Sanket'
}

print("Welcome")

pincode = int(input("Enter your 4 Digit Pin"))
if pincode == account('pin'):
    print("Correct Pin:")
else:
    print("Enter a pin again")




