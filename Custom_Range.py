class CustomRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end :
            current = self.start
            self.start += self.step
            return current
        else:
            raise StopIteration
        

fuck = CustomRange(10, 50, 4)

for i in fuck:
    print(i)