from flask import Flask, request, render_template, redirect,flash, session ,json,jsonify

from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SECRET_KEY'] ="oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
connect_db(app)
"""db.drop_all()
db.create_all()"""

@app.route("/")
def index_page():
    cupcakes = Cupcake.query.all();
    return render_template ('index.html' ,cupcakes = cupcakes)

 
@app.route("/api/cupcakes")
def get_all_cupcakes():
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    cupcake =Cupcake.query.get_or_404(cupcake_id) 
    return jsonify(cupcake=cupcake.serialize())


@app.route("/api/cupcakes/",methods=["POST"])
def create_new_cupcake():
    """Create dessert from form data & return it. Returns JSON {'cupcake': {id, name, calories}}""" 
    print(request.json)
    flavor = request.json["flavor"]
    image = request.json["image"]
    rating = request.json["rating"]
    size = request.json ["size"]
    new_cupCake = Cupcake(flavor=flavor, image=image,rating=rating,size=size)
    db.session.add(new_cupCake)
    db.session.commit()
      # Return w/status code 201 --- return tuple (json, status)
    return ( jsonify(cupcake=new_cupCake.serialize()), 201 )

@app.route("/api/cupcakes/<int:cupcake_id>",methods=["PATCH"])
def update_cupcake(cupcake_id):
   
    cupcake =Cupcake.query.get_or_404(cupcake_id) 
    cupcake.flavor = request.json.get("flavor",cupcake.flavor)
    cupcake.image = request.json.get("image",cupcake.image)
    cupcake.rating = request.json.get("rating",cupcake.rating)
    cupcake.size = request.json.get("size",cupcake.size)
    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes/<int:cupcake_id>",methods=["DELETE"])
def delete_cupcake(cupcake_id):
   
    cupcake =Cupcake.query.get_or_404(cupcake_id) 
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message ="deleted")




   
  