import unittest

import amg.sanitize as sanitize


class TestSanitize(unittest.TestCase):

  def test_normalize_tag_case(self):
    """ Fix tag capitalization. """
    references = {"A Little Test": "A Little Test",
                  "I Like L.A": "I Like L.A",
                  "Of The Moon": "Of the Moon",
                  "Just A Bunch Of Letters": "Just a Bunch of Letters",
                  "Episode VI": "Episode VI",
                  "EPISODE VIA": "Episode Via",
                  "VI VI VI": "VI VI VI",
                  "Episode VI: name": "Episode VI: Name",
                  "Matsya - The Fish": "Matsya - The Fish"}
    for before, after in references.items():
      self.assertEqual(sanitize.normalize_tag_case(before), after)
