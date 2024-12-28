from flask import Flask, render_template, request, redirect, flash
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)
app.secret_key = "5f2c7f3b8e2e4b9a3d6b8e1f75c12aaf098cf2f3df1c27ea"  # Remplacez par une clé secrète sécurisée

@app.route("/", methods=["GET", "POST"])
def connect_db():
    if request.method == "POST":
        # Récupérer les informations du formulaire
        host = request.form.get("host")
        port = request.form.get("port")
        dbname = request.form.get("dbname")
        user = request.form.get("user")
        password = request.form.get("password")

        try:
            # Tentative de connexion à la base de données PostgreSQL
            connection = psycopg2.connect(
                host=host,
                port=port,
                dbname=dbname,
                user=user,
                password=password
            )
            connection.close()
            flash("Connexion réussie à la base de données PostgreSQL.", "success")
        except OperationalError as e:
            flash(f"Erreur de connexion : {e}", "danger")

        return redirect("/")

    return render_template("login2.html")

if __name__ == "__main__":
    app.run(debug=True)
