
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
        result = member
        all_members = self.get_all()
        for index, current_member in enumerate(all_members):
            if current_member.id == member.id:
                all_members[index] = member
        return result


    def delete(self, id):
        mmb = self.get_by_id(id)
        MembersStore.members.remove(mmb)

    def entity_exist(self, member):
        result = False
        if self.get_by_id(member.id) is not None:
            result = True
        return result

    #def get_by_name(self, member_name):
     #   all = self.get_all()
      #  for memb in all:
       #     if str(member_name) == str(memb.name):
        #        yield memb

    #def get_by_name(self, member_name):
        #return [member for member in self.get_all() if member.name == member_name]

    def get_by_name(self, member_name):
        return [member for member in self.get_all() if member.name == member_name]


    def get_members_with_posts(self, all_posts):
       all_members = self.get_all()
       for member in all_members:
           for post in all_posts:
               if member.id == post.member_id:
                   member.posts.append(post)
       return all_members


    def get_top_two(self, all_posts):
        all_post = self.get_members_with_posts(all_posts)
        all_members = self.get_all()
        all_post = sorted(all_members, key=lambda x: len(x.posts), reverse=True)
        return all_post[:2]



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
        PostsStore.posts.remove(pst)

