
class bubblesort:
    """
    
        Bubble sort algorithm: O(N^2)
    
    """

    def __init__(self):
        self.steps = 0

    def sort(self, A):
        """
            Sort array of values
        """
        sorted = False
        while not sorted:
            swaps = 0

            for i in range(len(A) - 1):
                self.steps += 1
                if A[i] > A[i + 1]:
                    tmp = A[i]
                    A[i] = A[i + 1]
                    A[i + 1] = tmp
                    swaps += 1
                        
            if swaps == 0:
                sorted = True
        return A

    def steps_taken(self):
        return self.steps


class selectionsort:
    def __init__(self):
        self.steps = 0

    def sort(self, A):
        """
            Sort array of values using Bubble sort
            >>> O(N^2 / 2) --> O(N^2)
        """
        for i in range(len(A)):
            selected_index = i
            for j in range(i + 1, len(A)):
                if A[selected_index] > A[j]:
                    selected_index = j
            
            if A[selected_index] < A[i]:
                tmp = A[i]
                A[i] = A[selected_index]
                A[selected_index] = tmp
        
        return A

    def steps_taken(self):
        return self.steps