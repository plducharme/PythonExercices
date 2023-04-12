# Ouvrir le fichier 'cc.xlarge.png' en mode binaire

# Les 8 premiers sont la signature du fichier
# afficher chaque element de la signature
#   - Premier byte est le nombre magique representant un png
#   - 3 prochains bytes, PNG en ASCII
#   - 2 prochains bytes, \r\n
#   - 1 byte pour EOF 0x1A
#   - 1 byte \n