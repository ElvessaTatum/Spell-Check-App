import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.process_text import process_text

EXCEPTION_MESSAGE = "Spell check error"

class ProcessTextTests(unittest.TestCase):
  def test_canary(self):
    self.assertTrue(True)

  def test_process_empty_text(self):
    self.assertEqual(process_text(''), '')

  def test_process_text_hello(self):
    self.assertEqual(process_text('hello'), 'hello')

  def test_process_text_blah_which_we_will_considered_wrong_spelling(self):
    self.assertEqual(process_text('blah', lambda word: False), '[blah]')

  def test_process_text_good_morning(self):
    self.assertEqual(process_text('good moring'), 'good moring')

  def test_process_text_guud_morning_which_we_will_considered_wrong_spelling_for_the_first_word(self):
    self.assertEqual(process_text('guud morning', lambda word: word != 'guud'), '[guud] morning')

  def test_process_text_good_marning_which_we_will_considered_wrong_spelling_for_the_second_word(self):
    self.assertEqual(process_text('good marning', lambda word: word != 'marning'), 'good [marning]')

  def test_process_text_hello_guud_marning_which_we_will_considered_wrong_spelling_for_the_second_and_third_word(self):
    self.assertEqual(process_text('hello guud marning', lambda word: word not in ['guud', 'marning']), 'hello [guud] [marning]')

  def test_process_text_helo_good_marning_which_we_will_considered_wrong_spelling_for_the_first_and_third_word(self):
    self.assertEqual(process_text('helo good marning', lambda word: word not in ['helo', 'marning']), '[helo] good [marning]')

  def test_process_text_takes_text_with_two_lines_and_returns_text_with_two_lines(self):
    input_text = '''hello world
    good morning'''
    output_text = input_text

    self.assertEqual(process_text(input_text), output_text)

  def test_process_text_takes_text_with_two_lines_with_some_incorrect_spelling_words_and_returns_appropriate_result(self):
    input_text = '''helo wrld
    good marning'''
    output_text = '''[helo] [wrld]
    good [marning]'''
    
    self.assertEqual(process_text(input_text, lambda word: word not in ['helo', 'wrld', 'marning']), output_text)

  def test_process_text_takes_text_with_three_lines_and_returns_text_with_three_lines(self):
    input_text = '''hello world
    good morning
    how are you'''
    output_text = input_text
    
    self.assertEqual(process_text(input_text), output_text)

  def test_process_text_takes_text_with_three_lines_with_some_incorrect_spelling_words_and_returns_appropriate_result(self):
    input_text = '''hello wrld
    guud marning
    hew r u'''
    output_text = '''hello [wrld]
    [guud] [marning]
    [hew] [r] [u]'''
    
    self.assertEqual(process_text(input_text, lambda word: word not in ['wrld', 'guud', 'marning', 'hew', 'r', 'u']), output_text)

  def test_process_text_takes_text_hello_there_how_aare_you_but_runs_into_an_exception_from_the_spell_checker_when_looking_up_spelling_for_there(self):
    def mock_is_spelling_correct(word):
      if word == 'there':
        raise Exception(EXCEPTION_MESSAGE)

      return word != 'aare'

    self.assertEqual(process_text('hello there how aare you', mock_is_spelling_correct), 'hello _there_ how [aare] you')

if __name__ == '__main__': 
  unittest.main()
