import requests, os, json

API_KEY = os.getenv('int', '6163fbe091536a27c8951c10ecb40d6c')

total_data = []

idx = 1
for num in range(1, 4):
    movie_url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page={num}'
    movie_get = requests.get(movie_url)
    movies = movie_get.json().get('results')


    for movie in movies:
        if movie.get('release_date', ''):
            fields = {
                'movie_id': movie['id'],
                'title': movie['title'],
                'released_date': movie['release_date'],
                'popularity': movie['popularity'],
                'vote_avg': movie['vote_average'],
                'overview': movie['overview'],
                'poster_path': movie['poster_path'],
                'genres': movie['genre_ids']
            }
            data = {
                "pk": idx,
                "model": "movies.movie",
                "fields": fields
            }

            total_data.append(data)
            idx += 1
            
        genres_json = open('fixtures/genres.json', encoding='UTF8')
        genres_list = json.load(genres_json)

        for i in range(len(movie['genre_ids'])):
            for j in range(len(genres_list)):
                if movie['genre_ids'][i] == genres_list[j]['id']:
                    movie['genre_ids'][i] = genres_list[j]['name']

with open("movie_data.json", "w", encoding="utf-8") as w:
    json.dump(total_data, w, indent="\t", ensure_ascii=False)
