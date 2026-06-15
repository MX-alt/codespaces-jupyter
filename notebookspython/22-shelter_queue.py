from collections import deque

class AnimalShelter:
    def __init__(self):
        # 使用 deque 实现双端队列，高效且线程安全
        self.cats = deque()
        self.dogs = deque()
        self.timestamp = 0  # 递增的时间戳

    def enqueue(self, animal: list[int]) -> None:
        # 存储格式：[编号, 类型, 时间戳]
        record = [animal[0], animal[1], self.timestamp]
        self.timestamp += 1
        
        if animal[1] == 0:  # 猫
            self.cats.append(record)
        else:  # 狗
            self.dogs.append(record)

    def dequeueAny(self) -> list[int]:
        if not self.cats and not self.dogs:
            return [-1, -1]
        
        # 如果有一方为空，直接从另一方出队
        if not self.cats: return self.dequeueDog()
        if not self.dogs: return self.dequeueCat()

        # 比较时间戳，取较小者（即更早进入的）
        if self.cats[0][2] < self.dogs[0][2]:
            return self.dequeueCat()
        else:
            return self.dequeueDog()

    def dequeueDog(self) -> list[int]:
        if not self.dogs: return [-1, -1]
        record = self.dogs.popleft()
        return [record[0], record[1]]

    def dequeueCat(self) -> list[int]:
        if not self.cats: return [-1, -1]
        record = self.cats.popleft()
        return [record[0], record[1]]