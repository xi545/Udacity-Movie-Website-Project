import webbrowser

class Movie():
    """ This class provides a way to store movie related information"""
    
    valid_ratings = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        print("Movie Constructor Called")
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_info(self):
        print("Movie Title - "+self.title)
        print("Storyline - "+self.storyline)
        print("Poster Image URL - "+self.poster_image_url)
        print("Trailer - "+self.trailer_youtube_url)
        
 
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
