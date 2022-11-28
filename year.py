class LeapYear:
    def __init__(self) -> None:
        self.year = int(input("What year do you want to test? "))

    def checkLeapYear(self) -> bool:
        divideByFour = self.year%4
        divideBy100 = self.year%100
        divideBy400 = self.year%400

        if divideByFour == 0:
            if divideBy100 == 0:
                if divideBy400 == 0:
                    print(f"The year {self.year} is a leap year")
                elif divideBy400 != 0:
                    print(f"The year {self.year} is not a leap year")
        else:
            print(f"The year {self.year} is not a leap year.")