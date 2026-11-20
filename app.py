import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "replace-this-with-a-long-random-secret"
DATABASE = "secure_demo.db"

def connect_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def setup():
    with connect_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        # Demonstration account only; use password hashing in real applications.
        db.execute(
            "INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)",
            ("student", "LabPass123")
        )

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        with connect_db() as db:
            user = db.execute(
                "SELECT id, username FROM users WHERE username=? AND password=?",
                (username, password)
            ).fetchone()
        if user:
            session.clear()
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect(url_for("dashboard"))
        flash("Invalid username or password.")
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        comment = request.form.get("comment", "").strip()
        if not comment or len(comment) > 200:
            flash("Enter a comment of 1 to 200 characters.")
        else:
            # Parameterised query prevents input from becoming SQL syntax.
            with connect_db() as db:
                db.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                           ("comment_" + str(session["user_id"]), comment))
            flash("Input accepted and stored as data.")
    return render_template("dashboard.html", username=session["username"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

setup()
if __name__ == "__main__":

    app.run(debug=True)
