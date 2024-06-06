from db_config.gino_connect import db


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, default = lambda: db.Sequence('user_user_id_seq').next_value())
    username = db.Column(db.String(45), unique=True)
    hashed_password =db.Column(db.String(100))
    email = db.Column(db.Text, unique=True)
    first_name = db.Column(db.Text, unique=True)
    last_name = db.Column(db.Text, unique=True)
