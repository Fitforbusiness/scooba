def multiply(a,b):
    return a*b
yo = multiply (2,3)
print (yo)
#dual functions
def greeting (name,department):
    print ("welcome " + name)
    print ("you are part of " + department)
greeting ("chad", "IT support")
def new_employee (favorite_dog, favorite_vacation):
    print ("We love your favorite dog is a" + favorite_dog)
    print ("One day we are sending you to" + favorite_vacation)
new_employee (" yorkie"," Hawaii")
def speaking_to_family (family_name,holiday):
    print ("Hello, "+ family_name)
    print ("Happy " + holiday)
speaking_to_family ("Mandy","Easter")
def area_triangle (base,height):
    return base*height/2
area_a = area_triangle (5,4)
area_b = area_triangle (7,3)
sum = area_a + area_b
print ("The sum of both areas is: "+ str(sum))
def area_square (height,base):
    return base*height
area1 = area_square (5,4)
area2 = area_square (2,3)
sum = area1 + area2
print ("The area of the squares is:" + str(sum))
pie = 3.14
def area_circle (pie,r):
    return float(pie)*r**2
area11 = area_circle (pie,3)
area22 = area_circle (pie,2)
sum1 = area11+area22
print ("The area of both circles combined: " +str(sum1))
#coursera
def get_seconds (hours,minutes,seconds):
    return 3600*hours+60*minutes+seconds
amount_a = get_seconds (2,30,0)
amount_b = get_seconds (0,45,15)
result = amount_a + amount_b
print (result)
def convert_seconds (seconds1):
    hours1 = seconds1// 3600
    minutes1 = (seconds1 - hours1*3600)//60
    remining_seconds = seconds1 - hours1 * 3600 - minutes1 * 60
hours1, minutes1, seconds1 = convert_seconds (5000)
print (hours1, minutes1, seconds1)







