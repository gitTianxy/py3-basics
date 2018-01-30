class Cls1:
    def __init__(self, title):
        self.title = title

    def display(self):
        print "This is the ", self.title


class Cls2:
    def __init__(self):
        pass

    @staticmethod
    def display():
        print "This is class 2"
