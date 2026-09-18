import os
import time

from flask import Flask, Response, g, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    Counter,
    Histogram,
    generate_latest,
)

db = SQLAlchemy()

REQUEST_COUNT = Counter(
    "cloudcart_http_requests_total",
    "Total HTTP requests handled by CloudCart",
    ["method", "endpoint", "status"],
)

REQUEST_LATENCY = Histogram(
    "cloudcart_http_request_duration_seconds",
    "CloudCart HTTP request latency",
    ["method", "endpoint"],
)


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

    @app.before_request
    def start_timer():
        g.request_start_time = time.perf_counter()

    @app.after_request
    def record_metrics(response):
        if request.path != "/metrics":
            endpoint = request.endpoint or "unknown"

            REQUEST_COUNT.labels(
                method=request.method,
                endpoint=endpoint,
                status=response.status_code,
            ).inc()

            duration = time.perf_counter() - g.request_start_time

            REQUEST_LATENCY.labels(
                method=request.method,
                endpoint=endpoint,
            ).observe(duration)

        return response

    @app.get("/")
    def home():
        return render_template("index.html")

    @app.post("/notes")
    def create_note():
        data = request.get_json(silent=True) or {}

        text = data.get("text", "").strip()

        if not text:
            return jsonify({
                "error": "text is required"
            }), 400

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

    @app.get("/version")
    def version():
        return jsonify({
            "version": "v4",
            "message": "CloudCart with Prometheus metrics on Amazon EKS"
        }), 200

    @app.get("/metrics")
    def metrics():
        return Response(
            generate_latest(),
            content_type=CONTENT_TYPE_LATEST
        )

    return app


if __name__ == "__main__":
    app = create_app()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
