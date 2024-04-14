# The following program demonstrates how to use tuples and dictionaries.
# Tuples
a_tuple = ("Hello", 123, 5.0)
print(a_tuple)
print(a_tuple[0])

a_list = [("ABC", 123), ("Def", 456), ("XYZ", 890)]
print(a_list)
print(a_list[0][1])

# Dictionaries
student_ids = {"Rei": 1234, "Alexis": 6789}
print(student_ids["Alexis"])
# Add new student
student_ids["Ethan"] = 1011
print(student_ids)