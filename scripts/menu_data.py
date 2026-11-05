import json
from pathlib import Path
menus=[]
def group(category,title,rows,note=''):
 items=[]
 for line in rows.strip().split('\n'):
  name,price,description=line.split('|');items.append(dict(name=name,price=price,description=description))
 menus.append(dict(category=category,title=title,note=note,items=items))
group('seasonal',"Chef Pablo’s seasonal selections",'''Ensalada de Tomate|14.95|Organic heirloom tomatoes, basil vinaigrette, goat cheese, dry black olives.
Ensalada Sandía|14.95|Fresh watermelon, goat cheese, pomegranate vinaigrette.
Palta Rellena|12.95|Stuffed avocados with bay shrimp and gravlax, honey citrus surprise.
Colas de Bruselas|10.00|Brussels sprouts, onions, balsamic reduction and toasted almonds.
Espárrago en Romesco|12.95|Organic grilled asparagus, roasted red bells, garlic, toasted almonds.
Croquetas al Gusto|12.95|Creamy fried fritters of béchamel with a choice of chorizo, mushroom or serrano ham.
Pinchitos Exquisitos · Lamb|12.95|Marinated and seared lamb brochette with paprika, mint and caraway.
Pinchitos Exquisitos · Shrimp|12.95|Marinated and seared shrimp brochette with bread croutons, mint and ginger.
Cazuelita de Marisco|21.95|Seafood medley, shrimp, scallops and cuttlefish, white beans, tomato and saffron fumet.
Risotto Piemontese|49.95|Creamy risotto with taleggio, grana padano and gorgonzola dolcelatte; seasonal mushrooms. Served for two.
Reda’s Pepper Steak|49.95|16 oz prime New York steak, red wine, demi and peppercorns, potato onion casserole.
Panna Cotta|10.95|Silky gelatin classic with sweetened cream and raspberry coulis.''','Fall 2026')
group('lunch','Sopas y ensaladas','''Sopa del Día|Ask us|Soup of the day, seasonal fruits.
Ensalada de Elsy|12.95|Arugula, celery, radicchio, cucumber, onion, black olives, citrus vinaigrette.
Ensalada con Pollo|17.90|Chicken, spinach, green beans, carrots, beets, potatoes, eggs, olives, house vinaigrette: EVOO, Dijon, sherry vinegar, onions, anchovies.''')
group('lunch','Bocadillos con pan coca','''Bocadillo del Día|Ask us|Chef’s special bocadillo of the day, served with a rotating side.''','On a grilled flatbread from Mallorca.')
group('lunch','Tapas frías','''Tortilla Tres Colores|6.95|Spanish torte with egg, onion, potato, bell pepper and aioli.
Tartar|Ask us|Fish of the day, EVOO, red onions, capers, a touch of garlic, served with pan tostado and arugula.
Charcuterie y Queso Manchego|14.95|Pamplona and Soria chorizos, jamón serrano, cave-aged manchego and house-cured olives.
Pa amb Tomaquet|6.95|Catalan bruschetta with EVOO and tomato. With cured jamón serrano: 12.95.''')
group('lunch','Tapas calientes','''Mejillones Aioli|21.95|Mediterranean mussels, garlic, sherry, cream.
Pulpo a la Gallega|16.95|Octopus in an adobo marinade, scalloped potatoes with pimentón.
Gambas Ajillo|14.95|Shrimp, garlic and white wine sauce.
Gambas a la Parrilla|14.95|Grilled shrimp in a citrus and cumin avocado salsa fresca.
Salmón Alcaparado|12.95|Salmon, white wine, garlic, capers, citrus, mustard.
Portobello de la Moda|12.95|Portobello mushroom marinated in red wine vinegar, then grilled, topped with goat cheese and EVOO.
Patatas Bravas|8.95|Roasted potatoes in a spicy tomato sauce with garlic aioli.
Pinchos Morunos|12.50|Grilled leg of lamb skewers in a red wine bell pepper sauce.
Chorizo al Ajoarriero|12.95|Grilled chorizo, white beans, Swiss chard.''')
group('lunch','Pastas','''Ravioles Caseros|21.95|Housemade ravioli stuffed with herbs and fontina cheese, in a shiitake mushroom sauce.
Pasta Amatriciana|20.95|Bucatini in a pancetta tomato sauce, grana padano and bread crumbs.
Linguine al Limone|21.95|Linguine pasta in a citrus herb butter sauce.''')
group('lunch','Las raciones','''Zarzuela de Mariscos|32.95|Opera of seafood in a lightly tomato broth; pan tostado.
Paillard de Pollo|22.95|Grilled pounded chicken breast marinated in citrus, served with patatas bravas.
Parrillada Mixta|34.95|Grilled chorizo, chicken, two lamb chops, pisto manchego. Two additional chops: 17.95.
Bisteca Costeña|49.95|Prime rib-eye finished in a red wine reduction, blue cheese.''')
group('lunch','Las paellas','''Paella Barcelonetta|60.00|Squid ink rice, heads-on shrimp, bay scallops, cuttlefish sofrito.
Paella Valenciana|49.95|Saffron rice, shrimp, mussels, calamari, chicken thighs, pork spareribs.
Paella de Hongos|28.95|Saffron rice, shiitake and button mushrooms, grated grana padano.
Paella Vegetariana|26.95|Saffron rice and seasonal vegetables.''','Made to share, for two people. Please allow 45 minutes to prepare.')
group('lunch','Menu del almuerzo','''Lunch set|24.00|Starts with soup and ends with dessert. Choose a main course: fish, pasta or stew.''')
group('dessert','Postres','''Crema Catalana con Naranja|8.00|Classic orange flower crème brûlée.
Pastel Almendras|8.00|Almond cake with honey and orange flower water.
Delicia de Frambuesa|10.95|Chocolate raspberry cake with fresh raspberries.
Chocolate con Acento Francés|8.00|Chocolate mousse and berries.
Arroz con Leche|9.00|Rice pudding with vanilla, finished with caramelized sugar.
Pastel de Chocolate|8.00|Flourless chocolate lava cake, crème anglaise with mint.
Panna Cotta|10.95|Silky gelatin classic with sweetened cream and raspberry coulis.
Flan|8.00|Crème caramel.
Marscapone Limon Mousse|12.00|A dash of limoncello topped with a fresh iced amaretti.''')
group('dessert','Café','''Coffee|4.00|
Espresso|4.00|
Cappuccino|6.00|
Latte|6.00|
Mocha|6.00|
Tea|4.00|''')
group('drinks','Cócteles','''Honey Badger|14.00|Vodka, lemon, honey, St-Germain, lavender bitters, up, lemon zest.
Chambery Martini|16.00|Vodka, chamberyzette, up, lemon expression.
Self Care|17.00|Gin, strawberry-balsamic shrub, lemon, honey, saline, up, lemon zest.
Beetroot Sour|17.00|Gin, beet basil syrup, egg white, lemon, honey, up, fresh basil leaf.
Rosé Negroni|17.00|Botanical gin, Bonanto aperitivo, rosé vermouth, over, grapefruit zest.
Sailor’s Delight|17.00|Oleo rum, Plantation pineapple rum, Bonanto, lemon, Banane du Brésil, brown sugar, Angostura bitters, over, maraschino cherry.
Puertas al Infierno|16.00|Jalapeño-infused tequila, lemon, pineapple, jalapeño agave lime syrup, over, cucumber and Aleppo pepper.
La Sombra Negra|17.00|Tequila, mezcal, lime, peach liqueur, squid-ink syrup, firewater bitters, over, black salt rim, lime wheel.
Smoke It Up|15.00|Mezcal, tequila, lime, honey, crème de violette, salt, pinot noir float, over, lime zest.
Bamboo & Tonic|14.00|Dry sherry, dry vermouth, tonic, over, Manzanilla olive.
White Coco|18.00|Bourbon, dark rum, lime, cherry black vanilla bitters, coconut cream, over, dried tea leaves, sesame seeds.''','Explore the full wine, beer, spirits and after-dinner selection in the original menus below.')
Path(__file__).resolve().parents[1].joinpath('data/menu.json').write_text(json.dumps(menus,ensure_ascii=False,indent=2))
print(sum(len(g['items']) for g in menus),'readable menu entries')
