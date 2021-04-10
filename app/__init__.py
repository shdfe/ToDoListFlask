from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'Sheel-loves-chocolate'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'Flatly'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
migrate = Migrate(app, db)
db.create_all()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Task=Task)


from app import routes
from app.models import Task