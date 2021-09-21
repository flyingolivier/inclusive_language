import re

class StringUtils:
    def remove_punctuation(self, text):
        return re.sub(r'[^\w\s]', '', text)

    def list_to_sentence(self, list, last_word):
        if len(list) == 0:
            return ''
        if len(list) == 1:
            return list[0]
        if len(list) == 2:
            return list[0] + ' ' + last_word + ' ' + list[1]
        return ', '.join(list[:-1]) + ', ' + last_word + ' ' + list[-1]
