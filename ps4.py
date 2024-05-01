import pygame
import pyautogui

# Initialisation de pygame
pygame.init()

# Détection des manettes de jeu
pygame.joystick.init()

# Vérification du nombre de manettes détectées
num_joysticks = pygame.joystick.get_count()
if num_joysticks < 1:
    print("Aucune manette détectée.")
    quit()

# Sélection de la première manette détectée
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Boucle de lecture des événements
running = True
button_7_pressed = False
button_8_pressed = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYBUTTONDOWN:
            # Vérifier si le bouton 7 est pressé
            if event.button == 7:
                button_7_pressed = True
            # Vérifier si le bouton 8 est pressé
            elif event.button == 8:
                button_8_pressed = True
                
            # Vérifier si les boutons 7 et 8 sont pressés simultanément
            if button_7_pressed and button_8_pressed:
                # Émettre une pression sur la touche "W" du clavier
                while button_7_pressed and button_8_pressed:
                    pyautogui.keyDown('w')
                    for event in pygame.event.get():
                        if event.type == pygame.JOYBUTTONUP:
                            if event.button == 7:
                                button_7_pressed = False
                            elif event.button == 8:
                                button_8_pressed = False
                                # Lorsque le bouton 8 est relâché, relâchez la touche "W" du clavier
                                pyautogui.keyUp('w')

        elif event.type == pygame.JOYBUTTONUP:
            # Réinitialiser l'état des boutons lorsque le bouton est relâché
            if event.button == 7:
                button_7_pressed = False
            elif event.button == 8:
                button_8_pressed = False

# Arrêt de pygame
pygame.quit()
