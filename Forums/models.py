import datetime

#BaseStore Class =================>>>>>>

class BaseStore():

    def __init__(self, data_provider, last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def get_all(self):
        return self._data_provider

    def add(self, item_instance):
        item_instance.id = self._last_id
        self._data_provider.append(item_instance)
        self._last_id += 1

    def get_by_id(self, id):
        result = None
        all_items_instance = self.get_all()
        for item_instance in all_items_instance:
            if id == item_instance.id:  # replaced is cuz The operators is and is not test for object identity: x is y is true if and only if x and y are the same object.
                result = item_instance
                break
        return result


    def update(self, item_instance):
        result = item_instance
        all_items_instance = self.get_all()
        for index, current_item_instance in enumerate(all_items_instance):
            if current_item_instance.id == item_instance.id:
                all_items_instance[index] = item_instance
        return result


    def delete(self, id):
        item_instance = self.get_by_id(id)
        self._data_provider.remove(item_instance)


    def entity_exist(self, item_instance):
        result = False
        if self.get_by_id(item_instance.id) is not None:
            result = True
        return result



# Members Class --------------->>>>>>

class Members:
    def __init__(self, member_name, member_age):
        self.id = 0
        self.name = member_name
        self.age = member_age
        self.posts = []

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


# Posts Class --------------->>>>>>

class Post:
    def __init__(self,post_title,post_content, member_id=0):
        self.id = 0
        self.title = post_title
        self.content = post_content
        self.member_id = member_id
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"Title: {self.title}, Content: {self.content}"
