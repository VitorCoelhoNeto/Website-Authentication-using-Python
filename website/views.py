from flask import Blueprint, jsonify, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST']) # We need to specify which methods are allowed on this page
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash("Note too short", category='error')
        else:
            newNote = Note(data=note, userId=current_user.id)
            db.session.add(newNote)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)



@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)

    if note:
        print("Note exists")
        if note.userId == current_user.id:
            print("User owns note")
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({})