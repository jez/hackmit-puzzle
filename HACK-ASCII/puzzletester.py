#!/usr/bin/env python3

from puzzle import *

def checkSingleLine(puzzle, puzzleID, hashedID):
  for line in puzzle:
    if line == hashedID:
      return line

  return None


def checkPairedLines(puzzle, puzzleID, hashedID):
  for i in range(len(puzzle) - 2):
    addedLines = hex(int(puzzle[i], 16) + int(puzzle[2], 16))[-57:-1]
    if hashedID == addedLines:
      return i + 1

  return None


if __name__ == '__main__':
  puzzleID = loadPuzzleID()
  decodedPuzzleID = decodeHex(puzzleID)

  puzzle = Puzzle()

  puzzle.registerTest('single line check', checkSingleLine)
  puzzle.registerTest('paired line check', checkPairedLines)

  puzzle.registerPuzzleID(puzzleID)
  puzzle.registerPuzzleID('4841434b' + puzzleID)
  puzzle.registerPuzzleID(decodedPuzzleID)
  puzzle.registerPuzzleID('HACK' + decodedPuzzleID)
  puzzle.registerPuzzleID(('HACK' + decodedPuzzleID) * 2)

  puzzle.runTests()
