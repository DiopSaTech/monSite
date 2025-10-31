from flask import Flask, render_template, request, flash, redirect, url_for 
import os

app = Flask(__name__)
app.secret_key = 'votre_clé_secrète_ici'  # Changez ceci en production    



import json
from datetime import datetime


# Ajoute sur render mon site web perso
PROJECTS = [
    {"title": "Site perso", "link": "https://diopsakhewar.com"},
    {"title": "Projet local", "link": None},  # lien désactivé
]



# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Page à propos
@app.route('/about')
def about():
    return render_template('about.html')

# Page projets

@app.route('/projects')
def projects():
    projects_list = [
        {
            'title': 'Projet 1',
            'description': 'Site E-commerce',
            'technologies': ['HTML', 'CSS', 'MySQL', 'PHP'],
            'image': 'images/ecommerce.jpg',  # ✅ Correct
            'link': 'https://github.com/DiopSaTech/projet1'
        },
        {
            'title': 'Projet 2',
            'description': 'Système de management hôpital',
            'technologies': ['Scene Builder', 'JDBC', 'MySQL', 'JavaFX'],
            'image': 'images/hopital.jpg',  # ✅ (pas image1, et pas /static/)
            'link': 'https://github.com/DiopSaTech'
        },
        {
            'title': 'Projet 3',
            'description': 'Application chat',
            'technologies': ['Python', 'Django channels', 'Web sockets'],
            'image': 'images/chat.png',  # ✅ Assure-toi que le fichier existe
            'link': 'https://github.com/DiopSaTech'
        },
        {
            'title': 'Projet 4',
            'description': 'Architecture réseau entreprise multi-sites',
            'technologies': ['Conception infrastructure avec VLANs', 'routage inter-VLAN'
'Mise en place de liaisons VPN site-à-site (IPsec)',
'Configuration de redondance (HSRP/VRRP)'],
            'image': 'images/archi_multisites.jpg',
          #  'link': 'https://github.com/DiopSaTech'
        }, 
        {

            'title': 'Projet 5',
            'description': 'Solution de téléphonie IP (ToIP',
            'technologies': ['Déploiement un serveur Asterisk',
'Configuration de postes SIP et routage appels',
'Intégration avec passerelle RTC',
'Mise en place de la QoS pour prioriser le trafic voix'],
            'image': 'images/voixIP.png',
          #  'link': 'https://github.com/DiopSaTech'
        }, 
        {
            'title': 'Projet 6',
            'description': 'Etude de plateforme forensique',
            'technologies': ['Autopsy', 'Volatility'],
            'image': 'images/forensic.png',
          #  'link': 'https://github.com/DiopSaTech'
        }, 
         {
            'title': 'Projet 7 (21H)',
            'description': 'HACKATHON 2025/2026: Optimisation de la stratégie vaccinale contre la grippe - prédiction des besoins et amélioration accès aux soins',
            'technologies': ['Machine learning', 'python', 'css', 'flask'],
            'image': 'images/hacKathon.png',
            'link': 'https://github.com/DiopSaTech'
        },
    ]
    return render_template('projects.html', projects=projects_list)




@app.route('/cyber-ml')
def cyber_ml():
    return render_template('cyber-ml.html')







# Page contact
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Ici, vous pourriez envoyer un email ou sauvegarder dans une base de données
        # Pour l'instant, on affiche juste un message de confirmation
        flash(f'Merci {name} ! Votre message a été envoyé avec succès.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    #app.run(debug=True) 
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
