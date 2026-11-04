# Employee Profile Generator

print("#=====EMPLOYEE PROFILE=====#")

#Gather employee detail.
name=input("enter employee name: ")
age= int(input("enter employee age: "))
experience= float(input("experiance: "))
current_role= input("enter current role: ")
company= input("enter company: ")

# Display employee information

print("\n===== EMPLOYEE DETAILS =====")

print("Name: ", name)
print("Age: ", age)
print("Experience: ", experience)
print("Current role: ", current_role)
print("Company: ", company)


#Display the Data types

print("\n ===== Data Types =====")

print("Name: ", type(name) )
print("Age: ", type(age ))
print("Experience: ", type(experience))
print( "Current role: ",type(current_role))
print("company: ", type(company))


