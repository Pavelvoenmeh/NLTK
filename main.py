import nltk
import random

from deep_translator import GoogleTranslator
def _to_str(text):

    text1 = ''
    for i in text:
        text1 = text1 + ' ' + i

    is_noun = lambda pos: pos[:2] == 'NN'
    tokenized = nltk.word_tokenize(text1)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    return nouns


def _dict(text,dict):
    while len(dict) < 15:
        word = str(random.choice(text))
        word_rus = GoogleTranslator(source='auto', target='ru').translate(word)
        if len(word) > 4:
            dict[word] = word_rus

def _most_common(text):
    a = nltk.FreqDist(text)
    count = a.most_common(100)
    c = 0
    prov = ',--".;:atheandtoofinit\'that-!" ."?soiswithasTheforAndnotonoverwhatifbyButbutFromfromwasWasWerewere,"?"'
    for i in count:
        if (i[0] not in prov ) and (c<30):
            print('Слово \"'+i[0]+'\" повторяется', i[1],'раз')
            c=c+1
def _similar(text):
    a = input('Введетие слово, для которого необходимо найти похожие слова: ')
    b = 0
    while b==0:
        try:
            b = int(input('\nВведите глубину поиска: '))
        except:
            print('\nВведите цифру\n')
    text.similar(a, b)
def _generate(text):
    text.generate()
def _common_contexts(text):
    a = input('Введите слово для поиска: ')
    text.common_contexts([a])
def main():
    print('\n-------------------------------------\nИспользуется текст bryant-stories.txt\n-------------------------------------\n')
    ch = 1
    text = nltk.Text(nltk.corpus.gutenberg.words('bryant-stories.txt'))
    nouns = _to_str(text)
    dict = {}
    while ch != 0 :
        m1 = '1. Сформировать словарь\n'
        m2 = '2. Вывести самые часто повторяющиеся слова\n'
        m3 = '3. Показать похожие слова\n'
        m4 = '4. Сгенерировать текст наподобие оригинала\n'
        m5 = '5. Показать в каком месте встречается слово\n'
        m0 = '0. Выход\n'
        a = 'Выбран пункт '
        print('\n-------------------------------------\n'+m1+m2+m3+m4+m5+m0,
              '-------------------------------------\n')
        try:
            ch = int(input('Выберите пункт меню: '))
        except:
            print('Введено некорректное значение\n')
        if ((ch>5) or (ch<0)):
            print('Введите корректное значение\n')
        else:
            if ch == 1:
                print(a, m1)
                _dict(nouns, dict)
                for item in dict.items():
                    print('Eng:',item[0],'\nRus:',item[1],'\n')



            elif ch == 2:
                print(a, m2)
                _most_common(text)

            elif ch == 3:
                print(a, m3)
                _similar(text)

            elif ch == 4:
                print(a, m4)
                _generate(text)

            elif ch == 5:
                print(a, m5)
                _common_contexts(text)
main()
