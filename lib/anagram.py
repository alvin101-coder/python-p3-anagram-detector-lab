# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)
    
    def match(self, potential_anagrams):
        matches = []
        
        for possible in potential_anagrams:
            if sorted(possible) == self.sorted_word:
                matches.append(possible)
        
        return matches
