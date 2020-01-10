import random

foodplaces = [
    "shunfu duck rice",
    "herbal soup",
    "sing ming prata",
    "sing ming yong tao fu",
    "palak paneer",
    "toa payoh ba chor mee",
    "toa payoh char siew rice",
    "swensens",
    "bento set",
    "fatburger",
    "Blk 628 market",
    "upper thomson chicken rice",
    "crispy prata house",
    "meng's kitchen",
    "genki sushi",
    "j8 kim san ling"
]

print(f"You should eat at: {foodplaces[random.randint(0, len(foodplaces) - 1)]}")