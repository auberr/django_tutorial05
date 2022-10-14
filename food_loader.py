import json

genre_list = ["중식", "일식", "한식", "미국", "지중해", "중남미", "프랑스", "이태리", "동남아", "중동", "아프리카"]

with open('food.json', 'rt', encoding='UTF-8') as f:
    foods = json.load(f)

new_list = []
for food in foods:
    new_data = {"model": "foods.food"}
    if food["genre"]:
        genres = eval(food["genre"])
        genre_int_list = []
        for genre in genres:
            genre_int = genre_list.index(genre) + 1
            genre_int_list.append(genre_int)
        food['genre'] = genre_int_list
    
    else:
        food["genre"] = []
    new_data["fields"] = food
    new_list.append(new_data)

with open('foods_data.json', 'w', encoding='UTF-8') as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)