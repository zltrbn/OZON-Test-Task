from src.client import get_heros
from src.utils.hero_height import height_to_feet

def get_tallest_hero(gender: str, has_work: bool):
    heros = get_heros()

    tallest_hero = []
    tallest_height = None
    for hero in heros:
        if hero["work"]["occupation"] in ("", "-"):
            hero_has_work = False
        else:
            hero_has_work = True

        if hero["appearance"]["gender"] != gender or hero_has_work != has_work:
            continue

        height = height_to_feet(hero["appearance"]["height"])

        if height is None:
            continue

        if tallest_height is None or height > tallest_height:
            tallest_hero.clear()
            tallest_hero.append(hero)
            tallest_height = height

        elif height == tallest_height:
            tallest_hero.append(hero)

    if tallest_hero == []:
        return None
    return tallest_hero