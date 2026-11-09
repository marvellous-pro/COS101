#70–100 A
#60 to below 70 B
#50 to below 60 C
#45 to below 50 D
#40 to below 45 E
#0 to below 40 F


print("student result checker")
print("======================")

name=input("enter student name:")
work=int(input("enter course work between 0 and 30:"))
score=int(input("enter examination score between 0 and 70:"))
if score <= 0 and score >= 70:
    print("score is invalid!")
else:
    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 45:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else:
        grade = "F"

print(f"course work = {work}")
print(f"examination score = {score}")




total = work + score
print(f"{work} + {score} = {total}")

if total >=50:
    print("decision: pass")
else:
    print("decicion: resit required!")
    

