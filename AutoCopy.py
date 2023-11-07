import json
import keyboard
import win32clipboard
import time
import sys

# Load data from a JSON file
with open('./List.json', 'r') as fichier:
    donnees = json.load(fichier)

cles = list(donnees.keys())

def copy_to_clipboard(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text)
    win32clipboard.CloseClipboard()

for i in range(len(cles)):
	cle_actuelle = cles[i]
	valeur_actuelle = donnees[cle_actuelle]

	print(i)
	print(f"Clé: {cle_actuelle}")
	print(f"Valeur: {valeur_actuelle}")

    # Copy the value to the clipboard
	copy_to_clipboard(valeur_actuelle)
	print("La valeur a été copiée dans le presse-papiers. Attente de détection de collage...")

    # Wait for the paste action
	keyboard.wait('ctrl+v')
	time.sleep(0.1)
	print("La valeur a été collée. Passage à la clé suivante.")
	print("")

for i in range(3, 0, -1):
    sys.stdout.write(f"\rToutes les valeurs ont été traitées, fermeture du script dans {i} secondes")
    sys.stdout.flush()
    time.sleep(1)

# Empty the clipboard
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.CloseClipboard()
keyboard.unhook_all()
exit()
