import re

class Highlighter:
    styles = {
        "default":      "\033[39m",
        "black":        "\033[30m",
        "red":          "\033[31m",
        "green":        "\033[32m",
        "yellow":       "\033[33m",
        "blue":         "\033[34m",
        "magenta":      "\033[35m",
        "cyan":         "\033[36m",
        "lightgray":    "\033[37m",
        "darkgray":     "\033[90m",
        "lightred":     "\033[91m",
        "lightgreen":   "\033[92m",
        "lightyellow":  "\033[93m",
        "lightblue":    "\033[94m",
        "lightmagenta": "\033[95m",
        "lightcyan":    "\033[96m",
        "white":        "\033[97m",
        "bold":         "\033[1m",
    }
    
    default_style = styles.get("default")
    
    def __init__(self, style):
        self.style = self.styles.get(style)
    
    def highlight(self, word, in_text=None):
        if in_text is None:
            in_text = word
        return re.sub(r"\b%s\b" % word, f"{self.style}{word}{self.default_style}", in_text)
