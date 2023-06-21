from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import datetime
import re
import bcrypt
import sqlite3
import mask
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, DateTime, PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker, declarative_base


app = Flask(__name__)

engine = create_engine('sqlite:///project.db', echo=False)
db = sessionmaker(autoflush=False, bind=engine)()
Base = declarative_base()

conn = sqlite3.connect('project.db', check_same_thread=False)
cursor = conn.cursor()


# class Notes(Base):
#     __tablename__="Notes2"
#     id=Column(Integer,primary_key=True)
#     title = Column(String(2000),nullable=False)
#     text = Column(String(),nullable=False)
#     timestamp = Column(String(30), nullable=False)
#     __table_args__ = (
#     PrimaryKeyConstraint('title', 'text', 'timestamp'),
#     )

# class Backup(Base):
#     __tablename__="BackupTable"
#     id=Column(Integer,primary_key=True)
#     title = Column(String(2000),nullable=False)
#     text = Column(String(),nullable=False)
#     timestamp = Column(String(30), nullable=False)
#     __table_args__ = (
#      PrimaryKeyConstraint('title', 'text', 'timestamp'),
#     )


class Notes(Base):
    __tablename__="Notes21"
    id=Column(Integer)
    title = Column(String(2000))
    text = Column(String())
    timestamp = Column(String(30))
    __table_args__ = (
        PrimaryKeyConstraint('title', 'text', 'timestamp'),
    )

class Backup(Base):
    __tablename__="BackupTable1"
    id=Column(Integer)
    title = Column(String(2000))
    text = Column(String())
    timestamp = Column(String(30))
    __table_args__ = (
        PrimaryKeyConstraint('title', 'text', 'timestamp'),
    )

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/notes", methods=['GET', 'POST'])
def notest():
    if request.method == 'POST':
        title = request.form.get('title')
        text = request.form.get('text')
        timestamp = str(datetime.datetime.now())
        # enter = {}

        # db.query(Backup).filter_by(title=title, text=text, timestamp=timestamp).delete()


        # entry = Notes(title=title,text=text,timestamp=timestamp)
        note=Backup(title=title,text=text,timestamp=timestamp)


  
        db.add(note)
        # db.delete(note)


        db.commit()
    
    
    # if request.method == 'GET':
    #     delete_title = request.args.get('delete_title')
    #     delete_text = request.args.get('delete_text')
    #     delete_timestamp = request.args.get('delete_timestamp')

    #     if delete_title and delete_text and delete_timestamp:
    #         note = db.query(Backup).filter_by(title=delete_title, text=delete_text, timestamp=delete_timestamp).first()
    #         if note:
    #             db.delete(note)
    #             db.commit()
        
    notes = db.query(Backup).all()

    return render_template("notestest.html",notes=notes)


if __name__ == '__main__':
    with app.app_context():

     Base.metadata.create_all(engine)
     app.run(debug = True)

