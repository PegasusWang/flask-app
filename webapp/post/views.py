#!/usr/bin/env python
# -*- coding:utf-8 -*-


from flask import Blueprint, render_template


blueprint = Blueprint('post', __name__, url_prefix='/post',
                      static_folder='../static')


@blueprint.route('/')
def post():
    return render_template('semantic.html')


@blueprint.route('/t/')
def t():
    return render_template('semantic.html')
