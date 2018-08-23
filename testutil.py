import os, unittest, pyutils

class TestPyUtils(unittest.TestCase):
  def test_for_edits(self):
    testFileLocation = os.path.join(os.path.dirname(__file__), 'test')
    testAFile = os.path.join(testFileLocation, 'testA.c')
    testBFile = os.path.join(testFileLocation, 'testB.c')

    status = pyutils.checkForEditsOutsideIfDef(testAFile, testBFile)

    self.assertEqual(status, 1, 'Returned with incorrect status %d' % status)

if __name__ == '__main__':
  unittest.main()