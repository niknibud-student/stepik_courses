import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, data):
        super(LoggableList, self).append(data)
        self.log(data)

x = LoggableList()
x.append(3)