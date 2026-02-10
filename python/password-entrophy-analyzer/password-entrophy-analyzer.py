import math
from colorama import init, Fore, Style
init(autoreset=True)

# Strength categories with predictability tags
def classify_strength(entropy):
    if entropy < 28:
        return "Very Weak ❌", "(Highly Predictable)"
    elif entropy < 36:
        return "Weak ⚠️", "(Predictable)"
    elif entropy < 60:
        return "Reasonable ✅", "(Moderately Predictable)"
    elif entropy < 128:
        return "Strong 🔒", "(Unpredictable)"
    else:
        return "Uncrackable 🔥", "(Unpredictable)"

# Estimate crack time
def estimate_crack_time(entropy):
    guesses = 2 ** entropy
    guesses_per_second = 1e10  # 10 billion guesses per second
    seconds = guesses / guesses_per_second

    if seconds < 1e-3:
        return f"{seconds * 1000:.2f} ms"
    elif seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds / 60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds / 3600:.2f} hours"
    elif seconds < 31557600:
        return f"{seconds / 86400:.2f} days"
    elif seconds < 3.154e12:
        return f"{seconds / 31557600:.2f} years"
    else:
        return f"{seconds / 3.154e12:.2f} centuries"

# Character set size calculation
def get_charset_size(password):
    size = 0
    if any(c.islower() for c in password):
        size += 26
    if any(c.isupper() for c in password):
        size += 26
    if any(c.isdigit() for c in password):
        size += 10
    if any(c in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in password):
        size += 32
    if any(c.isspace() for c in password):
        size += 1
    return size if size > 0 else 1

# Entropy calculation
def calculate_entropy(password):
    charset_size = get_charset_size(password)
    return len(password) * math.log2(charset_size)

# Main execution
print("\nWhat is entropy?")
print(Fore.GREEN + Style.BRIGHT + "Entropy is a measure of uncertainty or randomness in a system.")
print(Fore.GREEN + "In the context of passwords, it quantifies how unpredictable a password is,")
print(Fore.GREEN + "making it harder for attackers to guess. " + Fore.YELLOW + "Higher entropy = stronger security.\n")

passwords = [input(f"Enter password {i+1} to analyze: ") for i in range(4)]

print("\n" + "="*50)
print(Fore.CYAN + Style.BRIGHT + "Analyzing your passwords...\n")

results = []
for pwd in passwords:
    entropy = calculate_entropy(pwd)
    strength, predictability = classify_strength(entropy)
    crack_time = estimate_crack_time(entropy)
    
    print(Fore.MAGENTA + Style.BRIGHT + f"Analyzing password: " + Fore.WHITE + f"{pwd}")
    print(Fore.YELLOW + f"Entropy: {entropy:.2f} bits")
    print(Fore.BLUE + f"Strength: " + Fore.WHITE + f"{strength}")
    print(Fore.RED + f"Estimated crack time: " + Fore.WHITE + f"{crack_time} " + Fore.LIGHTBLACK_EX + f"{predictability}")
    print(Fore.GREEN + "-"*50)
    
    results.append((pwd, entropy, strength, crack_time, predictability))

# Comparison chart
print("\n" + "="*50)
print(Fore.CYAN + Style.BRIGHT + "Password Strength Comparison Chart")
print(Fore.CYAN + "="*50)
print(Fore.YELLOW + f"{'Password':25} {'Entropy(bits)':15} {'Strength':20} {'Est. Crack Time'}")
print(Fore.GREEN + "-"*85)

for pwd, entropy, strength, crack_time, predictability in results:
    short_pwd = pwd if len(pwd) <= 20 else pwd[:17] + "..."
    print(Fore.WHITE + f"{short_pwd:25} " + Fore.YELLOW + f"{entropy:15.2f} " + Fore.BLUE + f"{strength:20} " + Fore.RED + f"{crack_time} " + Fore.LIGHTBLACK_EX + f"{predictability}")