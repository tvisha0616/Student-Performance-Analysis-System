 
SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "Computer"]

class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name



class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.__marks = marks

    def get_mark(self, subject):
        return self.__marks[subject]

    def total(self):
        return sum(self.__marks.values())

    def average(self):
        return self.total() / len(self.__marks)

    def lowest_mark(self):
        return min(self.__marks.values())

    def subjects_below(self, limit=40):
        return sum(
            1 for m in self.__marks.values() if m < limit
        )

    def grade(self):
        return assign_grade(self.average())



def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    elif avg >= 50:
        return "F"
    else:
        return "E"



def decide_action(s):
    if s.average() >= 50:
        if s.lowest_mark() >= 40:
            if s.average() >= 75:
                return "EXCELLENT - advanced track"
            else:
                return "GOOD - on track"
        else:
            return "OK overall - remedial help in weak subject"
    else:
        if s.subjects_below(40) >= 3:
            return "AT RISK - counselling + remedial classes"
        else:
            return "WEAK - extra support"



def subject_averages(students):
    return {
        sub: sum(s.get_mark(sub) for s in students) / len(students)
        for sub in SUBJECTS
    }



def find_extremes(students):
    top = max(students, key=lambda s: s.average())
    low = min(students, key=lambda s: s.average())
    return top, low



def print_report(students):

    print("\nSTUDENT PERFORMANCE ANALYSIS REPORT")
    print("=" * 75)

    print(
        f"{'Name':<12}{'Total':<10}"
        f"{'Avg':<10}{'Grade':<10}Action"
    )

    print("=" * 75)

    for s in students:
        print(
            f"{s.get_name():<12}"
            f"{s.total():<10}"
            f"{s.average():<10.1f}"
            f"{s.grade():<10}"
            f"{decide_action(s)}"
        )

    print("\nSUBJECT AVERAGES")
    print("-" * 30)

    for sub, avg in subject_averages(students).items():
        print(f"{sub}: {avg:.1f}")

    top, low = find_extremes(students)

    print("\nTOPPER AND LOWEST PERFORMANCE")
    print("-" * 40)

    print(f"Topper: {top.get_name()} ({top.average():.1f})")
    print(f"Lowest: {low.get_name()} ({low.average():.1f})")

    print("=" * 75)



data = {
    "Aman": [85, 78, 82, 88, 91],
    "Simran": [23, 24, 34, 45, 20],
    "Rahul": [65, 68, 60, 74, 70],
    "Neha": [92, 89, 94, 90, 96],
    "Karan": [45, 56, 34, 23, 30],
}



students = [
    Student(n, dict(zip(SUBJECTS, m)))
    for n, m in data.items()
]



print_report(students)