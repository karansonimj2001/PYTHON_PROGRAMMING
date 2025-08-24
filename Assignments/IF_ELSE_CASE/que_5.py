# sub1=int(input("enter the marks of social studies "))
# sub2=int(input("enter the marks of science "))
# sub3=int(input("enter the marks of hindi "))
# sub4=int(input("enter the marks of english "))
# sub5=int(input("enter the marks of maths "))
# earned_marks=sub1+sub2+sub3+sub4+sub5

print("----find the percentage of the given number----")
earned_marks=int(input("enter the total marks here : "))
percentage=int((earned_marks/500)*100)
print(percentage)
if percentage>=60:
    print("First Devision.")
elif percentage>=50 and percentage<60:
    print("Second Devision.")
elif percentage>=40 and percentage<=50:
    print("Third Devision.")
elif percentage<40:
    print("Fail.")