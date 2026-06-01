#.SECTION 4 : DATA STRUCTURES
#1.FAVORITE TOOLS LIST
print("FAVORITE TOOLS LIST :")
favorite_tools = []
num_tools = int(input("How many favorite tools do you want to add? : "))
for i in range(num_tools):
    tool = input(f"Enter tool {i+1} : ")
    favorite_tools.append(tool)
print("Your favorite tools are : ", favorite_tools)


#2. STUDENT SCORES
print("STUDENT SCORES :")
student_scores = {}
num_students = int(input("How many students do you want to add? : "))
for i in range(num_students):
    name = input(f"Enter name of student {i+1} : ")
    score = float(input(f"Enter score of {name} : "))
    student_scores[name] = score
print("Student Scores : ", student_scores)


#3. SHOPPING LIST MANAGER
print("SHOPPING LIST MANAGER :")
shopping_list = []
while True:
    item = input("Enter an item to add to the shopping list (or type 'done' to finish) : ")
    if item.lower() == 'done':
        break
    shopping_list.append(item)
print("Your shopping list : ", shopping_list)


#4. CONTRY CAPITALS
print("COUNTRY CAPITALS :")
country_capitals = {}
num_countries = int(input("How many countries do you want to add? : "))
for i in range(num_countries):
    country = input(f"Enter name of country {i+1} : ")
    capital = input(f"Enter capital of {country} : ")
    country_capitals[country] = capital
print("Country Capitals : ", country_capitals)


#5. UNIQUE VISITORS
print("UNIQUE VISITORS :")
unique_visitors = set()
num_visitors = int(input("How many unique visitors do you want to add? : "))
for i in range(num_visitors):
    visitor = input(f"Enter name of visitor {i+1} : ")
    unique_visitors.add(visitor)
print("Unique Visitors : ", unique_visitors)

#6. COMMON SKILLS
print("COMMON SKILLS :")
skills_set1 = set(input("Enter skills for person 1 (comma separated) : ").split(","))
skills_set2 = set(input("Enter skills for person 2 (comma separated) : ").
split(","))
common_skills = skills_set1.intersection(skills_set2)
print("Common Skills : ", common_skills)


#7. STUDENT RECORDS
print("STUDENT RECORDS :")
student_records = []
num_students = int(input("How many student records do you want to add? : "))    
for i in range(num_students):
    name = input(f"Enter name of student {i+1} : ")
    age = int(input(f"Enter age of {name} : "))
    grade = float(input(f"Enter grade of {name} : "))
    student_records.append({"name": name, "age": age, "grade": grade})
