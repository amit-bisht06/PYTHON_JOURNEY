# Using *args (variable number of arguments) -->If you do not know how many arguments that will be passed into your function, add a *️⃣  before the parameter name in the function definition.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
def sum_elements(*elements):
    result = 0
    for num in elements:
        result +=num
    return result

print(sum_elements(10,20,30))
print(sum_elements(10,20))
print(sum_elements(10))
print(sum_elements()) 
#---------------------------------------------------------------------------------

# Arbitrary Keyword Arguments, Using **kwargs --> If the number of keyword arguments is unknown, add a double ** before the parameter name
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

student_info(name="Amit", age=21, course="CSE")