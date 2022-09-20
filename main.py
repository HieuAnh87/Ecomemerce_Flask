from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.shop import app


if __name__ == "__main__":
    app.run(debug=True)