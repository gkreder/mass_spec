class Compound:
    def __init__(self, name, method, mz, rt):
        self.name = name
        self.method = method
        self.mz = mz
        self.rt = rt


class CompoundGraph:
    def __init__(self):
        self.compounds = []
        self.distances = {}
