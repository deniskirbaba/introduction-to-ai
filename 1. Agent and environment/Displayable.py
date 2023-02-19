class Displayable(object):
    """
        code trace class
        trace depth controls max_display_level
    """
    max_display_level = 1

    def display(self, level, *args, **nargs):
        """
        print argument, if its level <= max_display_level
        level = integer
        the rest of the arguments are any that can take print
        """
        if level <= self.max_display_level:
            print(*args, **nargs)