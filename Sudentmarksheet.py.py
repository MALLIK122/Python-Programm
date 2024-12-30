subject = ["Chemistry", "C programming", "Mathematics",
           "Environment", "Electrical and Electronics", "Machine Engineering"]
subjcode = ["CH-102", "MA-111", "CS-107", "EE-101", "ME-101"]
midmarks = []
semmarks = []
count = MTotal = 0

name = input("Enter your name ")
fname = input("Enter your Father name")
rnumber = input("Enter your Roll number ")
college = input("Enter your college name ")

for x in subject:
    a = int(input("Enter midterm marks for " + x))
    b = int(input("Enter semster marks for " + x))
    midmarks.append(a)
    semmarks.append(b)

print("\n\n\t\t****************************** YOUR RESULT ********************************\n\n")
print("\t\tCOLLEGE: ", college)
print("\n\t\tNAME: ", name, "\t\tFATHER NAME: ", fname)
print("\n\t\tROLL NUMBER: ", rnumber)

print("\n\t\t SUBJECTS \tMARKS1 \tMARKS2 \tTOTAL")

for(x, y, z) in zip(subjcode, midmarks, semmarks):
    print("\n\t\t", x, "\t", y, " \t", z, " \t", y+z)
    MTotal = MTotal + y + z
    if y+z < 44:
        count = count + 1

if count == 0:
    print("\n\t\tTOTAL MARKS: ", MTotal, "\t\tRESULT: PASS")
else:
    print("\n\t\tTOTAL MARKS:", MTotal, "\t\tRESULT: FAIL")