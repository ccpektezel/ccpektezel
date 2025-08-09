from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "replace-this-with-a-secure-key"

# Simple user store
users = {
    "admin": "password123"
}

# Sample data for the dashboard
metrics = {
    "shipments_processed": 1280,
    "shipments_in_transit": 230,
    "average_delivery_time": 3.4,
}

@app.route("/")
def dashboard():
    """Render the logistics dashboard."""
    return render_template("index.html", metrics=metrics)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Render login form and handle authentication."""
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if users.get(username) == password:
            session["user"] = username
            return redirect(url_for("dashboard"))
        error = "Invalid credentials"
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    """Log the user out and redirect to login page."""
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
