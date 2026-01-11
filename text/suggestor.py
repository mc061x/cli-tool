from prompt_toolkit.auto_suggest import AutoSuggest, Suggestion

class MySuggsetor(AutoSuggest):
    words : list

    def __init__(self, words: list):
        self.words = words

    def get_suggestion(self, buffer, document):
        text = document.text.rsplit("\n", 1)[-1]
        if text.strip():
            for word in self.words:
                if word.startswith(text):
                    return Suggestion(word[len(text) :])
        return None
    
    def getWordList(self):
        return self.words
    
    def updateWordList(self, newList: list):
        self.words = newList