"""Gestion des "routes" FLASK et des données pour les genres.
Fichier : gestion_genres_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.personnes.gestion_personnes_wtf_forms import FormWTFAjouterGenres
from APP_FILMS_164.personnes.gestion_personnes_wtf_forms import FormWTFDeleteGenre
from APP_FILMS_164.personnes.gestion_personnes_wtf_forms import FormWTFUpdateGenre

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /personnes_afficher
    
    Test : ex : http://127.0.0.1:5575/personnes_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_genre_sel = 0 >> tous les genres.
                id_genre_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/personnes_afficher/<string:order_by>/<int:id_genre_sel>", methods=['GET', 'POST'])
def personnes_afficher(order_by, id_genre_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_genre_sel == 0:
                    strsql_personnes_afficher = """SELECT t_personne.*, t_email.adresse_email AS nom_email, t_num_tel.num_tel AS num_tel, t_adresse.*
                                                        FROM t_personne
                                                        LEFT JOIN t_email ON t_personne.fk_email = t_email.id_email
                                                        LEFT JOIN t_num_tel ON t_personne.fk_num_tel = t_num_tel.id_num_tel
                                                        LEFT JOIN t_adresse ON t_personne.fk_adresse = t_adresse.id_adresse
                                                        """
                    mc_afficher.execute(strsql_personnes_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_personne"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_genre_selected_dictionnaire = {"value_id_genre_selected": id_genre_sel}
                    strsql_personnes_afficher = """SELECT id_personne, prenom, nom, fk_adresse, fk_num_tel, fk_email  FROM t_personne WHERE id_personne = %(value_id_genre_selected)s"""

                    mc_afficher.execute(strsql_personnes_afficher, valeur_id_genre_selected_dictionnaire)
                else:
                    strsql_personnes_afficher = """SELECT id_personne, prenom, nom, fk_adresse, fk_num_tel, fk_email  FROM t_personne ORDER BY id_personne DESC"""

                    mc_afficher.execute(strsql_personnes_afficher)

                data_genres = mc_afficher.fetchall()

                print("data_genres ", data_genres, " Type : ", type(data_genres))

                # Différencier les messages si la table est vide.
                if not data_genres and id_genre_sel == 0:
                    flash("""La table "t_personne" est vide. !!""", "warning")
                elif not data_genres and id_genre_sel > 0:
                    # Si l'utilisateur change l'id_genre dans l'URL et que le genre n'existe pas,
                    flash(f"Le genre demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_personne" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données genres affichés !!", "success")

        except Exception as Exception_personnes_afficher:
            raise ExceptionGenresAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{personnes_afficher.__name__} ; "
                                          f"{Exception_personnes_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("personnes/personnes_afficher.html", data=data_genres)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /genres_ajouter
    
    Test : ex : http://127.0.0.1:5575/genres_ajouter
    
    Paramètres : sans
    
    But : Ajouter un genre pour un film
    
    Remarque :  Dans le champ "name_genre_html" du formulaire "genres/genres_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/personnes_ajouter_wtf", methods=['GET', 'POST'])
def personnes_ajouter_wtf():
    form = FormWTFAjouterGenres()
    try:
        if request.method == "POST" and form.submit.data:
            name_genre_wtf = form.nom_genre_wtf.data
            nom_personne = name_genre_wtf.lower()

            prenom_personne_wtf = form.prenom_genre_wtf.data
            prenom_personne = prenom_personne_wtf.lower()

            email_fk = form.email_dropdown_wtf.data

            numtel_fk = form.num_dropdown_wtf.data

            adresse_fk = form.adresse_dropdown_wtf.data


            valeurs_insertion_dictionnaire = {"value_intitule_personne": nom_personne,
                                              "value_prenom_personne": prenom_personne,
                                              "value_email_fk": email_fk,
                                              "value_numtel_fk" : numtel_fk,
                                              "value_adresse_fk" : adresse_fk
                                              }
            print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

            strsql_insert_genre = """INSERT INTO t_personne (id_personne,nom,prenom,fk_email, fk_num_tel, fk_adresse) VALUES (NULL,%(value_intitule_personne)s,%(value_prenom_personne)s,%(value_email_fk)s, %(value_numtel_fk)s, %(value_adresse_fk)s)"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(strsql_insert_genre, valeurs_insertion_dictionnaire)

            flash(f"Données insérées !!", "success")
            print(f"Données insérées !!")

            # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
            return redirect(url_for('personnes_afficher', order_by='DESC', id_genre_sel=0))

        elif request.method == "GET":
            with DBconnection() as mc_afficher:
                strsql_email_dropdown = """SELECT * FROM t_email ORDER BY id_email ASC"""
                mc_afficher.execute(strsql_email_dropdown)
            data_email = mc_afficher.fetchall()
            print("gestion_personnes_crud.py data_email ", data_email, " Type : ", type(data_email))
            email_val_list_dropdown = []
            for i in data_email:
                email_val_list_dropdown = [(i["id_email"], i["adresse_email"]) for i in data_email]
            form.email_dropdown_wtf.choices = email_val_list_dropdown

            with DBconnection() as ntc_afficher:
                strsql_num_tel_dropdown = """SELECT * FROM t_num_tel ORDER BY id_num_tel ASC"""
                ntc_afficher.execute(strsql_num_tel_dropdown)
            data_num_tel = ntc_afficher.fetchall()
            print("gestion_personnes_crud.py data_email ", data_num_tel, " Type : ", type(data_num_tel))
            numtel_val_list_dropdown = []
            for i in data_num_tel:
                numtel_val_list_dropdown = [(i["id_num_tel"], i["num_tel"]) for i in data_num_tel]
            form.num_dropdown_wtf.choices = numtel_val_list_dropdown

            with DBconnection() as adc_afficher:
                strsql_adresse_dropdown = """SELECT * FROM t_adresse ORDER BY id_adresse ASC"""
                adc_afficher.execute(strsql_adresse_dropdown)
            data_adresse = adc_afficher.fetchall()
            print("gestion_personnes_crud.py data_email ", data_adresse, " Type : ", type(data_adresse))
            adresse_val_list_dropdown = []
            for i in data_adresse:
                adresse_val_list_dropdown = [(i["id_adresse"], i["rue"])  for i in data_adresse]
            form.adresse_dropdown_wtf.choices = adresse_val_list_dropdown



    except Exception as Exception_personnes_ajouter_wtf:
        raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                        f"{personnes_ajouter_wtf.__name__} ; "
                                        f"{Exception_personnes_ajouter_wtf}")

    return render_template("personnes/personnes_ajouter_wtf.html", form=form)

"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /genre_update
    
    Test : ex cliquer sur le menu "genres" puis cliquer sur le bouton "EDIT" d'un "genre"
    
    Paramètres : sans
    
    But : Editer(update) un genre qui a été sélectionné dans le formulaire "personnes_afficher.html"
    
    Remarque :  Dans le champ "nom_personne_updater_wtf" du formulaire "genres/personne_updater_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/personne_update_wtf", methods=['GET', 'POST'])
def personne_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_genre"
    id_genre_update = request.values['id_personne_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateGenre()
    try:
        if request.method == "POST":
            # Récupèrer la valeur du champ depuis "personne_updater_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            name_genre_update = form_update.nom_personne_updater_wtf.data
            name_genre_update = name_genre_update.lower()

            prenom_pers_update = form_update.prenom_personne_updater_wtf.data
            prenom_pers = prenom_pers_update.lower()

            update_email_fk = form_update.email_dropdown_update_wtf.data

            update_numtel_fk = form_update.num_dropdown_update_wtf.data

            update_adresse_fk = form_update.adresse_dropdown_update_wtf.data

            valeur_update_dictionnaire = {"value_id_genre": id_genre_update,
                                          "value_name_genre": name_genre_update,
                                          "value_prenom_pers": prenom_pers,
                                          "value_update_email": update_email_fk,
                                          "value_update_numtel": update_numtel_fk,
                                          "value_update_adresse": update_adresse_fk
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_intitulegenre = """UPDATE t_personne SET nom = %(value_name_genre)s, prenom = %(value_prenom_pers)s, fk_email = %(value_update_email)s, fk_num_tel = %(value_update_numtel)s, fk_adresse = %(value_update_adresse)s WHERE id_personne = %(value_id_genre)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_intitulegenre, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_genre_update"
            return redirect(url_for('personnes_afficher', order_by="DESC", id_genre_sel=id_genre_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_personne"
            str_sql_id_genre = "SELECT id_personne, nom, prenom, fk_email, fk_num_tel, fk_adresse FROM t_personne " \
                               "WHERE id_personne = %(value_id_genre)s"
            valeur_select_dictionnaire = {"value_id_genre": id_genre_update}
            print(valeur_select_dictionnaire)
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_genre, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_nom_genre = mybd_conn.fetchone()


            with DBconnection() as mc_afficher:
                    strsql_email_dropdown = """SELECT * FROM t_email ORDER BY id_email ASC"""
                    mc_afficher.execute(strsql_email_dropdown)
            data_email = mc_afficher.fetchall()
            print("gestion_personnes_crud.py data_email ", data_email, " Type : ", type(data_email))
            email_val_list_dropdown = []
            for i in data_email:
                email_val_list_dropdown = [(i["id_email"], i["adresse_email"]) for i in data_email]
            form_update.email_dropdown_update_wtf.choices = email_val_list_dropdown

            with DBconnection() as ntc_afficher:
                strsql_num_tel_dropdown = """SELECT * FROM t_num_tel ORDER BY id_num_tel ASC"""
                ntc_afficher.execute(strsql_num_tel_dropdown)
            data_num_tel = ntc_afficher.fetchall()
            print("gestion_personnes_crud.py data_email ", data_num_tel, " Type : ", type(data_num_tel))
            numtel_val_list_dropdown = []
            for i in data_num_tel:
                numtel_val_list_dropdown = [(i["id_num_tel"], i["num_tel"]) for i in data_num_tel]
            form_update.num_dropdown_update_wtf.choices = numtel_val_list_dropdown

            with DBconnection() as adc_afficher:
                strsql_adresse_dropdown = """SELECT * FROM t_adresse ORDER BY id_adresse ASC"""
                adc_afficher.execute(strsql_adresse_dropdown)
            data_adresse = adc_afficher.fetchall()
            print("gestion_personnes_crud.py data_email ", data_adresse, " Type : ", type(data_adresse))
            adresse_val_list_dropdown = []
            for i in data_adresse:
                adresse_val_list_dropdown = [(i["id_adresse"], i["rue"]) for i in data_adresse]
            form_update.adresse_dropdown_update_wtf.choices = adresse_val_list_dropdown

            # Afficher la valeur sélectionnée dans les champs du formulaire "personne_updater_wtf.html"
            form_update.nom_personne_updater_wtf.data = data_nom_genre["nom"]
            form_update.prenom_personne_updater_wtf.data = data_nom_genre["prenom"]
    except Exception as Exception_personne_updater_wtf:
        raise ExceptionGenreUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{personne_update_wtf.__name__} ; "
                                      f"{Exception_personne_updater_wtf}")

    return render_template("personnes/personne_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /genre_delete
    
    Test : ex. cliquer sur le menu "genres" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "personnes_afficher.html"
    
    Remarque :  Dans le champ "nom_personne_delete_wtf" du formulaire "genres/personne_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/personne_delete_wtf", methods=['GET', 'POST'])
def personne_delete_wtf():
    data_films_attribue_genre_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_genre"
    id_genre_delete = request.values['id_genre_btn_delete_html']

    # Objet formulaire pour effacer le genre sélectionné.
    form_delete = FormWTFDeleteGenre()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("personnes_afficher", order_by="ASC", id_genre_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "genres/personne_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_films_attribue_genre_delete = session['data_films_attribue_genre_delete']
                print("data_films_attribue_genre_delete ", data_films_attribue_genre_delete)

                flash(f"Effacer le genre de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_genre": id_genre_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_films_genre = """DELETE FROM t_personne WHERE id_personne = %(value_id_genre)s"""
                # Manière brutale d'effacer d'abord la "fk_genre", même si elle n'existe pas dans la "t_genre_film"
                # Ensuite on peut effacer le genre vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_films_genre, valeur_delete_dictionnaire)

                flash(f"Genre définitivement effacé !!", "success")
                print(f"Genre définitivement effacé !!")

                # afficher les données
                return redirect(url_for('personnes_afficher', order_by="ASC", id_genre_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_genre": id_genre_delete}
            print(id_genre_delete, type(id_genre_delete))

            # Requête qui affiche tous les films_genres qui ont le genre que l'utilisateur veut effacer
            str_sql_genres_films_delete = """SELECT nom FROM t_personne
                                            WHERE id_personne = %(value_id_genre)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_genres_films_delete, valeur_select_dictionnaire)
                data_films_attribue_genre_delete = mydb_conn.fetchall()
                print("data_films_attribue_genre_delete...", data_films_attribue_genre_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "genres/personne_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_films_attribue_genre_delete'] = data_films_attribue_genre_delete

                # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_personne"
                str_sql_id_genre = "SELECT nom FROM t_personne WHERE id_personne = %(value_id_genre)s"

                mydb_conn.execute(str_sql_id_genre, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom genre" pour l'action DELETE
                data_nom_genre = mydb_conn.fetchone()

            # Afficher la valeur sélectionnée dans le champ du formulaire "personne_delete_wtf.html"
            form_delete.nom_genre_delete_wtf.data = data_nom_genre["nom"]

            # Le bouton pour l'action "DELETE" dans le form. "personne_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_personne_delete_wtf:
        raise ExceptionGenreDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{personne_delete_wtf.__name__} ; "
                                      f"{Exception_personne_delete_wtf}")

    return render_template("personnes/personne_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_films_attribue_genre_delete)
