import hashlib

def sha224sum(source):
  return hashlib.sha224(source.encode('utf-8')).hexdigest()


def decodeHex(source):
  return bytes.fromhex(source).decode('utf-8')


def loadPuzzleID(filename = 'puzzleid.txt'):
  # Load the puzzle ID as given on the website
  with open(filename, 'r') as f:
    return f.read().rstrip('\n')


class Puzzle():
  def __init__(self, filename = 'puzzle.txt'):
    self.tests = {}
    self.puzzleIDs = []

    # Load the puzzle text (500 lines)
    with open(filename, 'r') as f:
      self.puzzle = [line.rstrip('\n') for line in f.readlines()]

  def runTests(self):
    for name, test in self.tests.items():
      for puzzleID in self.puzzleIDs:
        hashedID = sha224sum(puzzleID)

        print("Testing:", name)
        print("puzzleID =", puzzleID)
        print("hashedID =", hashedID)

        result = test(self.puzzle, puzzleID, hashedID)

        if result:
          assert isinstance(result, int)
          print('success! line:', result)
        else:
          assert result is None
          print('...nope.')

  def registerTest(self, name, test):
    """
    Register a test to be run.

    @param name A name to be printed for debugging
    @param test A function that has the following signature:
                puzzle : list of lines from the puzzle text
                puzzleID : a puzzleID represented as a string
                hashedID : the hashed version of that puzzleID
    """
    assert isinstance(name, str)
    assert callable(test)

    self.tests[name] = test

  def registerPuzzleID(self, puzzleID):
    """
    Register a puzzleID string to run the tests on.
    """
    assert isinstance(puzzleID, str)

    self.puzzleIDs.append(puzzleID)

