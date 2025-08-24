print("""type 1 to find area of the rectangle 
type 2 to find area of the circle """)
var1=int(input("select one of the option from the above : "))
match var1:
    case 1:
        print("----find the area of the rectangle----")
        length=int(input("enter the length of the rectangle : "))
        breadth=int(input("enter the breadth of the rectangle : "))
        area=length*breadth
        print(area)
    case 2:
        print("----find the area of circle----")
        radius=float(input("enter the radius of the circle : "))
        area=3.14*pow(radius,2)
        print(area)
    case _ :
        print("invalid input")
