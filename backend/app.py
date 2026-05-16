from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class LessonPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    objective = db.Column(db.Text)
    summary = db.Column(db.Text)
    planned_date = db.Column(db.String(100))
    discipline = db.Column(db.String(100))
    contents = db.Column(db.Text)
    support_resources = db.Column(db.Text)
    tags = db.Column(db.Text)

    with app.app_context():
        db.create_all()

@app.route('/')
def home():
    return {"message": "API funcionando"}


@app.route('/health')
def health():
    return {"status": "ok"}


if __name__ == '__main__':
    app.run(debug=True)