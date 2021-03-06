class Queue:
    """
    This is the Queue class. This is where you will be implementing
    your functions for queue
    """

    def __init__(self):
        self.queue = []

    def is_empty(self) -> bool:
        """
        This function should return True is the queue is
        empty and False if the queue is not empty.
        :return: A boolean
        """
        if len(self.queue) > 0:
            return False
        else:
            return True

    def enqueue(self, e) -> None:
        """
        This function add an element to the queue
        :param e: the element we want you to add
        :return: None
        """
        self.queue.append(e)
        return None

    def dequeue(self):
        """
        This function remove and return the first element
        of the list.
        :return: The first element of the list
        """
        if self.is_empty() is not True:
            return self.queue.pop(0)

