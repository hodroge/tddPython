import os
import unittest
#from mycode import * #il reconnait pas l'omport donct essayer avec le deuxième
import mycode
#mycode qui est deja definir sur une autre page est importer
# et s"'appel "m" ou laisser le mycode
# **import mycode as m

class MyFirstTest(unittest.TestCase):
	print ("heelo")
	#majuscukle pour la premère lettre
	"""Classe modélisant une testeur"""
	#tj commencer par "C" majuscule pour la classe
	#attibut de classe
	
	def test_hello(self):
		self.assertEqual(mycode.hello_world(),"hello world")

#quand on commence pour la première def en miniscule, il faut continuer de meme format
	def test_Score_Calculation_joseph(self):
		print ("coucou")
#self.appel test unitaire (la fonction(mycode) ou si ** m (parametre de fonction, ce qu'on veux afficher)
		self.assertEqual(mycode.calcule_score("joseph",15),"66%" )

	def test_Score_Calculation_marie(self):
		print ("patate")
		self.assertEqual(mycode.calcule_score("marie", 33), "50%")

	def test_Score_Calculation_marc(self):
		print ("marc")
		self.assertEqual(mycode.calcule_score("marc", 60), "43%")
	def test_Score_Calculation_ely(self):
		print ("ali")
		self.assertEqual(mycode.calcule_score("ely", 28), "75%")

if __name__=='__main__':
	unittest.main()

