import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialisation du détecteur de mains
detector = HandDetector(detectionCon=0.8, maxHands=2)  # Confiance minimum et nombre maximum de mains
cap = cv2.VideoCapture(0)  # Capture vidéo depuis la webcam

if not cap.isOpened():
    print("Erreur : Impossible d'accéder à la caméra.")
    exit()

while True:
    success, img = cap.read()
    if not success:
        print("Erreur : Impossible de capturer la vidéo.")
        break

    # Détection des mains
    hands, img = detector.findHands(img)  # Détection des mains et annotation de l'image

    # Vérifier si des mains sont détectées
    if hands:
        for hand in hands:
            lmList = hand['lmList']  # Liste des landmarks de la main
            bbox = hand['bbox']      # Boîte englobante de la main
            handType = hand['type']  # Type de main : "Left" ou "Right"

            print(f"Main détectée : {handType}")
            print(f"Landmarks : {lmList}")
            print(f"Boîte englobante : {bbox}")

    # Affichage de la vidéo avec les articulations connectées
    cv2.imshow("Hand Detection", img)

    # Quitter avec 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
