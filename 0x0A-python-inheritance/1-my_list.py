#!/usr/bin/python3
class MyList(list):
    """
    class MyList that inherits from lis
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        list_sort = self.copy()
        list_sort.sort()
        print(list_sort)
