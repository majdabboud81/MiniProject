import models
from operator import attrgetter
import itertools, copy


# MEMBERS FUNCS --------------------->>>>>>

class MembersStore(models.BaseStore):
    members = []
    last_id = 1

    def __init__(self):
        super().__init__(MembersStore.members, MembersStore.last_id)


    #get_by_name STARTS... many generators or comprehension

    def get_by_name(self, member_name):
        return (member for member in self.get_all() if member.name == member_name)

    # (((def get_by_name(self, member_name):
    #   all = self.get_all()
    #  for memb in all:
    #     if str(member_name) == str(memb.name):
    #        yield memb

    # def get_by_name(self, member_name):
    #   return [member for member in self.get_all() if member.name == member_name]

    # def get_members_with_posts(self, all_posts):
    #  all_members = self.get_all()
    # for member in all_members:
    #    for post in all_posts:
    #       if member.id == post.member_id:
    #           member.posts.append(post)
    # return all_members)))
    # get_by_name ENDZ ...........


    def get_members_with_posts(self, all_posts):
        all_members = copy.deepcopy(self.get_all())

        for member, post in itertools.product(all_members, all_posts):
            if member.id == post.member_id:
                member.posts.append(post)

        for member in all_members:
            yield member

    def get_top_two(self, all_posts):
        all_members_posts = list(self.get_members_with_posts(all_posts))
        all_members_posts.sort(key=lambda x: len(x.posts), reverse=True)

        yield all_members_posts[0]
        yield all_members_posts[1]



# POSTS CLASS ------------------------------>>>>>>>


class PostsStore(models.BaseStore):
    posts = []
    last_id = 1

    def __init__(self):
        super().__init__(PostsStore.posts, PostsStore.last_id)

    def get_posts_by_date(self, all_posts):
        all_posts.sort(key=attrgetter('date'), reverse=True)

        for post in all_posts:
            yield post
