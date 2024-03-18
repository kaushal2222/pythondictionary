def character_dict(word):
 char_count_dict = dict()
 for each_character in word:
    char_count_dict[each_character] = char_count_dict.get(each_character, 0) + 1
 sorted_list_keys = sorted(char_count_dict.keys())
 for each_key in sorted_list_keys:
     print(each_key, char_count_dict.get(each_key))
def main():
 word = input("Enter a string ")
 character_dict(word)
if __name__ == "__main__":
 main()
