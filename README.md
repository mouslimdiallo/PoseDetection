# PoseDetection 🎯
Code Python pour la détection des articulations des mains avec MediaPipe et cvzone.

# Introduction 📌 
Ce projet utilise OpenCV, MediaPipe et cvzone pour détecter et suivre les articulations des mains en temps réel via une webcam. Il permet d'afficher les coordonnées des points clés de la main et d'interagir avec l'image capturée.

# Installation 🚀
Avant de commencer, assure-toi d'avoir Python installé sur ton système. Ensuite, suis ces étapes :

1. Cloner le repository
bash git clone https://github.com/mouslimdiallo/PoseDetection.git

2. Créer un environnement virtuel (recommandé)
python -m venv venv

3. Installer les dépendances
pip install -r requirements.txt
Si le fichier requirements.txt n'existe pas, installe manuellement les bibliothèques :

pip install opencv-python cvzone mediapipe

🎯 Utilisation
Lance le script principal pour activer la détection des mains via la webcam :
python test.py

🔬 Fonctionnalités
✅ Détection des articulations des mains 
✅ Identification de la main gauche/droite 
✅ Affichage des landmarks et de la boîte englobante 
✅ Interaction avec l'image capturée en temps réel

🛠️ Structure du projet
PoseDetection/
│── test.py                # Script principal
│── Pose2-Couverture.jpg   # Image de couverture
│── requirements.txt       # Liste des dépendances
│── .gitignore             # Fichiers à exclure du versionnement
│── README.md              # Documentation du projet
🖼️ Exemple d'affichage

Une capture d'écran du projet en action

# Contribuer 🤝 
Les contributions sont les bienvenues ! Clone ce repo, améliore le projet et propose un Pull Request. Ça fait plaisir...

📜 Licence
Ce projet est sous licence MIT, donc libre d'utilisation et de modification.
