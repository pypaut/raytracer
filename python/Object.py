class Object:
    def __init__(self):
        pass

    @abstractmethod
    def intersects(self, point, vec):
        pass

    @abstractmethod
    def normal(self, point):
        pass

    @abstractmethod
    def getMaterial(self, point):
        pass
