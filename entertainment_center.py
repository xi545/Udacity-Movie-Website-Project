import media
import fresh_tomatoes

jason_bourne = media.Movie("Jason Bourne",
                           "Jason Bourne goes against the CIA in the fourth installment of the Jason Bourn series.",
                           "https://cinemabravo.files.wordpress.com/2016/02/jasonbourne-poster1.jpg# noqa",
                           "https://www.youtube.com/watch?v=v71ce1Dqqns")

#print(jason_bourne.storyline)
#jason_bourne.show_trailer()

rogue_one = media.Movie("Rogue One",
                        "A cast of all new characters goes against the Empire in this Star Wars sequel.",
                        "http://www.heavymetal.com/v2/wp-content/uploads/2016/01/12391871_1661833287405110_3493089815291090558_n.jpg",
                        "https://www.youtube.com/watch?v=Ze2kpOZx_kU")

#print(rogue_one.storyline)
#rogue_one.show_trailer()

insidious_chapter_four = media.Movie("Insidious Chapter 4",
                                     "Elise returns to fight more supernatural entities.",
                                     "https://i.ytimg.com/vi/vXnNXgi2-Ms/hqdefault.jpg",
                                     "https://www.youtube.com/watch?v=g5vG8wBN95Q")
dont_breathe = media.Movie("Don't Breathe",
                           "Teenagers break into a blind man's home and discover he's dangerous.",
                           "http://cdn.collider.com/wp-content/uploads/2016/03/dont-breathe-poster.jpeg",
                           "https://www.youtube.com/watch?v=76yBTNDB6vU")

split = media.Movie("Split",
                    "Teenage girls are kidnapped by a man with split personality disorder",
                    "https://upload.wikimedia.org/wikipedia/en/3/31/Split_(2017_film).jpg",
                    "https://www.youtube.com/watch?v=aUMQ9jW2qAw")



moana = media.Movie("Moana",
                    "Moana and Maui save the world from an evil lava monster.",
                    "http://www.newdvdreleasedates.com/images/posters/large/moana-2016-01.jpg",
                    "https://www.youtube.com/watch?v=jqmcxLUSRTQ")

allied = media.Movie("Allied",
                     "Intellegence officer Max Vatan goes on a secret mission in North Africa in 1942.",
                     "http://www.star-hdmovies.com/wp-content/uploads/2016/07/Allied-2016-watch-movie-full-free-hd-online-download-torrent.jpg",
                     "https://www.youtube.com/watch?v=22PY59GHQgU")

the_birth_of_a_nation = media.Movie("The Birth of a Nation",
                  "Nat Turner leads a slave rebellion.",
                  "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Birth_of_a_Nation_(2016_film).png",
                  "https://www.youtube.com/watch?v=C4TTbcXG1GQ")

sully = media.Movie("Sully",
                    "This movie is based on the time when a plane landed in the Hudson river",
                    "http://cdn3-www.comingsoon.net/assets/uploads/gallery/sully/cmizrmkukaas8-9.jpg",
                    "https://www.youtube.com/watch?v=mjKEXxO2KNE")

snowden = media.Movie("Snowden",
                      "Edward Snowden steals classified documents from the NSA",
                      "http://www.shockya.com/news/wp-content/uploads/snowden-movie-poster.jpg",
                      "https://www.youtube.com/watch?v=QlSAiI3xMh4")

peculiar_children = media.Movie("Miss Peregrine's Home for Peculiar Children",
                                "This is a fantasy movie.",
                                "http://cdn3-www.comingsoon.net/assets/uploads/gallery/miss-peregrines-home-for-peculiar-children/missperegrinesmall.jpg",
                                "https://www.youtube.com/watch?v=CYPHc8g4QDk")

fantastic_beasts= media.Movie("Fantastic Beasts and Where to Find Them",
                               "This is a Harry Potter spin-off",
                               "http://static.srcdn.com/wp-content/uploads/fantastic-beasts-where-find-them-movie-2016-poster.jpg",
                               "https://www.youtube.com/watch?v=_XIEnFpySnk")



# This is the list of movies that fresh_tomatoes uses
movies = [jason_bourne, rogue_one, insidious_chapter_four, dont_breathe, split, moana, allied, the_birth_of_a_nation, sully, snowden, peculiar_children, fantastic_beasts]
fresh_tomatoes.open_movies_page(movies)
    
