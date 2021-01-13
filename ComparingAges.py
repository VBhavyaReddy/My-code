print("Enter Your Father's age: ")
father_age = int(input())
print("Enter Your Mother's age: ")
mother_age =  int(input())
print("Enter Your Sister's / Brother's age: ")
sis_or_bro_age = int(input())
print("Enter Your age: ")
Your_age =  int(input())
print("Enter Your Friend's dad's age: ")
friends_dads_age = int(input())
print("Enter Your Friend's mom's age: ")
friends_moms_age = int(input())
print("Enter Your Friend's sister's / Brother's age: ")
friends_sis_or_bro_age = int(input())
print("Enter Your Friend's age: ")
friends_age = int(input())
print("Your Father's age is " + str(father_age))
print("Your Mother's age is " + str(mother_age))
print("Your Sister's age is " + str(sis_or_bro_age))
print("Your age is " + str(Your_age))
print("Your Friend's Dad's age is " + str(friends_dads_age))
print("Your Friend's Mom's age is " + str(friends_moms_age))
print("Your Friend's Sister's age is " + str(friends_sis_or_bro_age)) 
print("Your Friend's age is " + str(friends_age))
w = mother_age - Your_age
x = father_age - Your_age
y = mother_age - sis_or_bro_age
z = father_age - sis_or_bro_age
if sis_or_bro_age > Your_age:
 diff = sis_or_bro_age - Your_age
elif Your_age > sis_or_bro_age:
    diff = Your_age - sis_or_bro_age
p = friends_moms_age - friends_age
q = friends_dads_age - friends_age
r = friends_moms_age - friends_sis_or_bro_age
s = friends_dads_age - friends_sis_or_bro_age
if friends_sis_or_bro_age > friends_age:
    res = friends_sis_or_bro_age - friends_age
elif friends_age > friends_sis_or_bro_age:
    res = friends_age - friends_sis_or_bro_age
print("You were born when your mother was " + str(w) + " years old")
print("You were born when your father was " + str(x) + " years old") 
print("Your Brother / sister was born when your mother was " + str(y) + " years old")
print("Your Brother / sister was born when your father was " + str(z) + " years old")
print("Your Friend was born when his/her mother was " + str(p) + " years old")
print("Your Friend was born when his/her father was " + str(q) + " years old") 
print("Your Friend's sister / brother was born when their mother was " + str(r) + " years old")
print("Your Friend's sister / brother was born when their father was " + str(s) + " years old")
if friends_dads_age > father_age:
    print("Your Friend's Father is older than Your Father ")
elif friends_dads_age == father_age:
    print("Your Friend's Father and Your Father are of the same age ")
else:
    print("Your Father is older than Your Friend's Father")
if friends_moms_age > mother_age:
    print("Your Friend's mother is older than Your Mother ")
elif friends_moms_age == mother_age:
    print("Your Friend's mother and Your Mother are of the same age")
else:
    print("Your Mother is older than Your Friend's mother")
if friends_sis_or_bro_age > sis_or_bro_age:
    print("Your Friend's sister /  brother is older than Your Sister / Brother ")
elif friends_sis_or_bro_age == sis_or_bro_age:
    print("Your Friend's sister / brother and Your Sister / brother are of the same age")
else:
    print("Your Sister / brother is older than Your Friend's sister / brother")
if friends_age > Your_age:
    print("Your Friend is older than You")
elif friends_age == Your_age:
    print("Your Friend and You are of the same age ")
else:
    print("You are older than Your Friend")
