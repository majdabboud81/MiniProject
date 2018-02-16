class MembersStore:
    members = []
    last_id = 1

    def get_all(self):
            return MembersStore.members

    def add(self, member):
        member.id = MembersStore.last_id
        self.members.append(member)
        MembersStore.last_id += 1

    def get_by_id(self, id):
        all_members = self.get_all()
        for member in MembersStore.members:
            if member.id is id:
                return member

    def entity_exist(self, member):
        all_members = self.get_all()
        result = False
        for mem in MembersStore.members:
            if mem is member:
                result = True
        return result

    def delete(self, id):
        mmb = self.get_by_id(id)
        if mmb != None:
            MembersStore.members.remove(mmb)
        else:
            return "id not found"

class PostsStore:
    posts = []

    def get_all(self):
        return PostsStore.posts

    def add(self, post):
        self.posts.append(post)
