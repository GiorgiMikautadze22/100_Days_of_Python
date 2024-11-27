from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, redirect, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
app.secret_key = "dawdm12ed1mkj2mi124n"
bootstrap = Bootstrap5(app)

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


class AddBook(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    author = StringField(label='Author', validators=[DataRequired()])
    rating = IntegerField(label='Rating', validators=[DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField(label='Add Book')

class EditBook(FlaskForm):
    rating = IntegerField(label='Rating', validators=[DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField(label='Update Rating')


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    form = AddBook()
    if form.validate_on_submit():
        new_book = Book(title=form.title.data, author=form.author.data, rating=form.rating.data)
        db.session.add(new_book)
        db.session.commit()
        return redirect('/')
    return render_template('add.html', form=form)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = db.get_or_404(Book, book_id)
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = EditBook()
    book_id = request.args.get('id')
    book_to_edit = db.get_or_404(Book, book_id)
    if form.validate_on_submit():
        book_to_edit.rating = form.rating.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, book=book_to_edit)

if __name__ == "__main__":
    app.run(debug=True, port=5001)

