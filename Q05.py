# --- PART 1: VALID IDENTIFIERS ---
# Identifiers can contain letters (a-z, A-Z), digits (0-9), and underscores (_).
# They must start with a letter or an underscore.

student_name = "Aarav"       # Valid: lowercase letters and underscore
_rollNumber = 101            # Valid: starts with underscore, uses camelCase
marks2 = 95.5                # Valid: contains digits (not at the start)
TOTAL_SCORE = 500            # Valid: all uppercase letters

print("--- Valid Identifiers ---")
print("Student Name:", student_name)
print("Roll Number:", _rollNumber)
print("Marks 2:", marks2)
print("Total Score:", TOTAL_SCORE)


# --- PART 2: INVALID IDENTIFIERS ---
# Uncommenting any of the lines below will raise a SyntaxError when run:

# 1st_rank = "Riya"          # Invalid: cannot start with a digit
# student-age = 16           # Invalid: hyphens (-) are not allowed
# total marks = 450          # Invalid: spaces are not allowed
# class = "10th"             # Invalid: 'class' is a reserved Python keyword
# user@email = "a@b.com"     # Invalid: special characters like @ are not allowed


# --- PART 3: CHECKING IDENTIFIERS DYNAMICALLY ---
# Using Python's built-in .isidentifier() method and keyword module
import keyword

print("\n--- Testing Identifier Validity ---")
test_names = ["student_name", "1st_rank", "_rollNumber", "student-age", "class", "marks2"]

for name in test_names:
    if name.isidentifier() and not keyword.iskeyword(name):
        print(f"'{name}' -> VALID identifier")
    else:
        print(f"'{name}' -> INVALID identifier")
