# Encode - AI Bootcamp - Week 1 Project

This repository holds the weekend group project of week 1 for Encode AI Bootcamp. This is a python package which implements uses OPENAI API and prompt engineering to expose Chef GPT with some configurable personality  traits.

## Group Members' IDs
- **76tsNrC**
- **ipJZCWC**
- **s0qmoqC**
- **3nmWtwC**
- **XLiUjNC**

## Chef Personalities (WIP)

- **Antreas** (ID: s0qmoqC): A grumpy greek chef who cooks only traditional, authentic greek cuisine.
- **Arjun** (ID: s0qmoqC): A young and spirited Indian cook that loves to make Biryani.

> **TODO:** Add more personalities

## Get Started

Before runnning the script you can set your OPENAI API key by setting the `OPENAI_KEY` environment variable. If the key is not set at runtime the script will prompt you to provide it as an input.

Instead of a explicitly setting the env var in your terminal e.g. using `export OPENAI_KEY=...` you can also do it using a .env file. See the [.env.example](./.env.example) file for reference.

You can either get started by installing the package remotely from github or by cloning the repository locally.

### Run script by cloning:

Clone the repo
```
git clone https://github.com/apogiatzis/encode-ai-chefgpt && cd encode-ai-chefgpt
```

Make sure that you have poetry installed:
```
pip install -U poetry
```

Install dependencies:
```
poetry install
```

Run ChefGPT
```
poetry run chefgpt --chef <chef_name> ask
```



### Run script by installing package from github remote:

Install package from github
```
pip install git+https://github.com/apogiatzis/encode-ai-chefgpt.git
```

> Note that if you have installed the package using pip from the github remote any .env files in the current path won't be picked up.

Run ChefGPT
```
OPENAI_KEY="sk-..." chefgpt --chef <chef_name> ask
```

### Uninstall

To uninstall the package run:
```
pip uninstall chefgpt    
```

### How to add more Chef personalities:

The project is build in a modular way so that Chef personalities are open for extension. To add a new personality just create a new concrete subclass of `ChefPersonality` in [chef_personalities.py](./chefgpt/chef_personalities.py) and define the name and prompt properties. 

To add the new personality to the CLI just include the new class in the `chefs_map` dictionary in [chef_personalities.py](./chefgpt/chef_personalities.py)

### Examples

Here are some examples of ChefGPT questions and responses:

```
chefgpt --chef Antreas ask
```
```
[+] You have selected Chef Antreas!
[+] What would you like to ask your Chef?
(you) >>> Give me a recipe for Moussaka
(Antreas) >>> Ah, finally a request for a proper dish! Moussaka, a beloved Greek classic. Here's the detailed recipe for a traditional Greek Moussaka:

Ingredients:
- 2 large eggplants, sliced
- 1 lb ground lamb (you can also use beef)
- 1 large onion, chopped
- 2 garlic cloves, minced
- 1 can (14.5 oz) diced tomatoes
- 1/2 cup red wine
- 1/2 tsp ground cinnamon
- 1/4 tsp ground allspice
- Salt and pepper to taste
- Olive oil
- 1/4 cup butter
- 1/3 cup all-purpose flour
- 3 cups milk
- Pinch of nutmeg
- 1 cup grated kefalotyri or Parmesan cheese
- 1 egg, beaten

For the layers:
- Cooked eggplant slices
- Meat sauce
- Bechamel sauce

Instructions:
1. Preheat your oven to 375°F (190°C).
2. Sprinkle eggplant slices with salt and let them sit for about 30 minutes to draw out the bitter juices. Rinse and pat dry.
3. In a pan, heat olive oil and sauté the eggplant slices until lightly browned. Set aside.
4. In the same pan, add more olive oil and sauté the onions until translucent. Add garlic and cook until fragrant.
5. Add the ground lamb, breaking it up with a spoon, and cook until browned.
6. Stir in the diced tomatoes, red wine, cinnamon, allspice, salt, and pepper. Let it simmer for about 20 minutes.
7. In another saucepan, melt the butter over medium heat. Stir in the flour to make a roux.
8. Slowly add the milk while whisking continuously to avoid lumps. Cook until thickened.
9. Remove from heat and stir in nutmeg, half of the cheese, and beaten egg.
10. To assemble, layer half of the eggplant slices in a baking dish, followed by the meat sauce, then the remaining eggplant slices, and finally the bechamel sauce.
11. Sprinkle the remaining cheese on top.
12. Bake in the preheated oven for about 45 minutes or until golden brown and bubbly.
13. Let it rest for a bit before slicing and serving.

Enjoy your hearty and comforting Moussaka!
```