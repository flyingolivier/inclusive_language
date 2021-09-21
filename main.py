import sys
import argparse
from parser import Parser
from pretty_print import PrettyPrint

class Main:
    def parse_arguments(self):
        parser = argparse.ArgumentParser(
            description='Identifies non-inclusive words in a text and suggests alternative ones that could be used instead.',
            epilog='Output returns the submitted text with the non-inclusive words highlighted and alternative suggestions for each word. Returned status code is 1 if there are suggestions, 0 otherwise.'
        )
        parser.add_argument('text', help='The text to be analyzed. Either the text surrounded by quotes or the path to a file.')
        parser.add_argument('--text-lang', default="en", help='The language the text to analyze is written in. Needs a corresponding glossary under /glossaries. Defaults to "en"')
        parser.add_argument('--output-lang', default="en", help='The language for the output. Needs a corresponding translation file under /languages. Defaults to "en"')
        self.args = parser.parse_args()
        
        try:
            with open(self.args.text, 'r') as file:
                self.text = file.read()
        except FileNotFoundError:
            self.text = self.args.text
          
    
    def run(self):
        self.parse_arguments()
    
        parser = Parser(self.text, self.args.text_lang)
        parser.parse()

        if len(parser.findings) > 0:
            PrettyPrint(parser, self.args.output_lang).render()
            sys.exit(1)
        else:
            sys.exit(0)   
            
Main().run()
