class Members_Store:
    members = []

    def get_all(self):
            return Members_Store.members

    def add(self, member):
            Members_Store.members.append(member)

class Posts_Store:
    posts = []

    def get_all(self):
        return Members_Store.posts

    def add(self, post):
        self.posts.append(post)
