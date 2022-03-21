class Stack:
    """
    This is the Stack class. This is where you will be
    implementing your function.
    """

    def __init__(self):
        self.stack = []

    def is_empty(self) -> bool:
        """
        This function should return True is the queue is
        empty and False if the queue is not empty.
        :return: A boolean
        """
        if len(self.stack) > 0:
            return False
        else:
            return True

    def push(self, e) -> None:
        """
        This function should push an element to the stack.
        :param: e
        :return: None
        """
        self.stack.append(e)
        return None

    def pop(self):
        """
        This function should remove an element from the stack
        :return: The first element of the stack
        """
        if self.is_empty() is not True:
            return self.stack.pop()

        
