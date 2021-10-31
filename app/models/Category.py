from app import db
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(70))
    #relationship one to many
    #project = db.relationship("Project", back_populates="categories")