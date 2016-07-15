# -*- coding:utf-8 -*-

from webapp.extensions import mongodb as db


class Post(db.Document):
    title = db.StringField(max_length=255, required=True)
