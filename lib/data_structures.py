spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [key["name"] for key in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    return [item for item in spicy_foods if item["heat_level"] > 5]
    pass

def print_spicy_foods(spicy_foods):

    for item in spicy_foods:
            heat = "🌶" * item["heat_level"]
            print(f"{item['name']} ({item['cuisine']}) | Heat Level: {heat}")

    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    match = [item for item in spicy_foods if item["cuisine"] == cuisine]
    if match:
        return match[0]
    else:
        return None


def print_spiciest_foods(spicy_foods):
    spicy_dict = [item for item in spicy_foods if item["heat_level"] > 5]
    for item in spicy_dict:
        heat = '🌶'*item["heat_level"]
        print(f"{item['name']} ({item['cuisine']}) | Heat Level: {heat}")
   
def get_average_heat_level(spicy_foods):
    heat_levels = [food["heat_level"] for food in spicy_foods]
    return (sum(heat_levels,0) / len(heat_levels))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
