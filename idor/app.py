from flask import Flask, render_template, redirect, url_for

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
    15: {'title': 'Buffalo Bill Show', 'date': '2024-08-18', 'public': True}
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
        return render_template('flag.html', date=date)
    else:
        return redirect(url_for('index'))

# Redirection 302 si le chemin /flag est accédé sans date
@app.route('/flag')
def flag_redirect():
    return render_template('flag.html', date=None)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
