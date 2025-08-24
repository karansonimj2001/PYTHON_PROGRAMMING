def division(marks):
    if marks<30:
        return "fail"
    else:
        return "pass"
    

print(division(46))
print(division(16))

def division(marks:float)->str:
    if marks<30:
        return "fail"
    else:
        return "pass"

print(division(46))
print(division(16))
