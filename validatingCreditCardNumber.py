import re
for _ in range(int(input())):
    value = input()
    valid_structure = re.match(r"^[4-6](\d{15}|\d{3}(-\d{4}){3}$)",value)
    consecutive_repeat = re.compile(r"(\d)\1{3}")
    print("Valid" if valid_structure and not consecutive_repeat.search(value.replace("-","")) else "Invalid")
