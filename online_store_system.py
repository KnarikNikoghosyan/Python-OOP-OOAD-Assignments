class Product:
    def __init__(self, product_id, product_name, price, inventory_count):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.inventory_count = inventory_count

    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)
        print(f"New price: {self.price}")

    def sell(self, quantity):
        self.inventory_count -= quantity
        print(f"Modified inventory count: {self.inventory_count}")


class DynamicPricing:
    def adjust_price(self, product: Product, demand: str):
        if demand == "high":
            product.price += 5000
            print(f"Increased price: {product.price}")
        elif demand == "low" and product.inventory_count < 20:
            product.price -= 5000
            print(f"Decreased price: {product.price}")


product1 = Product("5497532", "Laptop", 100000, 40)
product1.apply_discount(15)
product1.sell(25)

product2 = Product("5315241", "Television", 150000, 50)
product2.apply_discount(5)
product2.sell(10)

dynamicpricing = DynamicPricing()

dynamicpricing.adjust_price(product1, "high")
dynamicpricing.adjust_price(product2, "low")

# Allowing direct manipulation of product prices and inventory counts can lead to problems like incorrect data, security risks, and difficulties in maintaining the system.
# When methods like sell(quantity) and apply_discount(discount_percentage) don't check if the inputs are right you might end up with wrong numbers for how much stuff you have or how much things cost.
# And people could use the system the wrong way on purpose or by accident, messing up the data.
# The current system design may lead to errors, such as increasing inventory when items are sold(like negative quantities or discounts over 100%), making unplanned price adjustments, or failing to maintain consistent pricing.