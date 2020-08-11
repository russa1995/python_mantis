class Project:
    def __init__(self, name=None, description=None):
        self.name = name
        self.description =description

    def __repr__(self):
        return "%s:%s" % (self.name, self.description)

    def __eq__(self, other):
        return self.name == self.name and self.description == self.description