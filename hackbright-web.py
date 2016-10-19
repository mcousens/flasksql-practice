from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    return render_template("student_info.html", first=first, last=last, 
                            github=github)


@app.route("/student-form")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add", methods=['GET'])
def get_add_form():
    """Show form for adding students"""

    return render_template("student_add.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    first_name = request.form.get('firstname')
    last_name = request.form.get('lastname')
    github = request.form.get('github')
    hackbright.make_new_student(first_name, last_name, github)
    return render_template('add_confirmation.html', first=first_name, last=last_name, github=github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
