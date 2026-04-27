class StackOOP:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Contoh penggunaan
if __name__ == "__main__":
    stack = StackOOP()

    stack.push("Donut")
    stack.push("Kue Cubit")
    stack.push("Kue Lapis")

    print("Top item:", stack.peek())  # Output: Kue Lapis
    print("Stack size:", stack.size())  # Output: 3

    popped_item = stack.pop()
    print("Popped item:", popped_item)  # Output: Kue Lapis
    print("Stack size after pop:", stack.size())  # Output: 2
