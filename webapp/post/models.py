# -*- coding:utf-8 -*-

from webapp.extensions import mongodb as db


class WechatPost(db.DynamicDocument):
    cdn_url = db.StringField()
    title = db.StringField()
    nick_name = db.StringField()
    tag_id = db.IntField()
    url = db.StringField()
    link = db.StringField()
    ori_create_time = db.IntField()

    meta = {'collection': 'wechat_post'}
