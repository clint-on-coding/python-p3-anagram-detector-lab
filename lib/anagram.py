# your code goes here!

class Anagram:
    def __init__(self, word):
        # normalize once so comparisons are easy
        self._word = word
        self._norm = word.lower()
        self._sig = sorted(self._norm)

    def match(self, candidates):
        matches = []
        for cand in candidates:
            norm = cand.lower()
            # don't match the exact same word; compare sorted letters
            if norm != self._norm and sorted(norm) == self._sig:
                matches.append(cand)
        return matches

