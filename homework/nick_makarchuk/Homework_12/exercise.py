class Flower:
    def __init__(self, name, color, stem_length, price, freshness, lifespan_days):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.freshness = freshness
        self.lifespan_days = lifespan_days

    def __repr__(self):
        return f"{self.name}({self.color}, {self.stem_length}см, {self.price}₽, свежесть: {self.freshness})"


class Rose(Flower):
    def __init__(self, color, stem_length, price, freshness):
        super().__init__("Роза", color, stem_length, price, freshness, lifespan_days=7)


class Tulip(Flower):
    def __init__(self, color, stem_length, price, freshness):
        super().__init__("Тюльпан", color, stem_length, price, freshness, lifespan_days=5)


class Chamomile(Flower):
    def __init__(self, color, stem_length, price, freshness):
        super().__init__("Ромашка", color, stem_length, price, freshness, lifespan_days=4)


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def total_price(self):
        total = 0
        for flower in self.flowers:
            total += flower.price
        return total

    def average_lifespan(self):
        if not self.flowers:
            return 0
        total_days = 0
        for flower in self.flowers:
            total_days += flower.lifespan_days
        return total_days / len(self.flowers)

    def sort_by(self, attribute):
        self.flowers.sort(key=lambda flower: getattr(flower, attribute))

    def find_by_lifespan(self, min_days, max_days):
        result = []
        for flower in self.flowers:
            if min_days <= flower.lifespan_days <= max_days:
                result.append(flower)
        return result

    def __repr__(self):
        return f"Букет из {len(self.flowers)} цветов: {self.flowers}"


flowers = [
    Rose("красный", 40, 150, 9),
    Tulip("жёлтый", 35, 100, 8),
    Chamomile("белый", 30, 50, 7),
    Rose("белый", 45, 160, 10),
    Tulip("розовый", 33, 90, 6)
]

bouquet = Bouquet(flowers)
print(bouquet)
print("Общая стоимость букета:", bouquet.total_price(), "₽")
print("Среднее время увядания:", bouquet.average_lifespan(), "дней")

bouquet.sort_by("freshness")
print("\nОтсортировано по свежести:")
print(bouquet)

found = bouquet.find_by_lifespan(5, 7)
print("\nЦветы с продолжительностью жизни от 5 до 7 дней:")
print(found)
