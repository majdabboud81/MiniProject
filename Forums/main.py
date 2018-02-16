from Forums import models , store

#MEMBERS INSTANCES ------>>>>

member1 = models.Members("Majd", 36,)
member2 = models.Members("Rida", 28,)

member_store = store.Members_Store()
member_store.add(member1)
member_store.add(member2)


#POSTS INSTANCES ------>>>>


post1 = models.Post("Post1", "Some contect whatever")
post2 = models.Post("Post2", "Som content whatever")
post3 = models.Post("Post2", "Som content whatever")

post_store = store.Posts_Store()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)
