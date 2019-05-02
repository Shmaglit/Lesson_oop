'''
1. Создайте класс Word.
2. Добавьте свойства text и part of speech.
3. Добавьте возможность создавать объект слово со значениями в скобках.
4. Создайте класс Sentence
5. Добавьте свойство content, равное списку, состоящему из номеров слов, входящих в предложение.
6. Добавьте метод show, составляющий предложение.
7. Добавьте метод show_parts, отображающий, какие части речи входят в предложение.
'''

import re
import pymorphy2


class Word:
    def __init__(self, text='None', part_of_speech='None'):
        self.text = text
        self.part_of_speech = part_of_speech


class Septence:
    def __init__(self, sep='', content=[]):
        self.sep = sep
        self.content = content

    def show(self):
        s = ' '.join(self.sep)
        return s.capitalize()

    def show_parts(self):
        s1_var = self.sep.lower()
        s1_var = re.sub(' - ', ' ', s1_var)
        li = re.split(' |, |: ', s1_var)
        morph = pymorphy2.MorphAnalyzer()
        dic = {'NOUN': 'имя существительное', 'ADJF': 'имя прилагательное (полное)',
                      'ADJS': 'имя прилагательное (краткое)', 'COMP': 'компаратив', 'VERB': 'глагол (личная форма)',
                      'INFN': 'глагол (инфинитив)', 'PRTF': 'причастие (полное)', 'PRTS': 'причастие (краткое)',
                      'GRND': 'деепричастие', 'NUMR': 'числительное', 'ADVB': 'наречие',
                      'NPRO': 'местоимение-существительное', 'PRED': 'предикатив', 'PREP': 'предлог', 'CONJ': 'союз',
                      'PRCL': 'частица', 'INTJ': 'междометие'}
        m = {}
        for i in range(0,len(li)):
            morph_temp = morph.parse(li[i])[0]
            m[li[i]] = dic[morph_temp.tag.POS]
        return m


word1 = Word('number', 'hello world')
print(word1.text)
print(word1.part_of_speech)

s = Septence()
s.sep = 'В этой статье собраны самые интересные, популярные и полезные туристические сайты'
s.content = [n+1 for n in range(0, len(re.findall('\w{3,}', s.sep)))]
print(s.sep)
print(s.content)

s2 = Septence()
s2.sep = ['в', 'этой', 'статье', 'собраны','сайты']
print(s2.show())

print(s.show_parts())


