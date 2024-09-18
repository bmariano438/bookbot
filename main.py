def main():
  book_path = "books/frankenstein.txt"
  book_text = get_book_text(book_path)
  num_words = get_num_words(book_text)
  chars_dict = get_chars_dict(book_text)
  chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

  print(f"--- Begin report of {book_path} ---")
  print(f"{num_words} words found in the document\n")

  for item in chars_sorted_list:
    char = item["char"]
    num = item["num"]
    if char.isalpha():
      print(f"The '{char}' character was found {num} times")
  
  print("--- End report ---")

def get_num_words(text):
  words = text.split()
  return len(words)

def sort_on(dict):
  return dict["num"]

def chars_dict_to_sorted_list(chars_dict):
  sorted_list = []
  for ch in chars_dict:
    sorted_list.append({ "char" : ch, "num" : chars_dict[ch] })
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list

def get_chars_dict(text):
  chars = {}
  for c in text:
    lowered = c.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars

def get_book_text(path):
  with open(path) as f:
    return f.read()


main()