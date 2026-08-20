import datetime
class Person():
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
    def check(self):
        today = datetime.date.today()
        age = today.year - self.dob.year
        if today < datetime.date(today.year, self.dob.month, self.dob.day):
            age -= 1
        if age>=18:
            print(self.name, ", Congratulations...You are eligible to vote.")
        else:
            print(self.name, ", Sorry...You Should be at lease 18 years of age to cast your vote.")
p = Person("Saesha", datetime.date(1998,12, 11))
p.check()