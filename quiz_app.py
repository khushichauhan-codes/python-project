print("===== PYTHON QUIZ =====")

score = 0

q1 = input("1. Which keyword is used for exception handling? (try/catch): ")

if q1.lower() == "try":
    score += 1

q2 = input("2. Which operator is used for equality check? (==/=): ")
if q2.lower() == "==":
    score += 1


q3 = input("3.Which collection allows duplicate values? (list/set) : ")

if q3.lower() == "list":
    score += 1

print("\nQuiz Completed!")
print("Your Score:", score, "/3")

if score == 3:
    print("Excellent!")
elif score == 2:
    print("Good Job!")
else:
    print("Keep Practicing!")