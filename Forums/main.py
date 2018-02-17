import models , store

#MEMBERS INSTANCES ------>>>>

member1 = models.Members("Majd", 36,)
member2 = models.Members("Rida", 28,)

member_store = store.MembersStore()
member_store.add(member1)
member_store.add(member2)

#for member in member_store.get_all():
#    print (member)


print (member_store.get_by_id(1))

#print(member_store.delete(4))


#print(member_store.entity_exist(member2))


#POSTS INSTANCES ------>>>>

post_store = store.PostsStore()
post1 = models.Post("Post1", "Some contect whatever")
post2 = models.Post("Post2", "Som content whatever")
post3 = models.Post("Post3", "Som content whatever")

post_store.add(post1)
post_store.add(post2)
post_store.add(post3)

#print (post_store.get_by_id(3))

#for post in post_store.get_all():
 #   print (post)
