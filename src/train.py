class _Car:
    __slots__ = ("id", "prev", "next")
    def __init__(self, id):
        self.id = id
        self.prev = None
        self.next = None


class Train:
    def __init__(self):
        self.head = None
        self.tail = None

    def attach_front(self, car_id):
        """Add a car at the front of the train."""
        node = _Car(car_id)
        node.next = self.head
        if self.head:
            self.head.prev = node
        else:
            # Train was empty
            self.tail = node
        self.head = node

    def attach_back(self, car_id):
        """Add a car at the back of the train."""
        node = _Car(car_id)
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        else:
            # Train was empty
            self.head = node
        self.tail = node

    def detach_front(self):
        """Remove car from front; return car id or None."""
        if self.head is None:
            return None
        car_id = self.head.id
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            # Train became empty
            self.tail = None
        return car_id

    def detach_back(self):
        """Remove car from back; return car id or None."""
        if self.tail is None:
            return None
        car_id = self.tail.id
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            # Train became empty
            self.head = None
        return car_id

    def detach(self, car_id):
        """Remove first car with matching id; return True if removed."""
        node = self.head
        while node:
            if node.id == car_id:
                # Patch neighbors
                if node.prev:
                    node.prev.next = node.next
                else:
                    # Removing head
                    self.head = node.next
                if node.next:
                    node.next.prev = node.prev
                else:
                    # Removing tail
                    self.tail = node.prev
                return True
            node = node.next
        return False

    def to_list(self):
        """Return list of car ids from head to tail."""
        result = []
        node = self.head
        while node:
            result.append(node.id)
            node = node.next
        return result
