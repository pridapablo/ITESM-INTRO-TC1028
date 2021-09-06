# El programa va a preguntar por una calificación numerica, entre 0 y 100.
# Añade el código necesario para que el programa imprima Pass si la calificación es mayor o igual a 70,
# o que imprima Fail si la calificación es menor a 70.

# La salida del programa debe de ser exactamente de la siguiente forma:

# Enter grade: 90
# Pass

def check_grade(grade):
    if grade >= 70:
        return "Pass"
    elif grade < 70:
        return "Fail"


def main():
    grade = int(input("Enter grade: "))
    print(check_grade(grade))


if __name__ == '__main__':
    main()