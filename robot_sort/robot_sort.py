class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    ''' first implementation - selection sort '''

    def right_bubble(self):
        self.swap_item()
        self.move_right()
        if self.compare_item() == 1:
            self.swap_item()
            self.set_light_off()
        self.move_left()
        self.swap_item()
        self.move_right()

    def right_bubble_cocktail(self):
        self.swap_item()
        self.move_right()
        if self.compare_item() == 1:
            self.swap_item()
            self.set_light_off()
        self.move_left()
        self.swap_item()
        # ignore final move right

    def left_bubble(self):
        self.swap_item()
        self.move_left()
        if self.compare_item() == -1:
            self.swap_item()
            self.set_light_off()
        self.move_right()
        self.swap_item()
        self.move_left()

    def left_bubble_alt(self):
        # idea here - move left 2 at a time, rather than 1, to help some bubble up faster
        self.swap_item()
        self.move_left()
        if self.can_move_left():
            self.move_left()
        if self.compare_item() == -1:
            self.swap_item()
            self.set_light_off()
        
        while self.compare_item() is not None:
            self.move_right()
        # self.move_right()
        # self.move_right()
        self.swap_item()
        self.move_left()

    def left_bubble_cocktail(self):
        self.swap_item()
        self.move_left()
        if self.compare_item() == -1:
            self.swap_item()
            self.set_light_off()
        self.move_right()
        self.swap_item()
        # ignore final move left
            

    def sort(self):
        """
        Sort the robot's list.
        """
        # test_list = self._list[:]
   
        # print(self._list)
   
        # working implementation DO NOT CHANGE
        # while self.light_is_on() == False:
        #     self.set_light_on()
        #     while self.can_move_right() == True:
        #         self.swap_item()
        #         self.move_right()
        #         if self.compare_item() == 1:
        #             self.swap_item()
        #             self.set_light_off()
        #         self.move_left()
        #         self.swap_item()
        #         self.move_right()
        #     while self.can_move_left() == True:
        #         self.move_left()

        # next implementation - do bubble sort on the way back
        # WORKING, DO NOT CHANGE
        # self.right_bubble()
        # while self.light_is_on() == False:
        #     self.set_light_on()
        #     # first pass - moving right
        #     while self.can_move_right() == True:
        #         self.right_bubble()
            
        #     if self.light_is_on() == True:
        #         break

        #     # once you get to the end, don't need to re-compare last two.
        #     # can move left one before doing left_bubble()
        #     self.move_left()
        #     while self.can_move_left() == True:
        #     # second pass - moving left
        #         self.left_bubble()
                
        #     # don't need to compare last two again
        #     if self.light_is_on() == False:
        #         self.move_right()

        # attempt with left_bubble_alt

        self.right_bubble()
        while self.light_is_on() == False:
            self.set_light_on()
            # first pass - moving right
            while self.can_move_right() == True:
                self.right_bubble()
            
            if self.light_is_on() == True:
                break

            # once you get to the end, don't need to re-compare last two.
            # can move left one before doing left_bubble()
            self.move_left()
            while self.can_move_left() == True:
            # second pass - moving left
                self.left_bubble_alt()
                
            # don't need to compare last two again
            if self.light_is_on() == False:
                self.move_right()

        # cocktail sort attempt, it did not help
        # self.right_bubble()
        # while self.light_is_on() == False:
        #     self.set_light_on()
        #     # first pass - moving right
        #     while self.can_move_right() == True:
        #         # self.right_bubble_cocktail()
        #         # self.left_bubble_cocktail()
        #         # self.move_right()
        #         self.right_bubble()
        #     if self.light_is_on() == True:
        #         break
        #     # once you get to the end, don't need to re-compare last two.
        #     # can move left one before doing left_bubble()
        #     self.move_left()
        #     self.left_bubble()
        #     while self.can_move_left() == True:
        #     # second pass - moving left
        #         # self.left_bubble_cocktail()
        #         # self.right_bubble_cocktail()
        #         # self.move_left()
        #     # variant - regular bubble on the way back
        #         self.left_bubble()
            
        #     # don't need to compare last two again
        #     if self.light_is_on() == False:
        #         self.move_right()
        

        # print(self._list)
        return None




if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    # l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    # l = [5, 4, 3, 2, 1]
    l = [11, 13, 7, 17, 9, 20, 1, 21, 2, 4, 22, 16, 15, 10, 23, 19, 8, 3, 5, 14, 6, 0, 24, 12, 18]
    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
    print(robot._time)

'''

first attempt with insertion sort

 print(self._list)
        while self.light_is_on() == 0:
            # print(self._list)
            self.set_light_on()

            # do this for the first item, index 0
            self.swap_item()
            self.move_right()
            
            # moving right - goal is to move greater numbers to back
            while self.can_move_right() == 1:
                if self.compare_item() == 1:
                    self.set_light_off()
                    # self.swap_item()
                self.move_right()

            # do this for the last item, index -1
            if self.compare_item() == 1:
                # self.set_light_off()
                self.swap_item()

            # going back - move left one first
            self.move_left()

            # drop off number if it's bigger
            while self.can_move_left() == 1:
                if self.compare_item() == 1:
                    # self.set_light_off()
                    self.swap_item()
                self.move_left()
            self.swap_item()
            # print(self._list)

'''