
import re       

import pyautogui


def is_strong_password(password):

    messages= []

    if len(password)< 8:                 
        messages.append("Password is less than 8 characters.")
    
    if not any(c.isupper() for c in password):   
       messages.append("Password is missing an uppercase letter.")


    if not any(c.islower() for c in password):      
        messages.append("Password is missing a lowercase letter.")


    if not any(c.isdigit() for c in password):          
       messages.append("Password is missing a digit.")


    if not re.search(r'[!@#\$%^&*()_+{}\[\]:;<>,.?~\\\-]',password):
       messages.append("Password is missing a special charecter.")

    common_passwords = ["password", "123456", "qwerty", "letmein"]

    if password in common_passwords:
       messages.append("Common password.")
    
    if messages:
        return "\n".join(messages)
    else:
        return "Strong password!"
    


def main():
    password= pyautogui.password("Enter your password")
    result= is_strong_password(password)

    if "Strong" in result:
        print(result)
    
    else:
        print(f"Weak Password. Reasons:\n{result}")
    
if __name__ == "__main__":
    main()

    
