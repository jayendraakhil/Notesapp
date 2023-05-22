import timeit
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import datetime
import re
import bcrypt
import mask
from sqlalchemy import create_engine, Column, Date, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)
engine = create_engine('sqlite:///project.db', echo=False)
db = sessionmaker(autoflush=False, bind=engine)()
Base = declarative_base()


class Reminder(Base):
    __tablename__ = "Reminder"
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    date_and_time = Column(DateTime, nullable=False)


@app.route('/reminder', methods=['GET', 'POST'])
def reminder():
    if request.method == 'POST':
  
        title = request.form.get('title')
        date_and_time= request.form.get('date_and_time')

        input_datetime = datetime.datetime.strptime(date_and_time, '%Y-%m-%dT%H:%M')

        entry = Reminder(title=title, date_and_time=input_datetime)



        db.session.add(entry)
        db.session.commit()


        return render_template('reminder.html')
    else:
      reminders = db.query(Reminder).all
      return render_template('reminder.html',reminders=reminders)


if __name__ == '__main__':
    with app.app_context():
        Base.metadata.create_all(engine)
        app.run(debug=True)
