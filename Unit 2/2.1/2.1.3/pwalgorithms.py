# Module pwalgorithms

# get words from password dictionary file
#from main import WordvPhrase


def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

def two_word(password):
  words = get_dictionary()
  guesses = 0
  for w in words:
    for w2 in words:
      guesses += 1
      test_password = w + w2
      if test_password == password:
        return True, guesses
  return False, guesses

def ComboWord(password):
  words = get_dictionary()
  guesses = 0
  for w in words:
    for w2 in words:
      for i in range(0,10):
        guesses += 1
        if w + w2 + str(i)== password or w + str(i)+ w2 == password or str(i)+ w + w2 == password:
          return True, guesses
  return False, guesses