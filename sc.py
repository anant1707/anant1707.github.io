from spellchecker import SpellChecker

def autocorrect(word):
	spell = SpellChecker()

	# find those words that may be misspelled
	misspelled = spell.unknown(word)

	e=0
	a=spell.correction(word)
	print(a)
	return a

	    # Get a list of `likely` options
	   # print(spell.candidates(word))


autocorrect("pythin")