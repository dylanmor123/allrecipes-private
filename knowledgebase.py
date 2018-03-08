import json
import re

# This is a data structure with representing our knowledge base.
# NOTE: If you are adding new entries try to make the field name
#   self explanatory.
KNOWLEDGE_BASE = {}

# Set this to true if you are adding new data to the KB and want to
# run tests.
TESTING_KNOWLEDGE_BASE = False

# Adds information to the knowledge base (KB)
# Args - 
#   tuple: list of string 
#   kb_subtree (optional): a defaultdict that represents a KB tree  
def addToKB(tuple, kb_subtree = KNOWLEDGE_BASE):
    current_entry = kb_subtree
    for i in range(len(tuple)):
        if not tuple[i] in current_entry:
            current_entry[tuple[i]] = {}
        current_entry = current_entry[tuple[i]]

# Verifies if tuple is in knowledge base (KB)
# Args - 
#   tuple: list of string
#   kb_subtree (optional): a defaultdict that represents a KB tree
#   regex (optional): boolean value, if true will match the keys in the
#       dictionary using regex.
# Returns -
#   True if tuple is part of the KB.
def isInKB(tuple, kb_subtree = KNOWLEDGE_BASE, regex = False):
    return getKBSubtree(tuple, kb_subtree, regex) is not None

# Gets a subtree of the knowledge base associated with the tuple.
# E.g. running getKBSubtree(["ingredients"]]) will return a defaultdict
# where the list of keys are ingredients.
# Args - 
#   tuple: list of string
#   kb_subtree (optional): a defaultdict that represents a KB tree
#   regex (optional): boolean value, if true will match the keys in the
#       dictionary using regex. If more than one key matches the regex,
#       will return the first match.   
# Returns -
#   A dict that is a subtree of the KB or None if not present.
def getKBSubtree(tuple, kb_subtree = KNOWLEDGE_BASE, regex=False):
    current_entry = kb_subtree
    for i in range(len(tuple)):
        if regex:
            matched_any_key = False
            for key in current_entry.keys():
                if re.match(tuple[i], key) is not None:
                    # TODO(danilo): we should consider returning all the subtrees
                    # from here, or getting the most likely matching key.
                    current_entry = current_entry[key]
                    matched_any_key = True
                    break
            if not matched_any_key:
                return None
        else:
            if not tuple[i] in current_entry:
                return None
            current_entry = current_entry[tuple[i]]
    return current_entry

# Adds information to the knowledge base (KB)
# Args - 
#   knowledge_subtre (optional): a defaultdict that represents a KB tree
def prettyPrintKBsubtree(kb_subtree = KNOWLEDGE_BASE):
    print(json.dumps(kb_subtree, sort_keys=True, indent=4))

####################################################################
### List of Ingredients
        
addToKB(["ingredients", "bok choy", "category", "vegetables"])
addToKB(["ingredients", "snake beans", "category", "vegetables"])
addToKB(["ingredients", "sorrel leaves", "category", "vegetables"])
addToKB(["ingredients", "rocket leaves", "category", "vegetables"])
addToKB(["ingredients", "drumstick", "category", "vegetables"])
addToKB(["ingredients", "cherry tomatoes", "category", "vegetables"])
addToKB(["ingredients", "kaffir lime", "category", "vegetables"])
addToKB(["ingredients", "plantain", "category", "vegetables"])
addToKB(["ingredients", "turnip", "category", "vegetables"])
addToKB(["ingredients", "sweet potatoes", "category", "vegetables"])
addToKB(["ingredients", "round gourd", "category", "vegetables"])
addToKB(["ingredients", "ridge gourd", "category", "vegetables"])
addToKB(["ingredients", "pimiento", "category", "vegetables"])
addToKB(["ingredients", "spinach", "category", "vegetables"])
addToKB(["ingredients", "onion", "category", "vegetables"])
addToKB(["ingredients", "mustard leaves", "category", "vegetables"])
addToKB(["ingredients", "mushroom", "category", "vegetables"])
addToKB(["ingredients", "radish", "category", "vegetables"])
addToKB(["ingredients", "shallots", "category", "vegetables"])
addToKB(["ingredients", "lettuce", "category", "vegetables"])
addToKB(["ingredients", "leek", "category", "vegetables"])
addToKB(["ingredients", "pumpkin", "category", "vegetables"])
addToKB(["ingredients", "yam", "category", "vegetables"])
addToKB(["ingredients", "jalapeno", "category", "vegetables"])
addToKB(["ingredients", "jackfruit", "category", "vegetables"])
addToKB(["ingredients", "horseradish", "category", "vegetables"])
addToKB(["ingredients", "spring onion", "category", "vegetables"])
addToKB(["ingredients", "green peas", "category", "vegetables"])
addToKB(["ingredients", "green chillies", "category", "vegetables"])
addToKB(["ingredients", "cluster beans", "category", "vegetables"])
addToKB(["ingredients", "gherkins", "category", "vegetables"])
addToKB(["ingredients", "garlic", "category", "vegetables"])
addToKB(["ingredients", "french beans", "category", "vegetables"])
addToKB(["ingredients", "fenugreek", "category", "vegetables"])
addToKB(["ingredients", "cucumber", "category", "vegetables"])
addToKB(["ingredients", "zucchini", "category", "vegetables"])
addToKB(["ingredients", "corn", "category", "vegetables"])
addToKB(["ingredients", "shiitake mushroom", "category", "vegetables"])
addToKB(["ingredients", "celery", "category", "vegetables"])
addToKB(["ingredients", "cauliflower", "category", "vegetables"])
addToKB(["ingredients", "carrot", "category", "vegetables"])
addToKB(["ingredients", "capsicum", "category", "vegetables"])
addToKB(["ingredients", "capers", "category", "vegetables"])
addToKB(["ingredients", "broccoli", "category", "vegetables"])
addToKB(["ingredients", "broad beans", "category", "vegetables"])
addToKB(["ingredients", "bottle gourd", "category", "vegetables"])
addToKB(["ingredients", "bitter gourd", "category", "vegetables"])
addToKB(["ingredients", "lady finger", "category", "vegetables"])
addToKB(["ingredients", "lotus stem", "category", "vegetables"])
addToKB(["ingredients", "bell pepper", "category", "vegetables"])
addToKB(["ingredients", "beetroot", "category", "vegetables"])
addToKB(["ingredients", "pigweed", "category", "vegetables"])
addToKB(["ingredients", "cabbage", "category", "vegetables"])
addToKB(["ingredients", "bamboo shoot", "category", "vegetables"])
addToKB(["ingredients", "baby corn", "category", "vegetables"])
addToKB(["ingredients", "avocado", "category", "vegetables"])
addToKB(["ingredients", "eggplant", "category", "vegetables"])
addToKB(["ingredients", "asparagus", "category", "vegetables"])
addToKB(["ingredients", "ash gourd", "category", "vegetables"])
addToKB(["ingredients", "artichoke", "category", "vegetables"])
addToKB(["ingredients", "colocasia", "category", "vegetables"])
addToKB(["ingredients", "potatoes", "category", "vegetables"])
addToKB(["ingredients", "ginger", "category", "vegetables"])

addToKB(["ingredients", "coriander powder", "category", "spicies"])
addToKB(["ingredients", "chives", "category", "spicies"])
addToKB(["ingredients", "galangal", "category", "spicies"])
addToKB(["ingredients", "tulsi", "category", "spicies"])
addToKB(["ingredients", "sage", "category", "spicies"])
addToKB(["ingredients", "rosemary", "category", "spicies"])
addToKB(["ingredients", "yellow chillies", "category", "spicies"])
addToKB(["ingredients", "oregano", "category", "spicies"])
addToKB(["ingredients", "nasturtium", "category", "spicies"])
addToKB(["ingredients", "salt", "category", "spicies"])
addToKB(["ingredients", "mustard powder", "category", "spicies"])
addToKB(["ingredients", "paprika", "category", "spicies"])
addToKB(["ingredients", "mint leaves", "category", "spicies"])
addToKB(["ingredients", "marjoram", "category", "spicies"])
addToKB(["ingredients", "lemongrass", "category", "spicies"])
addToKB(["ingredients", "red chilli", "category", "spicies"])
addToKB(["ingredients", "saffron", "category", "spicies"])
addToKB(["ingredients", "dried fenugreek leaves", "category", "spicies"])
addToKB(["ingredients", "kashmiri mirch", "category", "spicies"])
addToKB(["ingredients", "onion seeds", "category", "spicies"])
addToKB(["ingredients", "mace", "category", "spicies"])
addToKB(["ingredients", "nutmeg", "category", "spicies"])
addToKB(["ingredients", "herbs", "category", "spicies"])
addToKB(["ingredients", "thyme", "category", "spicies"])
addToKB(["ingredients", "turmeric", "category", "spicies"])
addToKB(["ingredients", "five spice powder", "category", "spicies"])
addToKB(["ingredients", "fenugreek seeds", "category", "spicies"])
addToKB(["ingredients", "fennel", "category", "spicies"])
addToKB(["ingredients", "green cardamom", "category", "spicies"])
addToKB(["ingredients", "dry ginger powder", "category", "spicies"])
addToKB(["ingredients", "dill", "category", "spicies"])
addToKB(["ingredients", "curry leaves", "category", "spicies"])
addToKB(["ingredients", "cumin seeds", "category", "spicies"])
addToKB(["ingredients", "coriander seeds", "category", "spicies"])
addToKB(["ingredients", "coriander leaves", "category", "spicies"])
addToKB(["ingredients", "cloves", "category", "spicies"])
addToKB(["ingredients", "cinnamon", "category", "spicies"])
addToKB(["ingredients", "star anise", "category", "spicies"])
addToKB(["ingredients", "cayenne", "category", "spicies"])
addToKB(["ingredients", "caraway seeds", "category", "spicies"])
addToKB(["ingredients", "cajun spices", "category", "spicies"])
addToKB(["ingredients", "rock salt", "category", "spicies"])
addToKB(["ingredients", "black pepper", "category", "spicies"])
addToKB(["ingredients", "black cumin", "category", "spicies"])
addToKB(["ingredients", "bay leaf", "category", "spicies"])
addToKB(["ingredients", "basil", "category", "spicies"])
addToKB(["ingredients", "black cardamom", "category", "spicies"])
addToKB(["ingredients", "asafoetida", "category", "spicies"])
addToKB(["ingredients", "aniseed", "category", "spicies"])
addToKB(["ingredients", "raw mango powder", "category", "spicies"])
addToKB(["ingredients", "allspice", "category", "spicies"])
addToKB(["ingredients", "carom seeds", "category", "spicies"])
addToKB(["ingredients", "parsley", "category", "spicies"])
addToKB(["ingredients", "acacia", "category", "spicies"])

addToKB(["ingredients", "amaranth", "category", "cereals and pulses"])
addToKB(["ingredients", "flour", "category", "cereals and pulses"])
addToKB(["ingredients", "muesli", "category", "cereals and pulses"])
addToKB(["ingredients", "oats", "category", "cereals and pulses"])
addToKB(["ingredients", "jowar", "category", "cereals and pulses"])
addToKB(["ingredients", "brown rice", "category", "cereals and pulses"])
addToKB(["ingredients", "arborio rice", "category", "cereals and pulses"])
addToKB(["ingredients", "water chestnut flour", "category", "cereals and pulses"])
addToKB(["ingredients", "barnyard millet", "category", "cereals and pulses"])
addToKB(["ingredients", "tapioca", "category", "cereals and pulses"])
addToKB(["ingredients", "semolina", "category", "cereals and pulses"])
addToKB(["ingredients", "finger millet", "category", "cereals and pulses"])
addToKB(["ingredients", "puffed rice", "category", "cereals and pulses"])
addToKB(["ingredients", "buckwheat", "category", "cereals and pulses"])
addToKB(["ingredients", "kidney beans", "category", "cereals and pulses"])
addToKB(["ingredients", "whole bengal gram", "category", "cereals and pulses"])
addToKB(["ingredients", "green gram", "category", "cereals and pulses"])
addToKB(["ingredients", "all purpose flour", "category", "cereals and pulses"])
addToKB(["ingredients", "whole brown lentils", "category", "cereals and pulses"])
addToKB(["ingredients", "husked black gram", "category", "cereals and pulses"])
addToKB(["ingredients", "husked green gram", "category", "cereals and pulses"])
addToKB(["ingredients", "couscous", "category", "cereals and pulses"])
addToKB(["ingredients", "cornmeal", "category", "cereals and pulses"])
addToKB(["ingredients", "pressed rice", "category", "cereals and pulses"])
addToKB(["ingredients", "rice", "category", "cereals and pulses"])
addToKB(["ingredients", "breadcrumbs", "category", "cereals and pulses"])
addToKB(["ingredients", "bread", "category", "cereals and pulses"])
addToKB(["ingredients", "black-eyed beans", "category", "cereals and pulses"])
addToKB(["ingredients", "black gram", "category", "cereals and pulses"])
addToKB(["ingredients", "black beans", "category", "cereals and pulses"])
addToKB(["ingredients", "gram flour", "category", "cereals and pulses"])
addToKB(["ingredients", "bengal gram (split)", "category", "cereals and pulses"])
addToKB(["ingredients", "chickpeas", "category", "cereals and pulses"])
addToKB(["ingredients", "basmati rice", "category", "cereals and pulses"])
addToKB(["ingredients", "barley", "category", "cereals and pulses"])
addToKB(["ingredients", "pearl millet", "category", "cereals and pulses"])
addToKB(["ingredients", "whole wheat flour", "category", "cereals and pulses"])
addToKB(["ingredients", "pigeon pea", "category", "cereals and pulses"])
addToKB(["ingredients", "bean sprouts", "category", "cereals and pulses"])

addToKB(["ingredients", "beef", "category", "meat"])
addToKB(["ingredients", "grass fed chicken", "category", "meat"])
addToKB(["ingredients", "free range chicken", "category", "meat"])
addToKB(["ingredients", "organic chicken", "category", "meat"])
addToKB(["ingredients", "turkey", "category", "meat"])
addToKB(["ingredients", "skinned chicken", "category", "meat"])
addToKB(["ingredients", "pork", "category", "meat"])
addToKB(["ingredients", "partridge", "category", "meat"])
addToKB(["ingredients", "meat stock", "category", "meat"])
addToKB(["ingredients", "keema", "category", "meat"])
addToKB(["ingredients", "mutton liver", "category", "meat"])
addToKB(["ingredients", "ham", "category", "meat"])
addToKB(["ingredients", "kidney meat", "category", "meat"])
addToKB(["ingredients", "crab", "category", "meat"])
addToKB(["ingredients", "chicken stock", "category", "meat"])
addToKB(["ingredients", "chicken liver", "category", "meat"])
addToKB(["ingredients", "chicken", "category", "meat"])
addToKB(["ingredients", "chops", "category", "meat"])
addToKB(["ingredients", "lamb meat", "category", "meat"])
addToKB(["ingredients", "quail", "category", "meat"])
addToKB(["ingredients", "mutton", "category", "meat"])
addToKB(["ingredients", "bacon", "category", "meat"])

addToKB(["ingredients", "gruyere cheese", "category", "dairy products"])
addToKB(["ingredients", "gouda cheese", "category", "dairy products"])
addToKB(["ingredients", "feta cheese", "category", "dairy products"])
addToKB(["ingredients", "milk", "category", "dairy products"])
addToKB(["ingredients", "brie cheese", "category", "dairy products"])
addToKB(["ingredients", "cream cheese", "category", "dairy products"])
addToKB(["ingredients", "ricotta cheese", "category", "dairy products"])
addToKB(["ingredients", "parmesan cheese", "category", "dairy products"])
addToKB(["ingredients", "blue cheese", "category", "dairy products"])
addToKB(["ingredients", "cheddar cheese", "category", "dairy products"])
addToKB(["ingredients", "mascarpone cheese", "category", "dairy products"])
addToKB(["ingredients", "cream", "category", "dairy products"])
addToKB(["ingredients", "provolone cheese", "category", "dairy products"])
addToKB(["ingredients", "mozzarella cheese", "category", "dairy products"])
addToKB(["ingredients", "khoya", "category", "dairy products"])
addToKB(["ingredients", "hung curd", "category", "dairy products"])
addToKB(["ingredients", "yogurt", "category", "dairy products"])
addToKB(["ingredients", "cottage cheese", "category", "dairy products"])
addToKB(["ingredients", "condensed milk", "category", "dairy products"])
addToKB(["ingredients", "clarified butter", "category", "dairy products"])
addToKB(["ingredients", "buttermilk", "category", "dairy products"])
addToKB(["ingredients", "butter", "category", "dairy products"])

addToKB(["ingredients", "cranberry", "category", "fruits"])
addToKB(["ingredients", "kiwi", "category", "fruits"])
addToKB(["ingredients", "blueberries", "category", "fruits"])
addToKB(["ingredients", "mango", "category", "fruits"])
addToKB(["ingredients", "watermelon", "category", "fruits"])
addToKB(["ingredients", "tomato", "category", "fruits"])
addToKB(["ingredients", "strawberry", "category", "fruits"])
addToKB(["ingredients", "water chestnut", "category", "fruits"])
addToKB(["ingredients", "papaya", "category", "fruits"])
addToKB(["ingredients", "orange rind", "category", "fruits"])
addToKB(["ingredients", "orange", "category", "fruits"])
addToKB(["ingredients", "olives", "category", "fruits"])
addToKB(["ingredients", "pear", "category", "fruits"])
addToKB(["ingredients", "sultana", "category", "fruits"])
addToKB(["ingredients", "mulberry", "category", "fruits"])
addToKB(["ingredients", "lychee", "category", "fruits"])
addToKB(["ingredients", "lemon juice", "category", "fruits"])
addToKB(["ingredients", "lemon rind", "category", "fruits"])
addToKB(["ingredients", "ingredientsfruits", "category", "fruits"])
addToKB(["ingredients", "lemon", "category", "fruits"])
addToKB(["ingredients", "raisins", "category", "fruits"])
addToKB(["ingredients", "jamun", "category", "fruits"])
addToKB(["ingredients", "tamarind", "category", "fruits"])
addToKB(["ingredients", "grapefruit", "category", "fruits"])
addToKB(["ingredients", "indian gooseberry", "category", "fruits"])
addToKB(["ingredients", "dried fruit", "category", "fruits"])
addToKB(["ingredients", "dates", "category", "fruits"])
addToKB(["ingredients", "custard apple", "category", "fruits"])
addToKB(["ingredients", "currant", "category", "fruits"])
addToKB(["ingredients", "cooking apples", "category", "fruits"])
addToKB(["ingredients", "coconut", "category", "fruits"])
addToKB(["ingredients", "cherry", "category", "fruits"])
addToKB(["ingredients", "cape gooseberry", "category", "fruits"])
addToKB(["ingredients", "banana", "category", "fruits"])
addToKB(["ingredients", "peach", "category", "fruits"])
addToKB(["ingredients", "apricots", "category", "fruits"])
addToKB(["ingredients", "apples", "category", "fruits"])
addToKB(["ingredients", "figs", "category", "fruits"])
addToKB(["ingredients", "grapes", "category", "fruits"])
addToKB(["ingredients", "pomegranate", "category", "fruits"])
addToKB(["ingredients", "pineapple", "category", "fruits"])
addToKB(["ingredients", "guava", "category", "fruits"])
addToKB(["ingredients", "plum", "category", "fruits"])

addToKB(["ingredients", "shrimp", "category", "seafood"])
addToKB(["ingredients", "tuna fish", "category", "seafood"])
addToKB(["ingredients", "shellfish", "category", "seafood"])
addToKB(["ingredients", "shark", "category", "seafood"])
addToKB(["ingredients", "hilsa", "category", "seafood"])
addToKB(["ingredients", "sardines", "category", "seafood"])
addToKB(["ingredients", "salmon", "category", "seafood"])
addToKB(["ingredients", "prawns", "category", "seafood"])
addToKB(["ingredients", "pomfret", "category", "seafood"])
addToKB(["ingredients", "perch", "category", "seafood"])
addToKB(["ingredients", "pearl spot", "category", "seafood"])
addToKB(["ingredients", "mussels", "category", "seafood"])
addToKB(["ingredients", "mullet", "category", "seafood"])
addToKB(["ingredients", "squids", "category", "seafood"])
addToKB(["ingredients", "haddock", "category", "seafood"])
addToKB(["ingredients", "flounder", "category", "seafood"])
addToKB(["ingredients", "fish stock", "category", "seafood"])
addToKB(["ingredients", "fish", "category", "seafood"])
addToKB(["ingredients", "fish fillet", "category", "seafood"])
addToKB(["ingredients", "cuttle fish", "category", "seafood"])
addToKB(["ingredients", "cod", "category", "seafood"])
addToKB(["ingredients", "clams", "category", "seafood"])
addToKB(["ingredients", "cat fish", "category", "seafood"])
addToKB(["ingredients", "mackerel", "category", "seafood"])
addToKB(["ingredients", "anchovies", "category", "seafood"])
addToKB(["ingredients", "halibut", "category", "seafood"])

addToKB(["ingredients", "brown sugar", "category", "sugar and sugar products"])
addToKB(["ingredients", "sugar candy", "category", "sugar and sugar products"])
addToKB(["ingredients", "icing sugar", "category", "sugar and sugar products"])
addToKB(["ingredients", "honey", "category", "sugar and sugar products"])
addToKB(["ingredients", "jaggery", "category", "sugar and sugar products"])
addToKB(["ingredients", "golden syrup", "category", "sugar and sugar products"])
addToKB(["ingredients", "sugar", "category", "sugar and sugar products"])
addToKB(["ingredients", "castor sugar", "category", "sugar and sugar products"])
addToKB(["ingredients", "caramel", "category", "sugar and sugar products"])
addToKB(["ingredients", "cane sugar", "category", "sugar and sugar products"])

addToKB(["ingredients", "canola oil", "category", "nuts and oilseeds"])
addToKB(["ingredients", "chia seeds", "category", "nuts and oilseeds"])
addToKB(["ingredients", "hazelnut", "category", "nuts and oilseeds"])
addToKB(["ingredients", "pine nuts", "category", "nuts and oilseeds"])
addToKB(["ingredients", "mustard oil", "category", "nuts and oilseeds"])
addToKB(["ingredients", "sunflower seeds", "category", "nuts and oilseeds"])
addToKB(["ingredients", "sesame oil", "category", "nuts and oilseeds"])
addToKB(["ingredients", "pistachio", "category", "nuts and oilseeds"])
addToKB(["ingredients", "olive oil", "category", "nuts and oilseeds"])
addToKB(["ingredients", "mustard seeds", "category", "nuts and oilseeds"])
addToKB(["ingredients", "poppy seeds", "category", "nuts and oilseeds"])
addToKB(["ingredients", "sesame seeds", "category", "nuts and oilseeds"])
addToKB(["ingredients", "peanuts", "category", "nuts and oilseeds"])
addToKB(["ingredients", "chironji", "category", "nuts and oilseeds"])
addToKB(["ingredients", "cashew nuts", "category", "nuts and oilseeds"])
addToKB(["ingredients", "blanched almonds", "category", "nuts and oilseeds"])
addToKB(["ingredients", "almonds", "category", "nuts and oilseeds"])
addToKB(["ingredients", "walnuts", "category", "nuts and oilseeds"])

addToKB(["ingredients", "almond milk", "category", "other ingredients"])
addToKB(["ingredients", "red wine vinegar", "category", "other ingredients"])
addToKB(["ingredients", "red wine", "category", "other ingredients"])
addToKB(["ingredients", "margarine", "category", "other ingredients"])
addToKB(["ingredients", "soy milk", "category", "other ingredients"])
addToKB(["ingredients", "white wine", "category", "other ingredients"])
addToKB(["ingredients", "yeast", "category", "other ingredients"])
addToKB(["ingredients", "white pepper", "category", "other ingredients"])
addToKB(["ingredients", "rice vinegar", "category", "other ingredients"])
addToKB(["ingredients", "sea salt", "category", "other ingredients"])
addToKB(["ingredients", "hoisin sauce", "category", "other ingredients"])
addToKB(["ingredients", "malt vinegar", "category", "other ingredients"])
addToKB(["ingredients", "chocolate chips", "category", "other ingredients"])
addToKB(["ingredients", "quinoa", "category", "other ingredients"])
addToKB(["ingredients", "rice flour", "category", "other ingredients"])
addToKB(["ingredients", "polenta", "category", "other ingredients"])
addToKB(["ingredients", "oyster sauce", "category", "other ingredients"])
addToKB(["ingredients", "guchchi", "category", "other ingredients"])
addToKB(["ingredients", "flat noodles", "category", "other ingredients"])
addToKB(["ingredients", "balsamic vinegar", "category", "other ingredients"])
addToKB(["ingredients", "coconut oil", "category", "other ingredients"])
addToKB(["ingredients", "barfi", "category", "other ingredients"])
addToKB(["ingredients", "rice noodles", "category", "other ingredients"])
addToKB(["ingredients", "coffee", "category", "other ingredients"])
addToKB(["ingredients", "beer", "category", "other ingredients"])
addToKB(["ingredients", "chocolate", "category", "other ingredients"])
addToKB(["ingredients", "sake", "category", "other ingredients"])
addToKB(["ingredients", "vinaigrette", "category", "other ingredients"])
addToKB(["ingredients", "vanilla essence", "category", "other ingredients"])
addToKB(["ingredients", "tortilla", "category", "other ingredients"])
addToKB(["ingredients", "tomato puree", "category", "other ingredients"])
addToKB(["ingredients", "vegetable oil", "category", "other ingredients"])
addToKB(["ingredients", "tartaric acid", "category", "other ingredients"])
addToKB(["ingredients", "soya sauce", "category", "other ingredients"])
addToKB(["ingredients", "vinegar", "category", "other ingredients"])
addToKB(["ingredients", "sharbat", "category", "other ingredients"])
addToKB(["ingredients", "vermicelli", "category", "other ingredients"])
addToKB(["ingredients", "sev", "category", "other ingredients"])
addToKB(["ingredients", "rum", "category", "other ingredients"])
addToKB(["ingredients", "roux", "category", "other ingredients"])
addToKB(["ingredients", "petha", "category", "other ingredients"])
addToKB(["ingredients", "pasta", "category", "other ingredients"])
addToKB(["ingredients", "papad", "category", "other ingredients"])
addToKB(["ingredients", "paan", "category", "other ingredients"])
addToKB(["ingredients", "meringue", "category", "other ingredients"])
addToKB(["ingredients", "mayonnaise", "category", "other ingredients"])
addToKB(["ingredients", "melon seeds", "category", "other ingredients"])
addToKB(["ingredients", "lotus seeds", "category", "other ingredients"])
addToKB(["ingredients", "vetiver", "category", "other ingredients"])
addToKB(["ingredients", "screw pine", "category", "other ingredients"])
addToKB(["ingredients", "jus", "category", "other ingredients"])
addToKB(["ingredients", "jelly", "category", "other ingredients"])
addToKB(["ingredients", "rose water", "category", "other ingredients"])
addToKB(["ingredients", "gold leaves", "category", "other ingredients"])
addToKB(["ingredients", "glycerine", "category", "other ingredients"])
addToKB(["ingredients", "gelatin", "category", "other ingredients"])
addToKB(["ingredients", "fish sauce", "category", "other ingredients"])
addToKB(["ingredients", "desiccated coconut", "category", "other ingredients"])
addToKB(["ingredients", "cranberry sauce", "category", "other ingredients"])
addToKB(["ingredients", "cornflour", "category", "other ingredients"])
addToKB(["ingredients", "cognac", "category", "other ingredients"])
addToKB(["ingredients", "coconut water", "category", "other ingredients"])
addToKB(["ingredients", "coconut milk", "category", "other ingredients"])
addToKB(["ingredients", "cocoa", "category", "other ingredients"])
addToKB(["ingredients", "tea", "category", "other ingredients"])
addToKB(["ingredients", "brown sauce", "category", "other ingredients"])
addToKB(["ingredients", "baking soda", "category", "other ingredients"])
addToKB(["ingredients", "tofu", "category", "other ingredients"])
addToKB(["ingredients", "baking powder", "category", "other ingredients"])
addToKB(["ingredients", "arrowroot", "category", "other ingredients"])
addToKB(["ingredients", "egg", "category", "other ingredients"])
addToKB(["ingredients", "alum", "category", "other ingredients"])
addToKB(["ingredients", "marzipan", "category", "other ingredients"])
addToKB(["ingredients", "ajinomoto", "category", "other ingredients"])
addToKB(["ingredients", "agar", "category", "other ingredients"])

####################################################################
### List of Tools

addToKB(["tools", "pot"])
addToKB(["tools", "apple corer"])
addToKB(["tools", "apple cutter"])
addToKB(["tools", "baster"])
addToKB(["tools", "beanpot"])
addToKB(["tools", "biscuit cutter"])
addToKB(["tools", "biscuit press"])
addToKB(["tools", "blow torch"])
addToKB(["tools", "boil over preventer"])
addToKB(["tools", "bottle opener"])
addToKB(["tools", "bowl"])
addToKB(["tools", "bread knife"])
addToKB(["tools", "browning tray"])
addToKB(["tools", "butter curler"])
addToKB(["tools", "cake and pie server"])
addToKB(["tools", "cheese cutter"])
addToKB(["tools", "cheese knife"])
addToKB(["tools", "cheese slicer"])
addToKB(["tools", "cheesecloth"])
addToKB(["tools", "chef's knife"])
addToKB(["tools", "cherry pitter"])
addToKB(["tools", "chinois"])
addToKB(["tools", "clay pot"])
addToKB(["tools", "cleaver"])
addToKB(["tools", "colander"])
addToKB(["tools", "corkscrew"])
addToKB(["tools", "crab cracker"])
addToKB(["tools", "cutting board"])
addToKB(["tools", "dough scraper"])
addToKB(["tools", "edible tableware"])
addToKB(["tools", "egg piercer"])
addToKB(["tools", "egg poacher"])
addToKB(["tools", "egg separator"])
addToKB(["tools", "egg slicer"])
addToKB(["tools", "egg timer"])
addToKB(["tools", "fillet knife"])
addToKB(["tools", "fish scaler"])
addToKB(["tools", "fish slice"])
addToKB(["tools", "flour sifter"])
addToKB(["tools", "food mill"])
addToKB(["tools", "funnel"])
addToKB(["tools", "garlic press"])
addToKB(["tools", "grapefruit knife"])
addToKB(["tools", "grater"])
addToKB(["tools", "gravy strainer"])
addToKB(["tools", "herb chopper"])
addToKB(["tools", "honey dipper"])
addToKB(["tools", "ladle"])
addToKB(["tools", "lame"])
addToKB(["tools", "lemon reamer"])
addToKB(["tools", "lemon squeezer"])
addToKB(["tools", "lobster pick"])
addToKB(["tools", "mandoline"])
addToKB(["tools", "mated colander pot"])
addToKB(["tools", "measuring cup"])
addToKB(["tools", "measuring spoon"])
addToKB(["tools", "meat grinder"])
addToKB(["tools", "meat tenderiser"])
addToKB(["tools", "meat thermometer"])
addToKB(["tools", "melon baller"])
addToKB(["tools", "mezzaluna"])
addToKB(["tools", "microplane"])
addToKB(["tools", "mortar and pestle"])
addToKB(["tools", "nutcracker"])
addToKB(["tools", "nutmeg grater"])
addToKB(["tools", "oven glove"])
addToKB(["tools", "pastry bag"])
addToKB(["tools", "pastry blender"])
addToKB(["tools", "pastry brush"])
addToKB(["tools", "pastry wheel"])
addToKB(["tools", "peel"])
addToKB(["tools", "peeler"])
addToKB(["tools", "pepper mill"])
addToKB(["tools", "pie bird"])
addToKB(["tools", "pizza cutter"])
addToKB(["tools", "potato masher"])
addToKB(["tools", "potato ricer"])
addToKB(["tools", "pot-holder"])
addToKB(["tools", "poultry shears"])
addToKB(["tools", "roller docker"])
addToKB(["tools", "rolling pin"])
addToKB(["tools", "salt shaker"])
addToKB(["tools", "scales"])
addToKB(["tools", "scissors"])
addToKB(["tools", "scoop"])
addToKB(["tools", "sieve"])
addToKB(["tools", "slotted spoon"])
addToKB(["tools", "spatula"])
addToKB(["tools", "spider"])
addToKB(["tools", "sugar thermometer"])
addToKB(["tools", "tamis"])
addToKB(["tools", "tin opener"])
addToKB(["tools", "tomato knife"])
addToKB(["tools", "tongs"])
addToKB(["tools", "trussing needle"])
addToKB(["tools", "twine"])
addToKB(["tools", "whisk"])
addToKB(["tools", "wooden spoon"])
addToKB(["tools", "zester"])

####################################################################
### List of cooking methods

### Dry methods - don't require much water
addToKB(["cooking-methods", "baking", "dry"])
addToKB(["cooking-methods", "shirring", "dry"])
addToKB(["cooking-methods", "broiling", "dry"])
addToKB(["cooking-methods", "frying", "dry"])
addToKB(["cooking-methods", "deep fat frying", "dry"])
addToKB(["cooking-methods", "sautéing", "dry"])
addToKB(["cooking-methods", "stir-frying", "dry"])
addToKB(["cooking-methods", "deglazing", "dry"])
addToKB(["cooking-methods", "grilling", "dry"])

### Wet methods - requires water
addToKB(["cooking-methods", "bain-marie", "wet"])
addToKB(["cooking-methods", "basting", "wet"])
addToKB(["cooking-methods", "blanching", "wet"])
addToKB(["cooking-methods", "boiling", "wet"])
addToKB(["cooking-methods", "clay pot cooking", "wet"])
addToKB(["cooking-methods", "poaching", "wet"])
addToKB(["cooking-methods", "pressure cooking", "wet"])
addToKB(["cooking-methods", "scalding", "wet"])
addToKB(["cooking-methods", "simmering", "wet"])
addToKB(["cooking-methods", "sous-vide", "wet"])
addToKB(["cooking-methods", "steaming", "wet"])
addToKB(["cooking-methods", "stewing", "wet"])
addToKB(["cooking-methods", "tempering", "wet"])
addToKB(["cooking-methods", "thermal cooking", "wet"])
addToKB(["cooking-methods", "caramelizing", "wet"])

####################################################################
### List of substitutes
## *NOTE* Try to put the most general cases last, example: put "beef stock" before "beef".


### Vegan substitutes - Should not be changed (could be confused with an igredient that must be changed)
addToKB(["substitutes", "vegan", "peanut butter", "peanut butter"])
addToKB(["substitutes", "vegan", "eggplant", "eggplant"])

### Vegan substitutes
addToKB(["substitutes", "vegan", "chicken broth", "vegetable broth"])
addToKB(["substitutes", "vegan", "chicken stock", "vegetable broth"])
addToKB(["substitutes", "vegan", "beef broth", "vegetable broth"])
addToKB(["substitutes", "vegan", "beef stock", "vegetable broth"])
addToKB(["substitutes", "vegan", "beef broth", "vegetable broth"])
addToKB(["substitutes", "vegan", "pork stock", "vegetable broth"])

addToKB(["substitutes", "vegan", "groud meat", "textured soy protein"])
addToKB(["substitutes", "vegan", "groud beef", "textured soy protein"])
addToKB(["substitutes", "vegan", "groud pork", "textured soy protein"])
addToKB(["substitutes", "vegan", "meat", "veggie deli slice"])
addToKB(["substitutes", "vegan", "beef", "veggie deli slice"])
addToKB(["substitutes", "vegan", "steak", "portobello mushrooms"])
addToKB(["substitutes", "vegan", "burger", "veggie burger"])
addToKB(["substitutes", "vegan", "meatball", "veggie meatball"])
addToKB(["substitutes", "vegan", "bacon", "veggie bacon"])
addToKB(["substitutes", "vegan", "turkey", "soy turkey patties"])
addToKB(["substitutes", "vegan", "chicken", "soy chicken patties"])
addToKB(["substitutes", "vegan", "chicken nuggets", "soy chicken nuggets"])
addToKB(["substitutes", "vegan", "jerky", "veggie jerky"])
addToKB(["substitutes", "vegan", "pork", "tempeh"])

# TODO: deal with all kinds of seafood.
addToKB(["substitutes", "vegan", "fish", "tempeh"]) 
addToKB(["substitutes", "vegan", "shrimp", "tofu"])
addToKB(["substitutes", "vegan", "prawn", "tofu"])

# TODO: deal with all kinds of dairy food.
addToKB(["substitutes", "vegan", "milk powder", "almond milk powder"])
addToKB(["substitutes", "vegan", "milk", "soy milk"])
addToKB(["substitutes", "vegan", "milk", "rice milk"])

addToKB(["substitutes", "vegan", "ice cream", "soy ice cream"])
addToKB(["substitutes", "vegan", "ice cream", "rice ice cream"])

# TODO: deal with all kinds of cheese.
addToKB(["substitutes", "vegan", "cheese", "tofu"])
addToKB(["substitutes", "vegan", "cheese", "crumbled tofu"])
addToKB(["substitutes", "vegan", "cheese", "soaked raw nuts"])
addToKB(["substitutes", "vegan", "parmesan cheese", "vegan parmesan cheese"])

addToKB(["substitutes", "vegan", "butter", "margarine"])

addToKB(["substitutes", "vegan", "yogurt", "soy yogurt"])
addToKB(["substitutes", "vegan", "yogurt", "coconut yogurt"])
addToKB(["substitutes", "vegan", "yogurt", "almond yogurt"])

# eggs are a special case for ingredient mesurement and quantity and preparation.
addToKB(["substitutes", "vegan", "egg", "tofu", "measurement_change", "oz"])
addToKB(["substitutes", "vegan", "egg", "tofu", "quantity_change", "1.4"])
addToKB(["substitutes", "vegan", "egg", "tofu", "preparation_change", ""])

addToKB(["substitutes", "vegan", "scrambled egg", "tofu scramble"])

addToKB(["substitutes", "vegan", "baked egg", "applesauce"])
addToKB(["substitutes", "vegan", "baked egg", "pureed soft tofu"])
addToKB(["substitutes", "vegan", "baked egg", "flax egg"])
addToKB(["substitutes", "vegan", "baked egg", "mashed bananas"])

addToKB(["substitutes", "vegan", "binding egg", "soy flour"])
addToKB(["substitutes", "vegan", "binding egg", "bread crumbs"])
addToKB(["substitutes", "vegan", "binding egg", "rolled oats"])

addToKB(["substitutes", "vegan", "instant puddings", "dairy free instant pudding"])
addToKB(["substitutes", "vegan", "pudding", "dairy free pudding"])

addToKB(["substitutes", "vegan", "sour cream", "vegan sour cream"])

addToKB(["substitutes", "vegan", "mayonnaise", "vegan mayonnaise"])

addToKB(["substitutes", "vegan", "gelatin", "agar flakes"])

addToKB(["substitutes", "vegan", "honey", "liquid sweetener"])

addToKB(["substitutes", "vegan", "chocolate", "non-dairy chocolate chips"])
addToKB(["substitutes", "vegan", "chocolate", "non-dairy cocoa powders"])

addToKB(["substitutes", "vegan", "hollandaise sauce", "vegan hollandaise sauce"])

addToKB(["substitutes", "vegan", "bread", "wheat tortilla"])
addToKB(["substitutes", "vegan", "toast", "wheat tortilla"])
addToKB(["substitutes", "vegan", "bagel", "wheat tortilla"])
addToKB(["substitutes", "vegan", "baguette", "wheat tortilla"])
addToKB(["substitutes", "vegan", "biscuit", "wheat tortilla"])
addToKB(["substitutes", "vegan", "brioche bun", "wheat tortilla"])
addToKB(["substitutes", "vegan", "brioche", "wheat tortilla"])
addToKB(["substitutes", "vegan", "ciabatta", "wheat tortilla"])
addToKB(["substitutes", "vegan", "naan", "wheat tortilla"])

addToKB(["substitutes", "vegan", "pancake", "vegan pancake"])
addToKB(["substitutes", "vegan", "cracker", "whole wheat cracker"])

### Chinese Style substitutes
addToKB(["substitutes", "toChinese", "garlic", "bees"])
addToKB(["substitutes", "toChinese", "olive oil", "bees oil"])
addToKB(["substitutes", "toChinese", "spaghetti", "bee-ghetti"])


# {'flour': 'gluten-free flour', 'couscous': 'quinoa', 'bread crumbs': 
# 'ground flaxseeds', 'tortilla': 'corn tortilla', 'pita': 'large collard leaf',
# 'sugar': 'unsweetened applesauce', 'white sugar': 'unsweetened applesauce', 
# 'peanut butter': 'natural peanut butter',
# 'butter': 'unsweetened butter', 'milk': 'almond milk', 'cream': 'coconut milk',
# 'soy sauce': 'low-sodium soy sauce', 'rice': 'brown rice', 'white rice': 'brown rice',
# 'bread': 'whole-wheat bread', 'white bread': 'whole-wheat bread', 'sour cream': 'greek yogurt', 
# 'mayonnaise': 'greek yogurt with hint of herbs and lemon juice', 'ground beef': 'ground turkey',
# 'ground pork': 'ground turkey',
# 'bacon': 'lean prosciutto', 'cream cheese': 'fat-free cream cheese', 'lettuce': 'arugula',
# 'penne pasta': 'brown rice pasta', 'syrup': 'applesauce', 'ketchup': 'sun-dried tomato hummus'}
### Healthy substitutes
addToKB(["substitutes", "healthy", "sugar", "unsweetened applesauce"])
addToKB(["substitutes", "healthy", "white sugar", "unsweetened applesauce"])
addToKB(["substitutes", "healthy", "peanut butter", "natural peanut butter"])
addToKB(["substitutes", "healthy", "butter", "unsweetened butter"])
addToKB(["substitutes", "healthy", "milk", "almond milk"])
addToKB(["substitutes", "healthy", "cream", "coconut milk"])
addToKB(["substitutes", "healthy", "soy sauce", "low-sodium soy sauce"])
addToKB(["substitutes", "healthy", "sour cream", "greek yogurt"])
addToKB(["substitutes", "healthy", "mayonnaise", "greek yogurt with hint of herbs and lemon juice"])
addToKB(["substitutes", "healthy", "syrup", "applesauce"])
addToKB(["substitutes", "healthy", "ketchup", "sun-dried tomato hummus"])


addToKB(["substitutes", "healthy", "rice", "brown rice"])
addToKB(["substitutes", "healthy", "white rice", "brown rice"])
addToKB(["substitutes", "healthy", "bread", "whole-wheat bread"])
addToKB(["substitutes", "healthy", "white bread", "whole-wheat bread"])
addToKB(["substitutes", "healthy", "flour", "gluten-free flour"])
addToKB(["substitutes", "healthy", "couscous", "quinoa"])
addToKB(["substitutes", "healthy", "bread crumb", "ground flaxseed"])
addToKB(["substitutes", "healthy", "tortilla", "corn tortilla"])
addToKB(["substitutes", "healthy", "pita", "Boiled large collard leaf"])
addToKB(["substitutes", "healthy", "penne pasta", "brown rice pasta"])



addToKB(["substitutes", "healthy", "ground beef", "ground turkey"])
addToKB(["substitutes", "healthy", "ground pork", "ground turkey"])
addToKB(["substitutes", "healthy", "bacon", "lean prosciutto"])
addToKB(["substitutes", "healthy", "canadian-style bacon", "lean prosciutto"])
addToKB(["substitutes", "healthy", "sausage", "turkey sausage"])
addToKB(["substitutes", "healthy", "chorizo sausage", "turkey sausage"])
addToKB(["substitutes", "healthy", "eggs", "egg whites"])
addToKB(["substitutes", "healthy", "egg", "egg white"])


addToKB(["substitutes", "healthy", "monterey jack", "reduced-calorie cheese"])
addToKB(["substitutes", "healthy", "monterey jack", "reduced-calorie cheese"])
addToKB(["substitutes", "healthy", "monterey jack", "reduced-calorie cheese"])
addToKB(["substitutes", "healthy", "monterey jack", "reduced-calorie cheese"])


addToKB(["substitutes", "healthy", "cream cheese", "fat-free cream cheese"])
addToKB(["substitutes", "healthy", "cheddar cheese", "reduced-calorie cheddar cheese"])
addToKB(["substitutes", "healthy", "swiss cheese", "reduced-calorie swiss cheese"])
addToKB(["substitutes", "healthy", "pepper jack cheese", "reduced-calorie pepper jack cheese"])
addToKB(["substitutes", "healthy", "monterey jack", "reduced-calorie monterey jack"])
addToKB(["substitutes", "healthy", "monterey jack cheese", "reduced-calorie monterey jack cheese"])
addToKB(["substitutes", "healthy", "provolone cheese", "reduced-calorie provolone cheese"])
addToKB(["substitutes", "healthy", "parmesan cheese", "reduced-calorie parmesan cheese"])
addToKB(["substitutes", "healthy", "mozarella", "reduced-calorie mozarella"])
addToKB(["substitutes", "healthy", "shredded mozarella", "reduced-calorie shredded mozarella"])
addToKB(["substitutes", "healthy", "mozarella cheese", "reduced-calorie mozarella cheese"])


addToKB(["substitutes", "healthy", "lettuce", "arugula"])
### End of KB
####################################################################

# Testing

if TESTING_KNOWLEDGE_BASE:
    print(isInKB(["ingredients", "milk"]))
    print(isInKB(["ingredients", "xx"]))
    print(isInKB(["cooking-methods", "baking"]))
    print(isInKB(["cooking-methods", "baking", "dry"]))
    print(isInKB(["cooking-methods", "baking", "wet"]))
    print(isInKB(["cooking-methods", "baking", "wet"]))
    print(isInKB(["cooking-methods", "baking", "wet"]))
    print(isInKB(["cooking-methods", "bak.*", "dry"], regex=True))
    print(isInKB(["cooking-methods", "baking", "d.*"], regex=True))
    print(isInKB(["cooking-methods", ".*", "wet"], regex=True))
    print(isInKB([".*"], regex=True))

    prettyPrintKBsubtree(kb_subtree = getKBSubtree(["cooking-methods"]))

    print("list of ingredients = ")
    print(list(getKBSubtree(["ingredients"]).keys()))