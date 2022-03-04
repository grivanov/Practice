class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    # Write your code here

    def add(self, name):
        self.members.append(name)

    def delete(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception("Member not in group")

    def get_members(self):
        return sorted(self.members)
