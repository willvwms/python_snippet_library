from box import Box

movie_data = {
  "movies": {
    "Spaceballs": {
      "imdb_stars": 7.1,
      "rating": "PG",
      "length": 96,
      "Director": "Mel Brooks",
      "Stars": [{"name": "Mel Brooks", "imdb": "nm0000316", "role": "President Skroob"},
                {"name": "John Candy","imdb": "nm0001006", "role": "Barf"},
                {"name": "Rick Moranis", "imdb": "nm0001548", "role": "Dark Helmet"}
      ]
    },
    "Robin Hood: Men in Tights": {
      "imdb_stars": 6.7,
      "rating": "PG-13",
      "length": 104,
      "Director": "Mel Brooks",
      "Stars": [
                {"name": "Cary Elwes", "imdb": "nm0000144", "role": "Robin Hood"},
                {"name": "Richard Lewis", "imdb": "nm0507659", "role": "Prince John"},
                {"name": "Roger Rees", "imdb": "nm0715953", "role": "Sheriff of Rottingham"},
                {"name": "Amy Yasbeck", "imdb": "nm0001865", "role": "Marian"}
      ]
    }
  }
}


my_box = Box(movie_data)

my_box.movies.Spaceballs.rating
'PG'

my_box.movies.Spaceballs.Stars[0].name
'Mel Brooks'

my_box.movies.Spaceballs.Stars[0]
# <Box: {'name': 'Mel Brooks', 'imdb': 'nm0000316', 'role': 'President Skroob'}>
