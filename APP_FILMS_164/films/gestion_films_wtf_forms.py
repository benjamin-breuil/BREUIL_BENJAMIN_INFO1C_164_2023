"""Gestion des formulaires avec WTF pour les films
Fichier : gestion_films_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, NumberRange, DataRequired
from wtforms.validators import Regexp
from wtforms.widgets import TextArea


class FormWTFAddFilm(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_film_regexp = ""
    nom_film_add_wtf = StringField("Nom du film ", validators=[Length(min=2, max=2000, message="min 2 max 20"),
                                                               Regexp(nom_film_regexp,
                                                                      message="Pas de chiffres, de caractères "
                                                                              "spéciaux, "
                                                                              "d'espace à double, de double "
                                                                              "apostrophe, de double trait union")
                                                               ])
    description_technique = StringField("Description technique ", validators=[Length(min=2, max=2000, message="min 2 max 20"),
                                                               Regexp(nom_film_regexp,
                                                                      message="Pas de chiffres, de caractères "
                                                                              "spéciaux, "
                                                                              "d'espace à double, de double "
                                                                              "apostrophe, de double trait union")
                                                               ])

    submit = SubmitField("Enregistrer la technique")


class FormWTFUpdateFilm(FlaskForm):
    """
        Dans le formulaire "film_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    nom_film_update_wtf = StringField("Clavioter le nom", widget=TextArea())
    desc_technique_update = StringField("Clavioter la description", widget=TextArea())

    submit = SubmitField("Update film")


class FormWTFDeleteFilm(FlaskForm):
    """
        Dans le formulaire "film_delete_wtf.html"

        nom_film_delete_wtf : Champ qui reçoit la valeur du film, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "film".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_film".
    """
    nom_film_delete_wtf = StringField("Effacer cette technique")
    submit_btn_del_film = SubmitField("Effacer technique")
    submit_btn_conf_del_film = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
