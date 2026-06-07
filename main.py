import flask 
import supabase
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

supabase: Client = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_KEY")
)

app = Flask(__name__)

@app.route("/")
def home():
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8550)