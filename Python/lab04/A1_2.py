# 1 - We need to implement a python class that represents the queue data structure.


class QueueBasic:

    def __init__(self):

        self.queue = []

    def insertVal(self, value):

        self.queue.insert(0, value)

    def pop(self):

        try:
            return self.queue.pop()

        except:
            print("**pop value from an empty queue**")

            return None

    def is_empty(self):

        return len(self.queue) == 0


# q = QueueBasic()

# q.insertVal("1")
# q.insertVal("2")
# q.insertVal("3")
# print(q.pop())
# print(q.queue)
# print(q.is_empty())


# 2 - We need to implement another queue class that has the same properties as previous but with the following changes:

class QueueOutOfRangeException(Exception):

    pass


class Queue(QueueBasic):

    _queues = {}

    def __init__(self, name, size):

        super().__init__()
        self.name = name
        self.size = size
        self._queues[name] = self

    def insertVal(self, value):

        try:
            if len(self.queue) == self.size:

                raise QueueOutOfRangeException("Queue is full. Cannot enqueue more items.")

            self.queue.insert(0, value)

        except QueueOutOfRangeException as e:
            print(e)

    @classmethod
    def get_queue(cls, name):

        return cls._queues.get(name)


# print()
# q2 = Queue("q2", 4).insertVal("6")
# print(Queue.get_queue("q2").queue)
# print()

# q = Queue("q1", 5)

# q.insertVal("1")
# q.insertVal("2")
# q.insertVal("3")
# q.insertVal("4")
# q.insertVal("5")
# q.insertVal("6")
# # print(q.pop())
# # print(q.is_empty())
# print(q.queue)
# print()
