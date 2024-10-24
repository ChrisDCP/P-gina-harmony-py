from flask import Flask

app = Flask(__name__)

app.secret_key = 'b91a683286dfa3df36442a3219406f3100726b236023f639'

from app import routes  
