from owlready2 import *

OWL_PATH = "library.owx"

onto = get_ontology(OWL_PATH).load()

Book = onto.Book
Author = onto.Author
Genre = onto.Genre
AgeGroup = onto.AgeGroup

hasAuthor = onto.hasAuthor
hasGenre = onto.hasGenre
hasAgeGroup = onto.hasAgeGroup  

authors = list(Author.instances())

authors.sort(key=lambda x: (x.label[0] if x.label else x.name))

print("\nВыберите автора:")
for i, a in enumerate(authors, 1):
    print(f"{i}. {a.label[0] if a.label else a.name}")
author_choice = authors[int(input("Введите номер: ")) - 1]


genres = list(Genre.instances())
genres.sort(key=lambda x: (x.label[0] if x.label else x.name))
print("\nВыберите жанр:")
for i, g in enumerate(genres, 1):
    print(f"{i}. {g.label[0] if g.label else g.name}")
genre_choice = genres[int(input("Введите номер: ")) - 1]

ages = list(AgeGroup.instances())
ages.sort(key=lambda x: (x.label[0] if x.label else x.name))

print("\nВыберите возраст:")
for i, ag in enumerate(ages, 1):
    print(f"{i}. {ag.label[0] if ag.label else ag.name}")
age_choice = ages[int(input("Введите номер: ")) - 1]

recommended = []

for b in Book.instances():
    b_authors = getattr(b, hasAuthor.python_name)
    b_genres = getattr(b, hasGenre.python_name)
    b_ages = getattr(b, hasAgeGroup.python_name)

    if (author_choice in b_authors) and (genre_choice in b_genres) and (age_choice in b_ages):
        recommended.append(b)
recommended.sort(key=lambda x: (x.label[0] if x.label else x.name))

print("\nРекомендованные книги:")
if recommended:
    for b in recommended:
        print("-", b.label[0] if b.label else b.name)
else:
    print("Ничего не найдено.")