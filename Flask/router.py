import os
from app import app
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from pathlib import Path

hi = {'hello':'world!'}
@app.route('/')
def upload_form():
    return hi


if __name__ == "__main__":
    app.run()