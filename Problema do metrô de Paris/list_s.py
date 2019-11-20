class list_s:
    def __init__(self, max_size=-1):
        self.max_size = max_size
        self.queue = []

    def put(self, element):
        if self.max_size != -1 and len(self.queue) == self.max_size:
            del self.queue[0]

        self.queue.append(element)

    def __contains__(self, item):
        for i in self.queue:
            if item == i:
                return True

        return False
