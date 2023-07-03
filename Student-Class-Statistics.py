from statistics import mean

class School:
    def __init__(self):
        self.n = int(input())

        self.sen = input().split()
        for i in range(len(self.sen)):
            self.sen[i] = int(self.sen[i])

        self.ghad = input().split()
        for j in range(len(self.ghad)):
            self.ghad[j] = int(self.ghad[j])

        self.vazn = input().split()
        for k in range(len(self.vazn)):
            self.vazn[k] = int(self.vazn[k])
        
    def miangin_kardan(self):
        print("{:.1f}".format(mean(self.sen)))
        print("{:.1f}".format(mean(self.ghad)))
        print("{:.1f}".format(mean(self.vazn)))
    
    def get_student_count(self):
        return self.n
    
A = School()
B = School()

A.miangin_kardan()
B.miangin_kardan()

if mean(A.ghad) > mean(B.ghad):
    print('A')
elif mean(A.ghad) < mean(B.ghad):
    print('B')
else:
    if mean(A.vazn) < mean(B.vazn):
        print('A')
    elif mean(A.vazn) > mean(B.vazn):
        print('B')
    else:
        print('Same')

print("Number of students in School A:", A.get_student_count())
print("Number of students in School B:", B.get_student_count())
