import csv
import string
import openpyxl

def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def check_contain_only_english(check_str):
    ctr = 0
    for en in check_str:
        if 97 <= ord(en) <= 122:
            ctr += 0
        elif 65 <= ord(en) <= 90:
            ctr += 0
        elif ord(en) == 39:
            ctr += 0
        else:
            ctr += 1
    if ctr != 0:
        # Not only English
        return True
    else:
        return False


def totalNumber(word_count, word):
    if word not in word_count:
        word_count.setdefault(word, []).append(1)
    else:
        count = word_count[word][0]
        count += 1
        word_count[word][0] = count


def AppearYears(word_count, word, year):
    if word not in word_count:
        word_count.setdefault(word, []).append(year)
    else:
        if year not in word_count[word]:
            word_count[word].append(year)


def sorting(word_count):
    return sorted(word_count, key=lambda x: x[0], reverse=True)


def check_contain_selection(check_str):
    if check_str is '(A)' or check_str is '(B)' or check_str is '(C)' or check_str is '(D)' or check_str is '(E)' \
            or check_str is '(F)' or check_str is '(G)' or check_str is '(H)' or check_str is '(I)' \
            or check_str is '(J)':
        return True
    else:
        return False


# 刪除 標點符號 !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
# translator = str.maketrans('', '', string.punctuation)
# We have to save the apostrophe
translator = str.maketrans('', '', '!"#()$%&\*+,-./:;<=>?@[\\]^_`{|}~，。；、：？！（）“”〝〞‵′「」')

word_count = {}
# -------------------83-107-------------------------------------------------------------------------------
# main()
for i in range(83, 108):
    year = str(i)
    ctr = 0
    text = open('D:\\Justin\'s_University\\專題(learning)\\txt\\GSAT\\'+str(i)+'.txt').read()
    words = text.split()
    for word in words:
        # checking Chinese words
        if check_contain_chinese(word):
            pass
        # selection
        elif check_contain_selection(word):
            pass
        # checking only English or with apostrophe
        elif check_contain_only_english(word):
            pass
        else:
            word = word.translate(translator).lower()
            # totalNumber(word_count, word)
            if word not in word_count:
                word_count.setdefault(word, {})
                word_count[word]['word'] = word
                word_count[word]['total'] = 1
            else:
                count = word_count[word]['total']
                count += 1
                word_count[word]['total'] = count
            # AppearYears(word_count, word, year)
            if year not in word_count[word]:
                word_count[word][year] = 1
            else:
                ctr = word_count[word][year]
                ctr += 1
                word_count[word][year] = ctr

# -------------別忘了 91-2, 92-2-------------------------------------------------------------------------
for i in range(91, 93):
    year = str(i)
    ctr = 0
    # 開91-2 和 92-2的檔案
    text = open('D:\\Justin\'s_University\\專題(learning)\\txt\\GSAT\\'+str(i)+'-2'+'.txt').read()
    words = text.split()
    for word in words:
        # checking Chinese words
        if check_contain_chinese(word):
            pass
        # selection
        elif check_contain_selection(word):
            pass
        # checking only English or with apostrophe
        elif check_contain_only_english(word):
            pass
        else:
            word = word.translate(translator).lower()
            # totalNumber(word_count, word)
            if word not in word_count:
                word_count.setdefault(word, {})
                word_count[word]['word'] = word
                word_count[word]['total'] = 1
            else:
                count = word_count[word]['total']
                count += 1
                word_count[word]['total'] = count
            # AppearYears(word_count, word, year)
            if year not in word_count[word]:
                word_count[word][year] = 1
            else:
                ctr = word_count[word][year]
                ctr += 1
                word_count[word][year] = ctr
# -----------------------------------------------------------------------------------------------------------
# print(word_count)


word_count_dict = sorted(word_count.items(), key=lambda x: x[1]['word'], reverse=False)
# 現在資料長相--> 'because' : ['total_number':132,'83':4,'84':5,'85':3,.........,'107':2]

# # whole list
# print(word_count_dict)
# print(type(word_count_dict))
#
# # the first word
# print(word_count_dict[0])
# print(type(word_count_dict[0]))
#
# # what does it has in dict
# print(word_count_dict[0][1])
# print(type(word_count_dict[0][1]))


years_list = [str(year) for year in range(83, 108)]
years_list = ['word'] + ['total'] + years_list
# years_list --> ['words','total',83,84,85,86,.....,107]
#
# for i in word_count_dict:
#     print(i)
#
with open('D:\\Justin\'s_University\\專題(learning)\\Software\\Word_Count\\output\\'+'final'+'.csv', 'w',\
          newline='') as csvFile:
    dictWriter = csv.DictWriter(csvFile, fieldnames=years_list)
    dictWriter.writeheader()

    for i in word_count_dict:
        output = i[1]
        print(output)
        dictWriter.writerow(output)
