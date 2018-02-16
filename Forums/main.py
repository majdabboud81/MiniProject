from Forums import models , store

#MEMBERS INSTANCES ------>>>>

member1 = models.Members("Majd", 36,)
member2 = models.Members("Rida", 28,)

member_store = store.Members_Store()
member_store.add(member1)
member_store.add(member2)

print (member_store.get_all())

#POSTS INSTANCES ------>>>>

post_store = store.Posts_Store()
post1 = models.Post("Post1", "Some contect whatever")
post2 = models.Post("Post2", "Som content whatever")
post3 = models.Post("Post2", "Som content whatever")
