from flask import Flask, render_template, request, redirect, session
from flask_cors import CORS
import database as db
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
CORS(app)

# Home page - Login
@app.route("/", methods=["GET", "POST"])
@app.route("/index.html", methods=["GET", "POST"])
def index():
    # Handle redirect parameter (VULNERABILITY: Open Redirect)
    if request.method == "GET" and request.args.get("redirect"):
        redirect_url = request.args.get("redirect")
        return redirect(redirect_url)

    # Handle login
    if request.method == "POST":
        student_id = request.form.get("student_id")
        password = request.form.get("password")

        # Check credentials (VULNERABILITY: SQL Injection in login)
        user = db.checkLogin(student_id, password)

        if user:
            session['student_id'] = student_id
            session['name'] = user['name']
            return redirect("/dashboard.html")
        else:
            error = "Invalid credentials"
            return render_template("index.html", error=error)

    return render_template("index.html")


# Dashboard - View grades
@app.route("/dashboard.html", methods=["GET"])
def dashboard():
    if 'student_id' not in session:
        return redirect("/")

    # Get student grades (VULNERABILITY: SQL Injection in grade lookup)
    student_id = request.args.get("id", session['student_id'])
    grades = db.getGrades(student_id)

    return render_template("dashboard.html",
                         name=session.get('name'),
                         grades=grades,
                         student_id=student_id)


# Submit assignment
@app.route("/submit.html", methods=["GET", "POST"])
def submit():
    if 'student_id' not in session:
        return redirect("/")

    if request.method == "POST":
        assignment_name = request.form.get("assignment")
        link = request.form.get("link")

        # Save submission (VULNERABILITY: SQL Injection in insert)
        db.submitAssignment(session['student_id'], assignment_name, link)

        message = "Assignment submitted successfully!"
        return render_template("submit.html", message=message)

    return render_template("submit.html")


# Profile update
@app.route("/profile.html", methods=["GET", "POST"])
def profile():
    if 'student_id' not in session:
        return redirect("/")

    if request.method == "POST":
        email = request.form.get("email")
        phone = request.form.get("phone")

        # Update profile (VULNERABILITY: SQL Injection in update)
        db.updateProfile(session['student_id'], email, phone)

        success = "Profile updated successfully!"
        return render_template("profile.html", success=success)

    # Get current profile
    profile_data = db.getProfile(session['student_id'])
    return render_template("profile.html", profile=profile_data)


# Announcements
@app.route("/announcements.html", methods=["GET", "POST"])
def announcements():
    if 'student_id' not in session:
        return redirect("/")

    if request.method == "POST":
        comment = request.form.get("comment")

        # Save comment (VULNERABILITY: SQL Injection + XSS)
        db.addComment(session['student_id'], comment)

    # Get all announcements and comments (VULNERABILITY: XSS in display)
    announcements_list = db.getAnnouncements()
    comments_list = db.getComments()

    return render_template("announcements.html",
                         announcements=announcements_list,
                         comments=comments_list)


# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True, host="0.0.0.0", port=5000)
