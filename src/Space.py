# Class representing space on game board

class Space(object):

    def __init__(self, space_type):
        self.set_space_type(space_type)

    def set_space_type(self, space_type):
        self.space_type = space_type

    def get_space_type(self):
        return self.space_type