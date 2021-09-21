# Inclusive Language

This Python script looks for non inclusive words in a text and suggests alternative ones that could be used instead. Writing inclusive language avoid excluding people from your audience on the basis of gender, sexual preference, age, race, ability, cultural background etc. The script does not try to be smart and does not understand the context of the text. Personal judgement and commons sense should apply when looking at its output. 

## Requirements
`python 3.x`

## Usage
```bash
python3 main.py --help

usage: main.py [-h] [--text-lang TEXT_LANG] [--output-lang OUTPUT_LANG] text

Identifies non-inclusive words in a text and suggests alternative ones that could be used instead.

positional arguments:
  text                  The text to be analyzed. Either the text surrounded by quotes or the path to a file.

optional arguments:
  -h, --help            show this help message and exit
  --text-lang TEXT_LANG
                        The language the text to analyze is written in. Needs a corresponding glossary under /glossaries. Defaults to "en"
  --output-lang OUTPUT_LANG
                        The language for the output. Needs a corresponding translation file under /languages. Defaults to "en"

Output returns the submitted text with the non-inclusive words highlighted and alternative suggestions for each word. Returned status code is 1 if there are suggestions, 0 otherwise.
```

## Example
```
python3 main.py "That's one small step for man, one giant leap for mankind."

################################################################################################################################################################
#                                                                                                                                                              #
# The following words in the provided text could, context permitting, be replaced by more inclusive ones. See below for a list of suggestions.                 #
#                                                                                                                                                              #
################################################################################################################################################################

**Submitted text**
   That's one small step for man, one giant leap for mankind.

**Recommendations**
   Instead of **man** consider **humanity**, **people**, or **humankind**
   Instead of **mankind** consider **humanity**, **people**, or **humankind**
```

## Disclaimer
This script come without warranty of any kind. Review its code and use it at your own risk. 
I assume no liability for the accuracy, correctness, completeness, or usefulness of any information the script returns nor for any sort of damages it may cause.