# класс Название, будет базовым для классов Product и Pizza
# он будет служить для проверки заполненности атрибута title в дочерних классах
class Title():
    # создаем конструктор класса
    def __init__(self, title):
        # проверяем заполненность title  с помощью статического метода check_title
        # если реквизит заполнен, то устанавливаем артибут, иначе выводим ValueError
        if Title.check_title(title):
            self.title = title
        else:
            raise ValueError
    # создаем статический метод, в котором будет осуществляться проверка заполненности артибута title
    @staticmethod
    def check_title(title):
        # если title существует (заполнен), возвращаем True
        if title:
            return True
        else:
            return False

# класс описание Продукта, в качестве базового класса ему передается класс Title
class Product(Title):
    # создаем конструктор класса и устанавливаем атрибуты:
    # title - название, calorific - калорийность, cost - цена
    def __init__(self, title, calorific, cost):
        # вызываем конструктор базового класса Title
        super().__init__(title)
        # устанавливаем атрибуты
        self.calorific = calorific
        self.cost = cost

# класс описание Ингредиента
class Ingredient():
    # создаем конструктор класса и устанавливаем атрибуты
    def __init__(self, product, weight):
        # делаем проверку с помощью статического метода check_weight
        # если проверка выполнятеся, то устанавливаем атрибуты, иначе выводим ValueError
        if self.check_weight(weight):
            self.product = product
            self.weight = weight
        else:
            raise ValueError
    
    # создаем статический метод для проверки, что weight положительное число
    # метод вернет weight если его значение > 0
    @staticmethod
    def check_weight(weight):
        return weight > 0

    # создаем метод для получения калорийности ингредиента
    # так как мы для получения ингредиентов передаем в атрибут product, экземпляр класса Product
    # то мы можем обращаться к атрибутам класса Product, через реквизит self.product
    def get_calorific(self):
        return (self.weight/100) * self.product.calorific

    # создаем метод для расчета себестоимости ингредиента, по формуле: вес_ингредиента / 100 * себестоимость_продукта
    def cost_price(self):
        return (self.weight/100) * self.product.cost

# класс Пицца, в качестве базового класса ему передается класс Title
class Pizza(Title):
    # создаем конструктор класса и устанавливаем атрибуты:
    # title - название, ingredients - ингредиенты. Список значений класса Ingredient.
    def __init__(self, title, ingredients):
        # вызываем конструктор базового класса Title
        super().__init__(title)
        self.ingredients = ingredients

    # переопределим метод __str__ чтобы вывести через принт значения атрибутов класса
    def __str__(self):
        return self.title

    # создадим метод для получения общей калорийности пиццы
    def calorific(self):
        sum_calorific = 0   # переменная для хранения суммы калорийности
        # пробегаем циклом по списку всех ингредиентов пиццы, и находим для каждого калорийность
        # после чего добавляем найденное значение в переменную sum_calorific
        for ingredient in self.ingredients:
            # так как мы передаем в атрибут ingredients - ингредиенты - представляющие собой экземпляр класса Ingredient
            # мы можем напрямую вызывать его методы обращаясь к self.ingredients
            sum_calorific += ingredient.get_calorific()
        return sum_calorific

    # создадим метод для получения общей себестоимости пиццы
    def cost_price(self):
        sum_cost_price = 0   # переменная для хранения суммы себестоимости всех ингредиентов
        # пробегаем циклом по списку всех ингредиентов пиццы, и находим для каждого себестоимость
        # после чего добавляем найденное значение в переменную sum_cost_price
        for ingredient in self.ingredients:
            # так как мы передаем в атрибут ingredients - ингредиенты - представляющие собой экземпляр класса Ingredient
            # мы можем напрямую вызывать его методы обращаясь к self.ingredients
            sum_cost_price += ingredient.cost_price()
        return sum_cost_price

# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Из продуктов создаем ингредиенты. Для каждого ингредиента указываем продукт, 
# из которого он состоит и вес продукта
dough_ingredient = Ingredient(dough_product, 100)
tomato_ingredient = Ingredient(tomato_product, 100)
cheese_ingredient = Ingredient(cheese_product, 100)

# Из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient])

# Выводим экземпляр пиццы
print(f'{pizza_margarita} ({pizza_margarita.calorific()} kkal) - {pizza_margarita.cost_price()} руб')
