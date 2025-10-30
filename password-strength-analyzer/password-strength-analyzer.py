import string
from colorama import Fore, Style, Back, init
init(autoreset=True)

inp = input("Enter a password: ")
flag = input("Do you want to see the reasons for the score? (yes/no)[Add --why for detail]: ").strip().lower()
suggestionIF = input("Do you want suggestions for a stronger password? (yes/no): ").strip().lower()
score = 0
reason = ""
suggestion = ""

    


if len(inp) >= 8:
    score += 1
    reason += "Length is sufficient.\n"
else:
    suggestion += "Consider making your password at least 8 characters long.\n"
if any(char.isdigit() for char in inp):
    score += 1
    reason += "Contains a digit.\n"
else:
    suggestion += "Consider adding numbers to your password.\n"
if any(char.islower() for char in inp):
    score += 1
    reason += "Contains a lowercase letter.\n"
else:
    suggestion += "Consider adding lowercase letters to your password.\n"
if any(char.isupper() for char in inp):
    score += 1
    reason += "Contains an uppercase letter.\n"
else:
    suggestion += "Consider adding uppercase letters to your password.\n"
if any(char in string.punctuation for char in inp):
    score += 1
    reason += "Contains a special character.\n"
else:
    suggestion += "Consider adding special characters to your password.\n"
    
    
if score < 3:
    print(Fore.MAGENTA + Style.BRIGHT + "Weak password")
elif score == 3:
    print(Fore.YELLOW + Style.BRIGHT + "Moderate password")
elif score == 4:
    print(Fore.BLUE + Style.BRIGHT + "Strong password")
elif score == 5:
    print(Fore.GREEN + Style.BRIGHT + "Very strong password")
else:
    print(Fore.RED + Style.BRIGHT + "Invalid input")
    
    
if suggestion == "":
    suggestion = "Your password is already strong. No suggestions needed."

if 'yes' in flag:
    print(Back.GREEN + "Reasons for score:")
    print(Back.GREEN + reason)
    
if " --why" in flag:
    print(Back.GREEN + "You have requested to know the reasons if your password is weak.")
    print(Back.GREEN +Fore.RED + Back.WHITE + Style.BRIGHT +  suggestion)
    
    
if suggestionIF == 'yes':
    print(Fore.RED + Back.WHITE + Style.BRIGHT + "Suggestions for a stronger password:")
    print(Fore.RED + Back.WHITE + Style.BRIGHT + "- Use a mix of uppercase and lowercase letters.")
    print(Fore.RED + Back.WHITE + Style.BRIGHT + "- Include numbers and special characters.")
    print(Fore.RED + Back.WHITE + Style.BRIGHT + "- Ensure the password is at least 8 characters long.")
    print(Fore.RED + Back.WHITE + Style.BRIGHT + "- Avoid common words or easily guessable information.")
    print(Fore.RED + Back.WHITE + Style.BRIGHT + "- Avoid using the same password across multiple accounts.")
    print(Fore.RED + Back.WHITE + Style.BRIGHT + "- Avoid using personal information such as names or birthdays.")
    print(Fore.RED + Back.WHITE + Style.BRIGHT + "- Consider using a passphrase that is easy to remember but hard to guess.")
    print(Fore.RED + Back.WHITE + Style.BRIGHT + "- Consider using a longer passphrase for added security.")
    print(Fore.RED + Back.WHITE + Style.BRIGHT + "- Consider using a passphrase for better security.")
    print(Fore.RED + Back.WHITE + Style.BRIGHT + "- Regularly update your password to maintain security.")
    print(Fore.RED + Back.WHITE + Style.BRIGHT + "- Use a password manager to keep track of complex passwords.")
    