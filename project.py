import re

def main():

    stop_word = generate_stop_word()

    words = read_data()

    new_word = replace_word(words, *stop_word)
    list = list_word(new_word)

    dict_word = total_word(list)
    generate_file_txt(dict_word)

# merender semua kata dari file stop_word.txt
def generate_stop_word():
    stop_word = []

    with open('stop_words.txt', 'r') as file:
        for f in file:
            stop_word.append(f.strip())

    return stop_word

def read_data():
    file_data = ""
    file_name = 'data.txt'

    with open(file_name, 'r') as file:
        file_data = file.read()

    return file_data

# menghapus kata yang sama dengan stop_word
def replace_word(s, *stop_word):

    new_word = s
    for remove in stop_word:

        pattern = r'\b{}\b'.format(re.escape(remove))
        new_word = re.sub(pattern, '', new_word)

    return new_word

# return list - membersihkan karakter ""
def list_word(s):
    new_list = []
    list = s.split(" ")

    for l in list:
        if(l != ""):
            new_list.append(l)

    return new_list


# return dictionary dari hasil penjumlahan kata yang sama
def total_word(s):

    words = {}
    for str in s:

        if str.lower() in words:
            words[str.lower()] += 1
        else:
            words[str.lower()] = 1

    return words


# membuat file baru (txt) / hasil dari menjumlahkan semua kata yang sama
def generate_file_txt(data):

    file_name = "result.txt"

    with open(file_name, 'w') as file:
        for key, value in data.items():
            file.write(f'{key}: {value}\n')

    print("Created")

if __name__ == "__main__":
    main()