
# Examination Result and Grace-Mark Validation

n = int(input("Enter number of subjects: "))
max_marks = float(input("Enter maximum marks per subject: "))
pass_marks = float(input("Enter minimum passing marks: "))
grace_limit = float(input("Enter maximum grace marks allowed per subject: "))

subjects = {}
total = 0
passed = 0
failed = 0

for i in range(n):
    subject = input(f"\nEnter subject {i + 1} name: ")
    marks = float(input("Enter marks obtained: "))

    if marks < 0 or marks > max_marks:
        print("Invalid marks! Enter marks within the valid range.")
        continue

    grace = 0

    # Apply grace marks only if the student is short of passing
    if marks < pass_marks:
        required = pass_marks - marks

        if required <= grace_limit:
            grace = required

    final_marks = min(marks + grace, max_marks)

    if final_marks >= pass_marks:
        result = "PASS"
        passed += 1
    else:
        result = "FAIL"
        failed += 1

    subjects[subject] = (marks, grace, final_marks, result)
    total += final_marks

# Display subject-wise results
print("\n------ FINAL EXAMINATION RESULT ------")

for subject, data in subjects.items():
    marks, grace, final_marks, result = data

    print(f"\nSubject: {subject}")
    print("Original marks:", marks)
    print("Grace marks:", grace)
    print("Final marks:", final_marks)
    print("Result:", result)

# Calculate percentage and classification
valid_subjects = len(subjects)

if valid_subjects > 0:
    percentage = total / (valid_subjects * max_marks) * 100

    print("\nTotal marks:", total)
    print("Percentage:", round(percentage, 2), "%")
    print("Subjects passed:", passed)
    print("Subjects failed:", failed)

    if failed > 0:
        classification = "FAIL"
    elif percentage >= 75:
        classification = "Distinction"
    elif percentage >= 60:
        classification = "First Class"
    elif percentage >= 50:
        classification = "Second Class"
    else:
        classification = "Pass Class"

    print("Final Classification:", classification)
else:
    print("No valid subject marks entered.")
