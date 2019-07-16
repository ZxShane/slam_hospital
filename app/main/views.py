# -*- coding: utf-8 -*-

from app.speech import Speech
from . import main
from .. import db
from ..models import User
from flask import render_template, request
import time
from ..models import PoseToLocation


@main.route('/')
def index():
    return render_template('index.html', name='index')


@main.route('/query')
def query():

    return render_template('web_wideo.html')

@main.route('/introduction')
def introduction():

    return render_template('introduction.html')

@main.route('/map')
def map():

    return render_template('map.html')

@main.route('/asr')
def asr():
    audio = request.args.get('audio')
    print audio
    if audio is None:
        return render_template('asr.html')
    else:
        speech = Speech()
        result = speech.asr(audio)
        print result  # we will know the message in the pcm file
        pose_to_location = PoseToLocation.query.filter_by(location=result).first()
        print pose_to_location.position_x + 'LOCATION '

        # INFO // liliangbin 将位置信息发送给项目  但是我们没有做一个验证，就是怎么来确定这个用户确实是拿到了数据
        # ros_goal = RosGoal()
        # ros_goal.publish_goal(pose_to_location)

        return result

@main.route('/asr_test')
def asr_test():
    audio = request.args.get('audio')
    print audio

    speech = Speech()
    result = speech.asr(audio)
    return result