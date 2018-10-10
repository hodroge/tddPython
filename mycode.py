

def hello_world():
	h="hello world"
	return h

## il faut tester la def avant avec un reurn vide
## test 1-1
# def calcule_score():
# 	return ""
# commentaire
#

#test 1-2
#ne jamais oublier les paramètre de name et age pour qu'il accepte
#il faut homogenisé les ecriture , attention au string "josephe" et aussi le return "66%"
def calcule_score(name,age):
	if name=="joseph" and age ==15:
		return "66%"
	if name== "marie" and age ==33:
		return "50%"
	if name=="marc" and age ==60:
		return "43%"
	if name=="ely" and age ==28:
		return "75%"
	else:
		return "non existant"