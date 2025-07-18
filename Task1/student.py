class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects  # dict {subject: score}
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()

    def calculate_average(self):
        if not self.subjects:
            return 0
        return sum(self.subjects.values()) / len(self.subjects)

    def calculate_grade(self):
        avg = self.average
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def to_dict(self):
        return {
            "name": self.name,
            "subjects": self.subjects,
            "average": self.average,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(data):
        return Student(data["name"], data["subjects"])
