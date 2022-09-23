movies = []


def menu():
    n = input(Menu)
    while n != 'd':
        if n == 'a':
            add_movie()
        elif n == 'b':
            show_movie()
        elif n == 'c':
            search_movie()
        n = input("Menu")


def add_movie():
    m_name = input("Enter the name of the movie:")
    m_director = input("Enter the name of the director:")
    m_year = int(input("Enter the release date"))

    d = {
        "name": m_name,
        "director": m_director,
        "year": m_year
    }
    movies.append(d)


def show(h):
    print(f"Name:{h['name']}")
    print(f"Director:{h['director']}")
    print(f"Year:{h['year']}")


def show_movie():
    for i in movies:
        show(i)


def search( n, m):
    f=[]
    for i in movies: // """ if i[n] == m: f.append(i)"""
        x=i.get(n)

        if x == m:
            f.append(i)

    print(f)


def search_movie():
    n = input("Enter the feature by which the search to be performed: ")
    m = input("What need to be searched:")
    search( n, m)


Menu = "\n Enter which operation has to be performed: \n 1. Add movies - a \n 2.Show movies -b \n 3. Search movies - c \n 4.Quit - d \n"
menu()
