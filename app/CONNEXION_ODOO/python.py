from flask import Flask, render_template, request, redirect, flash
import odoorpc

app = Flask(__name__)
app.secret_key = "5f2c7f3b8e2e4b9a3d6b8e1f75c12aaf098cf2f3df1c27eb"  # Clé secrète pour les sessions

# Configuration Odoo
ODOO_HOST = "localhost"  # Adresse de votre serveur Odoo
ODOO_PORT = 8069         # Port Odoo par défaut


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Récupérer les données du formulaire
        db_name = request.form.get("db_name")  # Nom de la base de données
        email = request.form.get("email")      # Email utilisateur
        password = request.form.get("password")  # Mot de passe utilisateur

        try:
            # Connexion au serveur Odoo
            odoo = odoorpc.ODOO(ODOO_HOST, port=ODOO_PORT)
            odoo.login(db_name, email, password)

            # Si connexion réussie, redirigez vers l'interface web d'Odoo
            return redirect(f"http://{ODOO_HOST}:{ODOO_PORT}/web?db={db_name}")

        except Exception as e:
            # En cas d'erreur (connexion échouée)
            flash(f"Erreur de connexion : {str(e)}")
            return redirect("/")

    # Afficher le formulaire de connexion
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
