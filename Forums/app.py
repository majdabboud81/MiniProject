from flask import Flask, render_template
from Forums import store, dummy_data


app = Flask(__name__)

member_store = store.MembersStore()
post_store = store.PostsStore()

from Forums.views import *


if __name__ == "__main__":
    dummy_data.seed_stores(member_store, post_store)
    app.run()
