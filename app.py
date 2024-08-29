from Converter import lbs_to_kg, kg_to_lbs
from find_max import find_max
from ecommerce.shipping import calc_shipping
import random


numbers = [100, 22, 3, 20, 10, 1, 2, 3, 4,]

print(find_max(numbers))


print(lbs_to_kg(70))
print(kg_to_lbs(70))
calc_shipping()