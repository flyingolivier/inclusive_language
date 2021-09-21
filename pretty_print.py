from i18n import I18n
from highlighter import Highlighter
from string_utils import StringUtils

class PrettyPrint:
    def __init__(self, parser, lang):
        self.parser = parser
        self.i18n = I18n(lang, "inclusive_language")

    def render(self):
        if len(self.parser.findings) == 0:
            return

        print(self.i18n.t("intro"))    
        print(Highlighter("bold").highlight(self.i18n.t("text")))
        self.print_highlighted_text()
        print(Highlighter("bold").highlight(self.i18n.t("recommendations")))
        self.print_suggestions()

    def print_highlighted_text(self):
        text = self.parser.text
        for finding in self.parser.findings:
            text = Highlighter("yellow").highlight(word = finding, in_text = text)
            text = Highlighter("yellow").highlight(word = finding.capitalize(), in_text = text)
        print("  ", text, "\n")

    def print_suggestions(self):
        for finding in self.parser.findings:
            suggestions = [Highlighter("green").highlight(w) for w in self.parser.suggestions(finding)]
            print("  ", 
                self.i18n.t("instead_of"), Highlighter("yellow").highlight(finding),
                self.i18n.t("consider"), StringUtils().list_to_sentence(suggestions, self.i18n.t("or"))
            )