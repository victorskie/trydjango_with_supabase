from .utils import number_str_to_float, parse_paragraph_to_recipe_line, convert_to_qty_units

# This is a fake response simulating what the OCR API would return
extracted = {"results": ["1 pound chicken breasts cut into bite", "size pieces", "", "2 tbsp olive oil", "", "2 clove garlic crushed or minced", "", "1 tbsp chili powder", "", "1/2 teaspoon ground cumin", "", "1/4 teaspoon onion or garlic powder", "1/4 teaspoon kosher salt", "", "1 tbsp olive oil", "", "squeeze of lime optional", "\f"], "original": "1 pound chicken breasts cut into bite\nsize pieces\n\n2 tbsp olive oil\n\n2 clove garlic crushed or minced\n\n1 tbsp chili powder\n\n1/2 teaspoon ground cumin\n\n1/4 teaspoon onion or garlic powder\n1/4 teaspoon kosher salt\n\n1 tbsp olive oil\n\nsqueeze of lime optional\n\f"}

og = extracted['original']

results = parse_paragraph_to_recipe_line(og)
dataset = convert_to_qty_units(results)

print(dataset)