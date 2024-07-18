from flask import Flask, render_template, redirect, url_for, send_from_directory

app = Flask(__name__)

# Exemple de données d'événements
events = {
    1: {'title': 'Rodeo Show', 'date': '2024-07-20', 'public': True},
    2: {'title': 'Town Meeting', 'date': '2024-07-22', 'public': False},
    3: {'title': 'Sheriff Election', 'date': '2024-07-25', 'public': True},
    4: {'title': 'Secret Council', 'date': '2024-07-30', 'public': False},
    5: {'title': 'Farmers Market', 'date': '2024-07-21', 'public': True},
    6: {'title': 'Bandit Capture', 'date': '2024-07-24', 'public': True},
    7: {'title': 'Saloon Night', 'date': '2024-07-27', 'public': True},
    8: {'title': 'Cattle Auction', 'date': '2024-07-28', 'public': False},
    9: {'title': "Mayor's Speech", 'date': '2024-08-01', 'public': True},
    10: {'title': 'Council Dinner', 'date': '2024-08-02', 'public': False},
    11: {'title': 'Gold Rush Festival', 'date': '2024-08-05', 'public': True},
    12: {'title': 'Pioneer Day', 'date': '2024-08-10', 'public': True},
    13: {'title': 'Western Dance', 'date': '2024-08-12', 'public': True},
    14: {'title': 'Horse Riding Competition', 'date': '2024-08-15', 'public': True},
    15: {'title': 'Buffalo Bill Show', 'date': '2024-08-18', 'public': True},
    16: {'title': 'Gunfight Reenactment', 'date': '2024-08-20', 'public': True},
    17: {'title': 'Stagecoach Tour', 'date': '2024-08-22', 'public': False},
    18: {'title': 'Railroad Celebration', 'date': '2024-08-25', 'public': True},
    19: {'title': 'Native American History Day', 'date': '2024-08-27', 'public': False},
    20: {'title': 'Barn Dance', 'date': '2024-08-29', 'public': True},
    21: {'title': 'Wild West Show', 'date': '2024-08-31', 'public': True},
    22: {'title': 'Frontier Days', 'date': '2024-09-02', 'public': True},
    23: {'title': 'Western Film Screening', 'date': '2024-09-05', 'public': False},
    24: {'title': 'Ranch Tour', 'date': '2024-09-07', 'public': True},
    25: {'title': 'Chuckwagon Cook-Off', 'date': '2024-09-10', 'public': True},
    26: {'title': 'Mining Expedition', 'date': '2024-09-12', 'public': True},
    27: {'title': 'Riverboat Cruise', 'date': '2024-09-15', 'public': True},
    28: {'title': 'Trail Ride', 'date': '2024-09-18', 'public': False},
    29: {'title': 'Cowboy Poetry Reading', 'date': '2024-09-20', 'public': True},
    30: {'title': 'Western Art Exhibition', 'date': '2024-09-22', 'public': True}
}

# Page d'accueil
@app.route('/')
def index():
    public_events = {k: v for k, v in events.items() if v['public']}
    return render_template('index.html', events=public_events)

# Détails de l'événement (vulnérabilité IDOR ici)
@app.route('/event/<int:event_id>')
def event_detail(event_id):
    event = events.get(event_id)
    if not event:
        return "Event not found", 404
    return render_template('event.html', event=event)

# Page de flag accessible par une date spécifique
@app.route('/flag/<date>')
def flag(date):
    secret_event_date = '2024-07-30'
    if date == secret_event_date:
        return redirect(url_for('download_elf'))
    else:
        return redirect(url_for('index'))

# Route pour télécharger le fichier .elf
@app.route('/download_elf')
def download_elf():
    return send_from_directory(directory='static', path='farwest_quiz.elf', as_attachment=True)

# Redirection 302 si le chemin /flag est accédé sans date
@app.route('/flag')
def flag_redirect():
    return render_template('flag.html', date=None)

if __name__ == '__main__':
    app.run(debug=True)
