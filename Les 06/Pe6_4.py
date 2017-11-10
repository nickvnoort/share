studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
def gemiddelde_per_student(studentencijfers):
 antwoord = []
 for student in range(len(studentencijfers)):
     number = studentencijfers[student]
     antwoord.append(sum(number) / len(number))
 return antwoord

def gemiddelde_van_alle_studenten(studentencijfers):
 list = []
 antwoord = 0
 for student in range(len(studentencijfers)):
     number = studentencijfers[student]
     list.append(sum(number) / len(number))
 for row in range(len(list)):
    antw = antwoord + list[row]

 return antwoord / len(list)

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))