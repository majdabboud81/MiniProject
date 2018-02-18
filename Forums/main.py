import models, store

# MEMBERS STORE ------>>>>

def create_members():

    member1 = models.Members("Majd", 36)
    member2 = models.Members("Rida", 28)
    member3 = models.Members("Manhal", 29)
    member4 = models.Members("Majd", 50)
    print(member1)
    print(member2)
    print(member3)
    print(member4)
    print("=" * 30)


    return member1, member2, member3, member4


def store_should_add_models(members_instances, member_store):

    for member in members_instances:
        member_store.add(member)


def stores_should_be_similar():

    member_store1 = store.MembersStore()
    member_store2 = store.MembersStore()
    if member_store1.get_all() is member_store2.get_all():
        print("Same stores elements !")


def print_all_members(member_store):
    print("=" * 30)

    for member in member_store.get_all():
        print(member)

    print("=" * 30)

def get_by_id_should_retrieve_same_object(member_store, member2):
    member2_retrieved = member_store.get_by_id(member2.id)

    if member2 is member2_retrieved:
        print("member2 and member2_retrieved are matching !")


def update_should_modify_object(member_store, member3):
    member3_copy = models.Members(member3.name, member3.age)
    member3_copy.id = 3

    if member3_copy is not member3:
        print("post3 and member3_copy are not the same !")

    print(member3_copy)
    member3_copy.name = "john"
    member_store.update(member3_copy)
    print(member_store.get_by_id(member3.id))


def catch_exception_when_deleting():
    try:
        member_store.delete(5)
    except ValueError:
        print("It should be an existence entity before deleting !")



def print_same_names(member_store):

    for member in member_store.get_by_name("Majd"):
        print (member)



members_instances = create_members()
member1, member2, member3, member4 = members_instances

member_store = store.MembersStore()

store_should_add_models(members_instances, member_store)

stores_should_be_similar()

print_all_members(member_store)

get_by_id_should_retrieve_same_object(member_store, member2)

update_should_modify_object(member_store, member3)

catch_exception_when_deleting()

print_all_members(member_store)

print_same_names(member_store)


# POST STORE ------------------>>>>>>>



def create_posts():

    post1 = models.Post("Post1", "Some contect whatever")
    post2 = models.Post("Post2", "Some content whatever")
    post3 = models.Post("Post3", "Some content whatever")
    print("=" * 35)
    print(post1)
    print(post2)
    print(post3)
    print("=" * 30)

    return post1, post2, post3,


def store_should_add_models(posts_instances, post_store):

    for post in posts_instances:
        post_store.add(post)


def stores_should_be_similar():

    post_stor1 = store.PostsStore()
    post_store2 = store.PostsStore()
    if post_stor1.get_all() is post_store2.get_all():
        print("Same stores elements !")


def print_all_posts(post_store):
    print("=" * 30)

    for post in post_store.get_all():
        print(post)

    print("=" * 30)

def get_by_id_should_retrieve_same_object(post_store, post2):
    post2_retrieved = post_store.get_by_id(post2.id)

    if post2 is post2_retrieved:
        print("post2 and post2_retrieved are matching !")


def update_should_modify_object(post_store, post3):
    post3_copy = models.Post(post3.title, post3.content)
    post3_copy.id = 3

    if post3_copy is not post3:
        print("post3 and post3_copy are not the same !")

    print(post3_copy)
    post3_copy.title = "Post3_C"
    post_store.update(post3_copy)
    print(post_store.get_by_id(post3.id))


def catch_exception_when_deleting():
    try:
        post_store.delete(5)
    except ValueError:
        print("It should be an existence entity before deleting !")

posts_instances = create_posts()
post1, post2, post3 = posts_instances

post_store = store.PostsStore()

store_should_add_models(posts_instances, post_store)

stores_should_be_similar()

print_all_posts(post_store)

get_by_id_should_retrieve_same_object(post_store, post2)

update_should_modify_object(post_store, post3)

catch_exception_when_deleting()

print_all_posts(post_store)

