import sys
from flask import Flask, render_template_string
from config import Config
from models import db, Post, Comment
from sqlalchemy import inspect, exc

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def home():
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    post_exists = 'post' in tables
    comment_exists = 'comment' in tables

    if post_exists and comment_exists:
        return render_template_string("""
        <h1>✅ Database is ready.</h1>
        <p>Post and Comment tables exist.</p>
        """)
    else:
        return render_template_string("""
        <h1>❌ Database setup incomplete.</h1>
        <p>Missing tables: 
            {% if not post_exists %} Post {% endif %}
            {% if not comment_exists %} Comment {% endif %}
        </p>
        """), 500

with app.app_context():
    inspector = inspect(db.engine)
    try:
        if 'post' not in inspector.get_table_names():
            Post.__table__.create(db.engine)
            print("✅ Post table created.")
        else:
            print("✅ Post table already exists.")

        if 'comment' not in inspector.get_table_names():
            Comment.__table__.create(db.engine)
            print("✅ Comment table created.")
        else:
            print("✅ Comment table already exists.")

    except exc.SQLAlchemyError as e:
        print("❌ Error occurred while creating tables:", e)
        sys.exit(1)

if __name__ == '__main__':
    app.run(debug=True)
