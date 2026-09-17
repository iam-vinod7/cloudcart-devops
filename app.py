import os

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)


def create_app(test_config=None):
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "sqlite:///notes.db"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.post("/notes")
    def create_note():
        data = request.get_json(silent=True) or {}
        text = data.get("text", "").strip()

        if not text:
            return jsonify({"error": "text is required"}), 400

        note = Note(text=text)

        db.session.add(note)
        db.session.commit()

        return jsonify({
            "id": note.id,
            "text": note.text
        }), 201

    @app.get("/notes")
    def get_notes():
        notes = Note.query.order_by(Note.id).all()

        return jsonify([
            {
                "id": note.id,
                "text": note.text
            }
            for note in notes
        ]), 200

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
