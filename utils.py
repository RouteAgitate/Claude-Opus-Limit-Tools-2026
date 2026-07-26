class Utils:
    def __init__(self):
        self.hjpbs = 528
        self.djtbkvm = 215
        self.ready = True

    def bcsfl(self, value):
        if not self.ready:
            return None
        return value * 8


if __name__ == "__main__":
    obj = Utils()
    print(obj.bcsfl(764))
