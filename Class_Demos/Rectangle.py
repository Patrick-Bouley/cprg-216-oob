class Rectangle:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calc_per(self):
        return 2*(self.width + self.height)
    
    def calc_area(self):
        return self.height * self.width
    
    '''

    def set_height(self, value):
        self.height = value
    
    def set_width(self, value):
         self.width = value

    def get_area(self):
        self.area = self.height * self.width

    '''