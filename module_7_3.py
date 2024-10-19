
file_names = []


class WordsFinder:

    def __init__(self, *args):
        self.args = args
        file_names.append(args)

    def get_all_words(self):
        all_words = {}
        with open(file_names, encoding='utf-8') as file:
            for i in file:
                print(i)
        return f'{self.args }'


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего