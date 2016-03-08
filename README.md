# data-structures
Code Fellows Python 401 Data Structures assignment
Created by Kyle Richardson and Iris Carrera
This repo will hold sample code for a number of classic data structures implemented in Python.

## linked_list.py
The linked list data structure. Our design uses Node objects where each node containing a value and a pointer to some other node, or a None value if it's the last in the list. This None value pointer makes reading through the list for various functions very easy as we can just do >while head_step: and have the head_step assigned to the current node's point_to. That will go through each item until head_step will be assigned to None value stopping the loop. In general our outside resources included Python documentation and assistance from our instructors.

##stack.py
The Stack data structure. We realized that a stack is essentially just a linked_list. Since the linked_list we made has all the qualities of a Stack data structure including the LIFO access. We decided to inherit the LinkedList class for the Stack class and override the pop() method from LinkedList. And add a method push(val). In both cases we just used methods from the LinkedList class to create these methods as the LinkedList methods did everything we already needed to do.
