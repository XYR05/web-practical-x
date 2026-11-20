from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/result", methods=["POST"])
def result():
    name = request.form.get("name", "").strip()
    marks_text = request.form.get("marks", "").strip()

    if not name or not marks_text:
        return render_template("result.html", error="All fields are required.")

    try:
        marks = float(marks_text)
        if marks < 0 or marks > 100:
            raise ValueError
    except ValueError:
        return render_template("result.html", error="Enter marks between 0 and 100.")

    status = "Pass" if marks >= 40 else "Needs Improvement"
    return render_template("result.html", name=name, marks=marks, status=status)

if __name__ == "__main__":
    app.run(debug=True)
