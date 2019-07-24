from tkinter import *
root=Tk()
from bs4 import BeautifulSoup
import requests
import random
def get_imd_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    movies = soup.find_all("td", class_="titleColumn")
    random.shuffle(movies)
    return movies
def get_imd_summary(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    return soup.find("div", class_="summary_text").contents[0].strip()

def get_imd_movie_info(movie):
    movie_title = movie.a.contents[0]
    movie_year = movie.span.contents[0]
    movie_url = 'http://www.imdb.com' + movie.a['href']
    return movie_title, movie_year, movie_url

def imd_movie_picker():
    ctr=0
    for movie in get_imd_movies('http://www.imdb.com/chart/top'):
        movie_title, movie_year, movie_url = get_imd_movie_info(movie)
        movie_summary = get_imd_summary(movie_url)
        with open("projectfile.txt", "a+") as file:
            file.write(movie_title+" \n")
            file.write(movie_year+"\n")
            file.write(movie_summary+"\n")
            file.write("------------------------- \n")
        ctr=ctr+1
        if (ctr==10):
          break;
def func1():
    if __name__ == '__main__':
        imd_movie_picker()
label0 = Label(root, text="Top Random IMDB Movies", bg="white", fg="black", font=("Times", 40))
label1=Label(root,text="Click the button to see the top movies", bd="2", relief="ridge", bg="white", fg="black", font=("Times", 12),
               width=25)
button1 = Button(root, text="Click Here to Save Data in File.", bg="white", fg="black", width=20, font=("Times", 12), command=func1)
label0.grid(row=0)
label1.grid(row=1,column=0)
button1.grid(row=1,column=1)
root.mainloop()