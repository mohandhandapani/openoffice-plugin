import MendeleyDesktopAPI 

import unittest

# API functions that can't be tested without manual user interaction
class TestMendeleyDesktopAPI_Interactive(unittest.TestCase):

    def setUp(self):
        self.api = MendeleyDesktopAPI.MendeleyDesktopAPI("component context (unused)")

    def test_citationStyle_choose_interactive(self):
        chosenStyle = self.api.citationStyle_choose_interactive("http://www.zotero.org/styles/apa")
        print "chosen style = " + chosenStyle

    def test_citation_choose_interactive(self):
        chosenFieldCode = self.api.citation_choose_interactive()
        print "chosen field code = " + chosenFieldCode
    
if __name__ == '__main__':
    unittest.main()