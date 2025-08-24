#write a fun to return div based on marks
#below 30->F
#3 to 44-->3rd
#45 to 59->2nd
#60 or above>1st

def division(marks):
    if marks<30:
        return "fail"
    elif marks>=30 and marks<45:
        return "3rd"
    elif marks>=45 and marks<60:
        return "2nd"
    else:
        return "1st"

def division(marks):
    if marks<30:
        res="fail"
    elif marks>=30 and marks<45:
        res="3rd"
    elif marks>=45 and marks<60:
        res="2nd"
    else:
        res="1st"

    return res

print(division(56))#2nd div
print(division(26))#Fail
print(division(76))#1st div


