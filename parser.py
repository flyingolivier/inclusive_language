import yaml
import sys
from string_utils import StringUtils

class Parser:
    def __init__(self, text, lang):
        self.text = text
        self.lang = lang
        self.findings = []
        self.glossary = self.glossary()

    def glossary(self):
        with open(f"glossaries/{self.lang}.yml", "r") as file:
            yaml_string = file.read().lower()
        return yaml.safe_load(yaml_string)
    
    def uninclusive_words(self):
        return [w for w in self.glossary.keys()]
    
    def suggestions(self, word):
        return self.glossary.get(word)
 
    def parse(self): 
        words = StringUtils().remove_punctuation(self.text).lower().split()
        
        for word in words:
            if word in self.uninclusive_words() and word not in self.findings:
                self.findings.append(word)