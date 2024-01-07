from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()
def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class Cupcake (db.Model):
    """Cupcake"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(400), nullable=False,default="https://tinyurl.com/demo-cupcake")
    
    def serialize(self):
      """Serialize a cupcake SQLAlchemy obj to dictionary."""

      return {
        "id": self.id,
        "flavor": self.flavor,
        "size": self.size,
        "rating": self.rating,
        "image": self.image
      }
   
   
    
  