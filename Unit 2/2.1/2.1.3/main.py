# a213_pw_analyzer.py
import time
import pwalgorithms as pwa
from pwalgorithms import *

WordvPhrase = input("Would you like to search for a password or passphrase (word/phrase/combination) ")
if WordvPhrase == "word":
  password = input("Enter password:")

  print("Analyzing a one-word password ...")
  time_start = time.time()

  # attempt to find password
  found, num_guesses = pwa.one_word(password)
  time_end = time.time()

  # report results
  if (found):
    print(password, "found in", num_guesses, "guesses")
  else: 
    print(password, "NOT found in", num_guesses, "guesses!")
  print("Time:", format((time_end-time_start), ".8f"))

if WordvPhrase == "phrase":
  passphrase = input("Enter passphrase: ")

  print("Analyzing a two-word password ...")
  time_start = time.time()

  # attempt to find password
  found2, num_guesses = pwa.two_word(passphrase)
  time_end = time.time()

  # report results
  if (found2):
    print(passphrase, "found in", num_guesses, "guesses")
  else: 
    print(passphrase, "NOT found in", num_guesses, "guesses!")
  print("Time:", format((time_end-time_start), ".8f"))

if WordvPhrase == "Combo":
  Combo = input("Enter combination: ")

  print("Analyzing a combination password ...")
  time_start = time.time()

  # attempt to find password
  found3, num_guesses = pwa.ComboWord(Combo)
  time_end = time.time()

  # report results
  if (found3):
    print(Combo, "found in", num_guesses, "guesses")
  else: 
    print(Combo, "NOT found in", num_guesses, "guesses!")
  print("Time:", format((time_end-time_start), ".8f"))






