class MyArray:
    def __init__(self, total_size: int, used_size: int):
        self.total_size = total_size
        self.used_size = used_size
        self.array = []

    def append(self, value):
        """
        Add a value to the end of the array
        """
        if len(array) < used_size:
            self.array.append(value)
        else:
            raise Exception("Array full please increase the size of the array")

    def increase_size(self, size):
        """
        Increase the used size of the array
        """
        if self.total_size > size:
            raise Exception("Cannot assign size more than the total size of the array")
        else:
            self.used_size = size

    def show(self):
        """
        Show the array
        """
        for i in range(self.used_size):
            print(self.array[i])
        print()

    def setVal(self):
        """
        Set the values of the array
        """
        for i in range(self.used_size):
            self.array.append(int(input(f"Enter the value at {i}: ")))

    def bubbleSort(self):
        """
        A function to sort the array using the bubbleSort method
        """
        for i in range(self.used_size - 1, 0, -1):
            for j in range(i):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]

    def __len__(self):
        """
        Display the length of an array
        """
        return len(self.array)

    def delete(self, index: int):
        """
        Deletes the element at index
        """
        for i in range(index, self.used_size - 1):
            self.array[i] = self.array[i + 1]

        self.used_size -= 1
