class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.undo_index = 0 # Index of current action in stack
        self.undo_list = []

    def add(self, num: int):
        self.value += num
        if self.undo_index < len(self.undo_list): # Not the last element
            self.undo_list[self.undo_index] = num
        else: # Currently on last element; append new element
            self.undo_list.append(num)

        self.undo_index += 1

    def subtract(self, num: int):
        self.add(-1 * num)

    def undo(self):
        if self.undo_index > 0: #There are actions to undo
            self.value -= self.undo_list[self.undo_index-1]
            self.undo_index -= 1

    def redo(self):
        if self.undo_index< len(self.undo_list): # There are actions to redo
            self.value += self.undo_list[self.undo_index]
            self.undo_index += 1

    def bulk_undo(self, steps: int):
        for _ in range(steps):
            self.undo()


    def bulk_redo(self, steps: int):
        for _ in range(steps):
            self.redo()