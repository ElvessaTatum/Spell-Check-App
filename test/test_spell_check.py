import unittest
import sys
import os
from unittest.mock import patch

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.spell_check import get_response, parse_response, is_spelling_correct

EXCEPTION_MESSAGE = "Spell check error"

class SpellCheckTests(unittest.TestCase):
  def test_parse_response_for_a_word_returns_a_value(self):
    self.assertGreater(len(get_response('hello')), 0)
    
  def test_get_response_for_a_word_returns_true_value(self):
    self.assertTrue(parse_response('true'))

  def test_get_response_for_a_word_returns_false_value(self):
    self.assertFalse(parse_response('false'))

  def test_is_spelling_correct_calls_get_response_and_parse_response_to_check_the_spelling(self):
    with patch('src.spell_check.get_response') as mock_get_response, patch('src.spell_check.parse_response') as mock_parse_response:
      tested_word = 'hello'
      expected_resposne = 'true'
      expected_result = True

      mock_get_response.return_value = expected_resposne
      mock_parse_response.return_value = expected_result
      
      result = is_spelling_correct(tested_word)

      mock_get_response.assert_called_with(tested_word)
      mock_parse_response.assert_called_with(expected_resposne)
      self.assertEqual(result, expected_result)

  def test_is_spelling_correct_passes_on_the_exception_from_get_response(self):
    with patch('src.spell_check.get_response') as mock_get_response:
      tested_word = 'hello'

      mock_exception = Exception(EXCEPTION_MESSAGE)
      mock_get_response.side_effect = mock_exception

      with self.assertRaises(Exception) as message: is_spelling_correct(tested_word)
      self.assertEqual(str(message.exception), str(mock_exception))

if __name__ == '__main__': 
  unittest.main()
