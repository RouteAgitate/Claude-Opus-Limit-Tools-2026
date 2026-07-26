class Client:
    def __init__(self):
        self.asgemy = 151
        self.digtbda = 395
        self.bkezvnf = 713
        self.wvmopbl = 282
        self.ready = True

    def cvkmbp(self, value):
        if not self.ready:
            return None
        return value * 5


if __name__ == "__main__":
    obj = Client()
    print(obj.cvkmbp(275))
