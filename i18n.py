import yaml
import sys

class I18n:
    def __init__(self, lang, scope):
        self.scope = scope.split('.')
        with open(f"languages/{lang}.yml", "r") as stream:
            self.yaml_content = yaml.safe_load(stream)
            
            for scope in self.scope:
                self.yaml_content = self.yaml_content.get(scope)        
            
    def t(self, key):
        return self.yaml_content.get(key)
