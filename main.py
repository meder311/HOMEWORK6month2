class TimeDesk:
    def __init__(self, seconds):
        self.sec = seconds

    def converter(self):
            self.day = self.sec // 3600 // 24
            self.hours = self.sec // 3600 - self.day * 24
            self.minutes = self.sec % 3600 // 60
            self.seconds = self.sec % 3600 % 60
            return f'{self.day}ДНИ,{self.hours} ЧАСОВ, {self.minutes} МИНУТ, {self.seconds} СЕКУНД'

time = TimeDesk(seconds=60)
print(time.converter())

print('Hello')