#!/usr/bin/env python3


"""module that contains class"""


class VerboseList(list):
    """class of verbolist"""
    def append(self, item):
        """method that adds el"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """method that extend el"""
        super().extend(items)
        number_of_items = len(items)
        print(f"Extended the list with [{number_of_items}] items.")

    def remove(self, item):
        """method that removes el"""
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """method that pop el by idx"""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
