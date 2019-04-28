import requests
import flask_login
from flask import request, redirect, url_for, Blueprint, render_template, flash, current_app, session
from sqlalchemy.exc import IntegrityError

website = Blueprint("website", __name__)

@website.route("/")
def home():
    return render_template("index.html")