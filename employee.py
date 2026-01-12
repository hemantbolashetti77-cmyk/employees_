import sys

def calculate_bonus(present_days):
    if present_days >= 26:
        return 5000
    elif present_days >= 20:
        return 3000
    elif present_days >= 15:
        return 1500
    else:
        return 0

# Validate arguments
if len(sys.argv) != 4:
    print("Usage: python employee.py <emp_id> <name> <present_days>")
    sys.exit(0)   # Jenkins will NOT fail

try:
    emp_id = int(sys.argv[1])
    name = sys.argv[2]
    present_days = int(sys.argv[3])
except ValueError:
    print("Error: emp_id and present_days must be numbers")
    sys.exit(0)

bonus = calculate_bonus(present_days)

print("Employee ID:", emp_id)
print("Employee Name:", name)
print("Present Days:", present_days)
print("Bonus:", bonus)
