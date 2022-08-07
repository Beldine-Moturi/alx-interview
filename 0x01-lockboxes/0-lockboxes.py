#!/usr/bin/python3
"""
Defines a function that determines if locked boxes can be opened
"""

from operator import truediv


def canUnlockAll(boxes):
    """Determines if locked boxes can be opened"""

    if len(boxes[0]) == 0:
        return False

    class Box:
        def __init__(self, open, keys):
            self.open = open
            self.keys = keys

    list_of_boxes = []
    for box in boxes:
        b = Box(False, box)
        list_of_boxes.append(b)

    list_of_boxes[0].open = True

    for box in list_of_boxes:
        if (box.open is True) and box != []:
            for i in box.keys:
                # print(i)
                if (i < len(list_of_boxes)):
                    list_of_boxes[i].open = True
                    if (i < list_of_boxes.index(box)):
                        for x in list_of_boxes[i].keys:
                            if (x < len(list_of_boxes)):
                                list_of_boxes[x].open = True

    for box in list_of_boxes:
        if box.open is False:
            return False

    return True
