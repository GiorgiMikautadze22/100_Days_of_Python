import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()

API_KEY="TopSecretAPIKey"

@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafe():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    cafes_list = [cafe.to_dict() for cafe in all_cafes]
    return jsonify(all_cafes=cafes_list)


@app.route("/search")
def find_cafe():
    loc = request.args.get('loc')
    cafes = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add_cafe():
    data = request.form
    new_cafe = Cafe(
        name=data["name"],
        map_url=data["map_url"],
        img_url=data["img_url"],
        location=data["location"],
        seats=data["seats"],
        has_toilet=bool(data["has_toilet"]),
        has_wifi=bool(data["has_wifi"]),
        has_sockets=bool(data["has_sockets"]),
        can_take_calls=bool(data["can_take_calls"]),
        coffee_price=data["coffee_price"]
    )
    db.session.add(new_cafe)
    db.session.commit()
    return {"Success": True, "message": "Cafe has been added"}


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:id>", methods=['PATCH', 'PUT'])
def update_coffee_price(id):
    new_price = request.form.get('new_price')
    cafe_to_update = db.get(Cafe, id)
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Success": True, "Message": "Price has been updated"}), 404

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:id>", methods=['DELETE'])
def delete_cafe(id):
    user_api_key = request.form.get('api_key')
    if user_api_key == API_KEY:
        cafe_to_delete = db.get_or_404(Cafe, id)
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(response={"success": "Cafe has been deleted"}), 200
    else:
        return jsonify(response={"success": False, "Message": "Wrong Api key"}), 403


if __name__ == '__main__':
    app.run(debug=True, port=8080)
