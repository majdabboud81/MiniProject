class Members:
    def __init__(self, member_name, member_age):
        self.id = 0
        self.name = member_name
        self.age = member_age

    def __str__(self):
        return """Name: {}
Age: {}""".format(self.name,
                    self.age,)

class Post:
    def __init__(self,post_title,post_content):
        self.id = 0
        self.title = post_title
        self.content = post_content

    def __str__(self):
        return """Title: {}
Content: {}""".format(self.title,
                    self.content,)
