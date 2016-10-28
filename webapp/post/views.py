#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint, render_template, request, redirect, url_for
from .models import WechatPost
from webapp.extensions import redis_store as r


blueprint = Blueprint('post', __name__, url_prefix='/post',
                      static_folder='../static')


@blueprint.route('/')
@blueprint.route('/page/<int:page>')
def post_list(page=1):
    nick_name = request.args.get('nick_name')
    # posts = WechatPost.objects.paginate(page=page, per_page=16)
    posts = WechatPost.objects[:5]
    # return ''.join([post.title for post in posts])
    return render_template('index.html')

"""
@blueprint.route('/')
def hello():
    return 'hello'


@blueprint.route('/list')
def post():
    post_list = Post.objects.all()
    title_str = '\n'.join([post.title for post in post_list])
    if not title_str:
        title_str = 'wahaha'
    return title_str
    # return render_template('semantic.html')


@blueprint.route('/add/')
def add_post():
    title = request.args.get('title', 'hehe')
    post = Post(title=title)
    post.save()
    return redirect(url_for('post.post'))


@blueprint.route('/r/')
def redis():
    r.incr('hits')
    return 'I have been seen %s times' % r.get('hits')
"""
