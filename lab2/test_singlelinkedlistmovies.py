import pytest 
import config 
from DataStructures import singlelinkedlist as slt
from ADT import list as lt
import csv


def cmpfunction (element1, element2):
    if element1 == element2:
        return 0

@pytest.fixture
def lst ():
    lst = slt.newList(cmpfunction)
    return lst


@pytest.fixture
def movies (sep=";"):
    movies = lt.newList()
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open("Data/MoviesCastingRaw-small.csv", encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(movies,row)
    except:
        print("Hubo un error con la carga del archivo")
    return movies


@pytest.fixture
def lstmovies(movies):
    lst = slt.newList(cmpfunction)
    for i in range(1,(movies['size']+1)):
        mov=lt.getElement(movies,i)    
        slt.addLast(lst,mov)    
    return lst



def test_empty (lst):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0




def test_addFirst (lst, movies):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addFirst (lst, lt.getElement(movies,2))
    assert slt.size(lst) == 1
    slt.addFirst (lst, lt.getElement(movies,3))
    assert slt.size(lst) == 2
    movie = slt.firstElement(lst)
    assert movie == lt.getElement(movies,3) 




def test_addLast (lst, movies):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addLast (lst, lt.getElement(movies,2))
    assert slt.size(lst) == 1
    slt.addLast (lst, lt.getElement(movies,3))
    assert slt.size(lst) == 2
    movie = slt.firstElement(lst)
    assert movie == lt.getElement(movies,2) 
    movie = slt.lastElement(lst)
    assert movie == lt.getElement(movies,3) 




def test_getElement(lstmovies, movies):
    movie = slt.getElement(lstmovies, 1)
    assert movie == lt.getElement(movies,1) 
    movie = slt.getElement(lstmovies, 5)
    assert movie == lt.getElement(movies,5) 





def test_removeFirst (lstmovies, movies):
    assert slt.size(lstmovies) == 2000
    slt.removeFirst(lstmovies)
    assert slt.size(lstmovies) == 1999
    movie = slt.getElement(lstmovies, 1)
    assert movie  == lt.getElement(movies,2) 



def test_removeLast (lstmovies, movies):
    assert slt.size(lstmovies) == 2000
    slt.removeLast(lstmovies)
    assert slt.size(lstmovies) == 1999
    movie = slt.getElement(lstmovies, 4)
    assert movie  == lt.getElement(movies,4) 



def test_insertElement (lst, movies):
    assert slt.isEmpty(lst) is True
    assert slt.size(lst) == 0
    slt.insertElement (lst, lt.getElement(movies,1), 1)
    assert slt.size(lst) == 1
    slt.insertElement (lst, lt.getElement(movies,2), 2)
    assert slt.size(lst) == 2
    slt.insertElement (lst, lt.getElement(movies,3), 1)
    assert slt.size(lst) == 3
    movie = slt.getElement(lst, 1)
    assert movie == lt.getElement(movies,3) 
    movie = slt.getElement(lst, 2)
    assert movie == lt.getElement(movies,1) 



def test_isPresent (lstmovies, movies):
    movie = ([('id', '4000'), ('actor1_name', 'Turo Pajala'), ('actor1_gender', '0'), ('actor2_name', 'Susanna Haavisto'), ('actor2_gender', '0'), ('actor3_name', 'Matti Pellonpää'), ('actor3_gender', '2'), ('actor4_name', 'Eetu Hilkamo'), ('actor4_gender', '0'), ('actor5_name', 'none'), ('actor5_gender', '0'), ('actor_number', '4'), ('director_name', 'Aki Kaurismäki'), ('director_gender', '0'), ('director_number', '1'), ('producer_name', 'none'), ('producer_number', '0'), ('screeplay_name', 'Aki Kaurismäki'), ('editor_name', 'Raija Talvio')])
    movie3=lt.getElement(movies, 3)
    print(slt.isPresent (lstmovies,movie3))
    assert slt.isPresent (lstmovies, movie3) > 0
    assert slt.isPresent (lstmovies, movie) == 0
    


def test_deleteElement (lstmovies, movies):
    pos = slt.isPresent (lstmovies, lt.getElement(movies,3))
    assert pos > 0
    movie = slt.getElement(lstmovies, pos)
    assert movie == lt.getElement(movies,3)
    slt.deleteElement (lstmovies, pos)
    assert slt.size(lstmovies) == 1999
    movie = slt.getElement(lstmovies, pos)
    assert movie == lt.getElement(movies,4)


def test_changeInfo (lstmovies):
    movie10 = ([('id', '2'), ('actor1_name', 'Turo Pajala'), ('actor1_gender', '0'), ('actor2_name', 'Susanna Haavisto'), ('actor2_gender', '0'), ('actor3_name', 'Matti Pellonpää'), ('actor3_gender', '2'), ('actor4_name', 'Eetu Hilkamo'), ('actor4_gender', '0'), ('actor5_name', 'none'), ('actor5_gender', '0'), ('actor_number', '4'), ('director_name', 'Aki Kaurismäki'), ('director_gender', '0'), ('director_number', '1'), ('producer_name', 'none'), ('producer_number', '0'), ('screeplay_name', 'Aki Kaurismäki'), ('editor_name', 'Raija Talvio')])
    slt.changeInfo (lstmovies, 1, movie10)
    movie = slt.getElement(lstmovies, 1)
    assert movie10 == movie


def test_exchange (lstmovies, movies):
    movie1 = slt.getElement(lstmovies, 1)
    movie5 = slt.getElement(lstmovies, 5)
    slt.exchange (lstmovies, 1, 5)
    assert slt.getElement(lstmovies, 1) == movie5
    assert slt.getElement(lstmovies, 5) == movie1