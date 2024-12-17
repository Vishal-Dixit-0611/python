# Create a class with a class attribute a; Create an object from it and set a directly using object.a = 0. Does this change the class attribute.

class test:
    a = "Vishal"
    language = "Python"

# z = test()
object = test()
print(object.a, object.language)
object.a = 0
print(object.a, object.language)



