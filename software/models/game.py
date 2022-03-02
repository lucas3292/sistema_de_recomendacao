from software import db


class User(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key = True)
    gamename =  db.Column(db.String(200), unique= True)
    studioname = db.Column(db.String(50), unique = True)
    likes_id = db.Column(db.Integer, db.ForeighKey('users.id'))

    likes = db.relationship('User', foreign_keys = likes_id)

    def __init__(self, gamename,studioname):
        self.gamename = gamename
        self.studioname = studioname

    def __repr__(self):
        return '<User %r>' % self.gamename