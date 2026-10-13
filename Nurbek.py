js_students = {"Vali", "Malika", "Jasur", "Madina", "Ali"}
python_students = {"Ali", "Vali", "Sardor", "Malika", "Aziza"}

print(js_students)
print(python_students)

jami = js_students.union (python_students)
print("Jami studentlar soni: ", jami)

js_studentlar = js_students.difference(python_students)
print("JS studentlari soni: ", js_studentlar)

py_studentlar = python_students.difference(js_students)
print("PY studentlari soni: ", py_studentlar)

simmetrik = js_students.symmetric_difference(python_students)
print("1 ta kursga boradigan studentlar: ", simmetrik)

ikkala_kurs = js_students.intersection(python_students)
print("students: ", ikkala_kurs)