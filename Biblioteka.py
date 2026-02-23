import steamlit as st
st.title("moqta mini biblioteka")
if "boobks" not in st.session_state:
  st.session_state_books = []


st.header("dobaci kniga")
title = st.text_input("zaglavie")
author = st.text_input("avtor")
price = st.number_input("cena", min_value=0.0)
if st.button("dobavi knigata")

book = {
  "title": title,
  "author": author,
  "price": price
}

st.session_state.books.append(book)
st.success("knigata e dobavena!")

if st.button("pokJI VSICHKI KNIGI"):

if len(st.session_state.books) == 0:
st.write("nqma dobaveni knigi")
else:
for boom in st.session_state.books:
st.write("zaglavie", book["title"])
st.write("avtor", book["author"])
st.write("cena", book["price"])
st.write("------------------")

st.header("tursene na avtor")
search_author = st.text_input("vuvedi ime na avtor")
if st.button("tursi po avtor"):

found = False

for book in st.session_state.books:
  if book["author"] == search_author:
  st.write(book)
  found = True

if found == False:
st.write("nqa namereni knigi ot tozi avtor")



st.header("tursene po zaglavie")
search_title = st.text_input("vuvedi")
if st.button("tursi po zaglavie")
found = True

for book in st.session_state.books:
if book["title"] == search_title:
  st.write(book)
  found = True

if found == False:
  st.write("nqma namerena takava kniga.")

if st.button("pokaji nai evtina kniga")

else:
  cheapest = st.sseassion_state.books[0]

for book in st.session_state.books:
  if book["price"] < cheapest["price"]:
    cheapest = book

st write("nai evtina kn")
st.write(cheapest)



  
