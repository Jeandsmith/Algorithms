
from typing import List


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


class insertionsort:

    def __init__(self, list):
        self.__list = list
        self.steps = 0

    def sort(self):
        self.steps = 0
        for i in range(1, len(self.__list)):
            tmp = self.__list[i]
            left_pos = i
            while left_pos > 0:
                if self.__list[left_pos - 1] > tmp:
                    self.__list[i] = self.__list[left_pos - 1]
                    i = left_pos - 1
                left_pos -= 1
                self.steps += 1
            self.__list[i] = tmp
        return self.__list


class QuickSort:

    def __init__(self) -> None:
        self.steps = 0

    def sort(self, A: List[int], left: int, right: int):

        if right - left <= 0:
            return self.st
        n_pivot = self.__partition(A, left, right)
        self.sort(A, left, n_pivot - 1)
        self.sort(A, n_pivot + 1, right)

    def __partition(self, A, left, right) -> int:
        l = left
        r = right - 1
        p = A[right]

        while True:

            # print ([l, r])
            while A[l] < p:
                l += 1
                self.steps += 1

            while A[r] > p:
                r -= 1
                self.steps += 1

            if l >= r:
                tmp = A[right]
                A[right] = A[l]
                A[l] = tmp
                return l
            else:
                tmp = A[l]
                A[l] = A[r]
                A[r] = tmp
            l += 1

class DFS:
    """
        Dept first search for Graph or 2D array searching where pieces of data, 
        Vertex or Nodes, are related to one another
    """