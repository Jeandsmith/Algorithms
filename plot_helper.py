
from tkinter import font
from typing import Sized
from Algorithms import TrieTree
import tkinter as tk

#  Will be using the gutenberg collection of documents to test the trie tree
# import nltk
from nltk.corpus import gutenberg as gt

trie = TrieTree()

#  Insert all the words into the trie
for fileid in gt.fileids():
    for word in gt.words(fileid):
        trie.insert(word.lower())

# print(shakespeare_macbeth)
# print(trie.root.data)

# # Test the autome complete by typing someting
# # I think I will make a TK gui to illutrate the auto complete

root = tk.Tk()
root.geometry("1200x800")

frame = tk.Frame(root)
frame.pack()

label = None

def search_word():

    global label

    # Get the input text from the field
    result = trie.autocomplete(search_field.get().lower())
    print(result)

    if label is not None:
        label.destroy()

    label = tk.Label(master=root, text=', '.join(result), wraplength=700, font=('Times New Roman', '20'))
    label.pack()

#  Create the search field
header = tk.Label(root, text="Search Autocomplete With Trie Tree", font=('Times New Roman', '40'), pady=10)
header.pack()
search_field = tk.Entry(frame, width=30)
search_field.insert(0, 'Search')
search_field.pack(padx=5, pady=20)
button_search = tk.Button(frame, text='Search', command=search_word)
button_search.pack(pady=30)


root.mainloop()
