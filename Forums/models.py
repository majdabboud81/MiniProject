class Members:
    def __init__(self, member_name, member_age):
        self.name = member_name
        self.age = member_age

    def __str__(self):
        return """Name: {}
Age: {}""".format(self.name,
                    self.age,)

class Post:
    def __init__(self,post_title,post_content):
        self.title = post_title
        self.content = post_content

