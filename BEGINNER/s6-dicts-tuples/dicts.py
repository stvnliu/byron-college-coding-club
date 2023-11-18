# A dictionary in Python is a collection of property names that can be referenced from a parent name.
# Example:
example_dict = {
    "data_1": "value1", # String property
    "data_2": 2235, # Int property
    "data_3": True, # Bool property
    "data_4": [54345, 234, 23233, 111221] # List property
}

# You will learn later that a boolean can be directly referred to in an if-statement
# Writing "if boolean == True: ..." expressions can be less efficient, but it doesn't make much difference
# Usually, it can be better to say directly "if boolean: ...", as it is more concise
print("Executing test program part 1...")
if example_dict["data_3"] == True:
    print(example_dict["data_1"]) # What would this give me?
    print(example_dict["data_2"] - 1255)
    print(example_dict["data_4"][2]) # Which element is this?

# Using dicts inside of dicts and classes are how data structures that can represent
# complex data are constructed. For example:
print("Executing test program part 2...")
school = {
    "school_name": "Byron College",
    "headmaster": "Mr Gallagher",
    "year_groups": [
        {
            "year_name": "Year 7",
            "students": [
                "Fake name 1",
                "Fake name 2",
                "Fake name 3"
            ]
        },
        {
            "year_name": "Year 8",
            "students": [
                "Fake name 4",
                "Fake name 5",
                "Fake name 6"
            ]
        },
    ]
}

# This is a pretty complex data structure referencing the school composition of Byron College
# But the good thing is we can refer to any property in this structure very easily.

# Say I want to get the first student in Year 7
first_year7_student = school["year_groups"][0]["students"][0]

# The code first refers to the property "year_groups" 
# This is school["year_groups"]
print(school["year_groups"])

# and gets the 1st year group in the data (Which is Year 7)
# This is school["year_groups"][0]
print(school["year_groups"][0])

# Then it refers to the list of students
# This is school["year_groups"][0]["students"]
print(school["year_groups"][0]["students"])

# Then it refers to the first student in the list
# This is school["year_groups"][0]["students"][0]
print(school["year_groups"][0]["students"][0])

# Finally it assigns the name of this student to the variable first_year7_student
print(f"Value assigned to variable first_year7_student: {first_year7_student}")