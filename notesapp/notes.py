from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)

engine = create_engine('sqlite:///project.db', echo=False)
db = sessionmaker(autoflush=False, bind=engine)()
Base = declarative_base()
conn = sqlite3.connect('project.db', check_same_thread=False)
cursor = conn.cursor()


class Note(Base):
    __tablename__ = "Notes4"
    id = Column(Integer, primary_key=True)
    title = Column(String(2000), nullable=False)
    text = Column(String(), nullable=False)
    timestamp = Column(String(30), nullable=False)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/notes", methods=['GET', 'POST'])
def notes():
    if request.method == 'POST':
        note_id = request.form.get('noteId')
        title = request.form.get('title')
        text = request.form.get('text')
        timestamp = str(datetime.now())
        if note_id:
            note = db.query(Note).get(note_id)
            if note:
                if 'delete' in request.form:
                    # Delete the selected note
                    db.delete(note)
                else:
                    # Update the selected note
                    note.title = title
                    note.text = text
                    note.timestamp = timestamp
            else:
                return redirect('/notes')
        else:
            # Create a new note
            note = Note(title=title, text=text, timestamp=timestamp)
            db.add(note)

        db.commit()

    notes = db.query(Note).all()

    return render_template("notes.html", notes=notes)


if __name__ == '__main__':
    with app.app_context():
        Base.metadata.create_all(engine)
        app.run(debug=True)
