
# MEMBERS FUNCS --------------------->>>>>>

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
        result = None
        all_members = self.get_all()
        for member in all_members:
            if id == member.id: # replaced is cuz The operators is and is not test for object identity: x is y is true if and only if x and y are the same object.
                result = member
                break
        return result

    def update(self, member):
        members = self.get_by_id(member.id)
        if members != None:
            members.name = member.name
            members.age = member.age

    def delete(self, id):
        mmb = self.get_by_id(id)
        MembersStore.members.remove(mmb)

    def entity_exist(self, member):
        result = False
        if self.get_by_id(member.id) is not None:
            result = True
        return result

    def get_by_name(self, member_name):
        sam_name = []
        all = self.get_all()
        for memb in all:
            if str(member_name) == str(memb.name):
                sam_name.append(memb)
        return sam_name



# POSTS CLASS ------------------------------>>>>>>>

class PostsStore:
    posts = []
    last_id = 1

    def get_all(self):
        return PostsStore.posts

    def add(self, post):
        post.id = PostsStore.last_id
        self.posts.append(post)
        PostsStore.last_id += 1

    def get_by_id(self, id):
        all_posts = self.get_all()
        result = None
        for post in all_posts:
            if post.id == id:
                result = post
                break
        return result

    def update(self, post):
        posts = self.get_by_id(post.id)
        if posts != None:
            posts.title = post.title
            posts.content = post.content

    def entity_exist(self, post):
        result = False
        if self.get_by_id(post.id) is not None:
            return True
        return result

    def delete(self, id):
        pst = self.get_by_id(id)
        if pst != None:
            PostsStore.posts.remove(pst)
        else:
            return "id not found !!!"

