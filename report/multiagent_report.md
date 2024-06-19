## Multi agent ChefGPT intereaction report

This reports aims to summarise and observe the interaction between multiple ChefGPT agents.

Please find below the a chain of interactions between the various ChefGPTs. Note the difference in responses amongst the agent based on their personalities.

### Dish Recipe Requests

<table>
    <tr>
        <td>Personality Name</td>
        <td>Question</td>
        <td>Response</td>
    </tr>
    <tr>
        <td>Antreas</td>
        <td>
            <code>
                Give me a recipe for Moussaka
            </code>
        </td>
        <td>
            <code id="dish-recipe-1">
                Ah, finally a request for a proper dish! Moussaka, a beloved Greek classic. Here's the detailed recipe for a traditional Greek Moussaka:

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
            </code>
        </td>
    </tr>
    <tr>
        <td>Arjun</td>
        <td>
            <code>
                Give me a recipe for Chicken korma
            </code>
        </td>
        <td>
            <code id="dish-recipe-2">
            Absolutely, I'd be happy to share a Chicken Korma recipe with you!

Ingredients:
- 1 kg chicken, cut into pieces
- 2 large onions, finely sliced
- 4 cloves of garlic, minced
- 1-inch piece of ginger, grated
- 1 cup plain yogurt
- 1/2 cup ground almonds
- 1/2 cup heavy cream
- 2 tablespoons ghee or vegetable oil
- 2 bay leaves
- 4 green cardamom pods
- 4 cloves
- 1 cinnamon stick
- 1 teaspoon cumin seeds
- 1 teaspoon coriander powder
- 1/2 teaspoon turmeric powder
- 1 teaspoon red chili powder (adjust to your spice preference)
- Salt to taste
- Fresh coriander leaves for garnish

Instructions:
1. In a large bowl, mix the yogurt, ground almonds, cream, garlic, and ginger. Add the chicken pieces to this mixture, ensuring they are well coated. Marinate for at least 30 minutes, preferably longer in the fridge.

2. Heat ghee/oil in a large pot over medium heat. Add the bay leaves, cardamom pods, cloves, cinnamon stick, and cumin seeds. Sauté for a minute until fragrant.

3. Add the sliced onions and cook until they turn golden brown.

4. Add the marinated chicken along with the marinade to the pot. Stir well and let it cook for a few minutes.

5. Add coriander powder, turmeric powder, red chili powder, and salt. Mix everything together and let it cook on low heat for about 30-40 minutes or until the chicken is tender.

6. Once the chicken is cooked through, check the seasoning and adjust salt and spices if needed.

7. Garnish with fresh coriander leaves and serve hot with rice, naan, or roti.

Enjoy your delicious Chicken Korma!
            </code>
        </td>
    </tr>
    <tr>
        <td>Lorenzo</td>
        <td>Give a recipe for the finest Italian Carbonara, with French Cream</td>
        <td>Oh, mio caro! Finest Italian Carbonara with French cream? Ah, no, no, no! In Italy, we make Carbonara with eggs, pecorino cheese, pancetta, and pepper - no French cream here!

Now, I will share with you a traditional Italian Carbonara recipe, just like how we make it in the old country. Here you go:

Ingredients:
- 400g spaghetti
- 200g pancetta or guanciale (Italian cured pork cheek), diced      

5. Remove the skillet from the heat and quickly pour the egg and cheese mixture over the hot pasta. Toss the spaghetti vigorously to coat each strand in the creamy sauce. The heat from the pasta will cook the eggs, creating a silky, creamy sauce.

6. If the sauce seems too thick, you can add some of the reserved pasta water a little at a time until you reach your desired consistency.

7. Season with salt and more black pepper if needed. Serve immediately, garnished with extra grated Pecorino Romano cheese and a sprinkle of black pepper.

Ecco fatto! A delicious and authentic Italian Carbonara, just like Nonna used to make. Enjoy, caro mio! Buon appetito! 🍝</td>
    </tr>
</table>

### Ingredients Recipe Requests

<table>
    <tr>
        <td>Personality Name</td>
        <td>Question</td>
        <td>Response</td>
    </tr>
    <tr>
        <td>Antreas</td>
        <td>
            <code>
                Give me a recipe that uses the following ingredients:
Celery
Eggplant
Sweet Potato
            </code>
        </td>
        <td>
            <code>
                Ugh, sweet potato, celery, and eggplant. What are we making here, a mishmash of confusion? Anyway, since you're intent on mixing these odd ingredients, we'll make a somewhat acceptable dish called "Briam," a Greek roasted vegetable dish. Here's the recipe—try not to set the kitchen on fire:

Ingredients:
- 2 sweet potatoes, peeled and cut into chunks
- 1 large eggplant, cut into chunks
- 3-4 celery stalks, chopped
- 3-4 tomatoes, sliced
- 1 onion, sliced
- 4-5 garlic cloves, minced
- 1/2 cup olive oil
- 1 teaspoon dried oregano
- Salt and pepper to taste
- Fresh parsley, chopped (for garnish)

Instructions:
1. Preheat your oven to 200°C (400°F).
2. In a large baking dish, layer the sweet potatoes, eggplant, celery, tomatoes, onion, and garlic.
3. Drizzle the olive oil over the vegetables. Season with oregano, salt, and pepper. Toss everything together to coat the vegetables evenly.
4. Cover the baking dish with foil and roast in the preheated oven for about 45 minutes.
5. Remove the foil and bake for an additional 15-20 minutes until the vegetables are tender and lightly browned.
6. Garnish with fresh parsley before serving.

There you have it, a not-so-Greek Briam made with your peculiar ingredient selection. Just remember, Greeks might raise an eyebrow at this combo!
            </code>
        </td>
    </tr>
    <tr>
        <td>Arjun</td>
        <td>
            <code>
                 Give me a recipe with the following ingredients:
Cocoa 
Coffee
Rice
            </code>
        </td>
        <td>
            <code>
                It seems like you're interested in making an interesting dish combining cocoa, coffee, and rice. One unique dish you can try is a Chocolate Coffee Rice Pudding. Here's a recipe for you to enjoy:

Ingredients:
- 1 cup rice
- 2 cups water
- 1 cup milk
- 2 tablespoons cocoa powder
- 2 tablespoons Instant coffee powder
- 1/2 cup sugar
- 1/2 teaspoon vanilla extract
- A pinch of salt
- Whipped cream, chocolate syrup, and coffee beans for garnish (optional)

Instructions:
1. Rinse the rice under cold water until the water runs clear.
2. In a medium saucepan, bring the water to a boil, then add the rice. Reduce heat to low, cover, and simmer for about 18-20 minutes or until the rice is cooked and water is absorbed.
3. In a separate saucepan, combine milk, cocoa powder, instant coffee powder, sugar, vanilla extract, and salt. Heat the mixture over medium heat, stirring constantly until well combined and hot but not boiling.
4. Once the rice is cooked, pour the cocoa-coffee mixture over the rice in the saucepan. Stir well to combine all ingredients.
5. Cook over low heat for another 5-10 minutes, stirring occasionally, until the pudding reaches your desired consistency.
6. Remove from heat and let it sit for a few minutes to thicken further.
7. Serve the Chocolate Coffee Rice Pudding warm or chilled. Optionally, top with whipped cream, a drizzle of chocolate syrup, and a few coffee beans for garnish.

Enjoy your unique Chocolate Coffee Rice Pudding!
            </code>
        </td>
    </tr>
    <tr>
        <td>Lorenzo</td>
        <td>I live in the United Kingdom. Make me a traditional italian recipe with the following ingredients: Cheddar, Bacon, Baked Beans</td>
        <td>Oh, mio Dio! Cheddar, bacon, and baked beans?! These ingredients are like telling Michelangelo to paint with mud! In Italia, we make art with food, not English breakfast leftovers! But, I will help you anyway, because Nonna is just that kind.

Let's make a dish I like to call "Italian-Inspired Pasta Carbonara":

Ingredients:
- 350g spaghetti
- 200g pancetta or guanciale (Italian bacon)
- 3 large eggs
- 100g Pecorino Romano cheese, grated (please, no Cheddar!)
- Black pepper, freshly ground
- Olive oil
- Salt

1. Cook the spaghetti in a large pot of salted boiling water until al dente. Save a cup of pasta water for later.
2. While the pasta cooks, heat a drizzle of olive oil in a pan and add the pancetta or guanciale. Cook until crispy but not burnt.
3. In a bowl, beat the eggs, grated Pecorino Romano cheese, and a generous amount of freshly ground black pepper.
4. When the pasta is done, drain it and return it to the pot. Remove the pot from the heat.
5. Quickly add the cooked pancetta or guanciale to the pasta and mix well.
6. Now, pour the egg and cheese mixture over the hot pasta. Mix quickly and thoroughly. The heat from the pasta will cook the eggs, creating a creamy sauce. If needed, add some reserved pasta water to loosen the sauce.
7. Serve immediately, garnished with a bit more Pecorino Romano and black pepper.

There you go! A little taste of Italy to rescue those poor English ingredients. Buon appetito! And remember, real carbonara has no beans!</td>
    </tr>
</table>

### Criticise Recipe Requests

<table>
    <tr>
        <td>Personality Name</td>
        <td>Question</td>
        <td>Response</td>
        <td>Remarks</td>
    </tr>
    <tr>
        <td>Antreas</td>
        <td>
            <code>
                Criticise the following recipe:
        Ingredients:
- 1 kg chicken, cut into pieces
- 2 large onions, finely sliced
- 4 cloves of garlic, minced
- 1-inch piece of ginger, grated
- 1 cup plain yogurt
- 1/2 cup ground almonds
- 1/2 cup heavy cream
- 2 tablespoons ghee or vegetable oil
- 2 bay leaves
- 4 green cardamom pods
- 4 cloves
- 1 cinnamon stick
- 1 teaspoon cumin seeds
- 1 teaspoon coriander powder
- 1/2 teaspoon turmeric powder
- 1 teaspoon red chili powder (adjust to your spice preference)
- Salt to taste
- Fresh coriander leaves for garnish

Instructions:
1. In a large bowl, mix the yogurt, ground almonds, cream, garlic, and ginger. Add the chicken pieces to this mixture, ensuring they are well coated. Marinate for at least 30 minutes, preferably longer in the fridge.

2. Heat ghee/oil in a large pot over medium heat. Add the bay leaves, cardamom pods, cloves, cinnamon stick, and cumin seeds. Sauté for a minute until fragrant.

3. Add the sliced onions and cook until they turn golden brown.

4. Add the marinated chicken along with the marinade to the pot. Stir well and let it cook for a few minutes.

5. Add coriander powder, turmeric powder, red chili powder, and salt. Mix everything together and let it cook on low heat for about 30-40 minutes or until the chicken is tender.

6. Once the chicken is cooked through, check the seasoning and adjust salt and spices if needed.

7. Garnish with fresh coriander leaves and serve hot with rice, naan, or roti. 
            </code>
        </td>
        <td>
            <code>
                Oh, what a modern mishmash of flavors and ingredients! I see chicken, yogurt, almonds, and cream all in one dish. Is this some kind of chicken biryani trying to pose as a curry? Cardamom, cumin, and coriander are confusing my Greek taste buds! And don't get me started on the turmeric and chili powder. Where's the oregano, lemon, or feta cheese in this recipe? This dish seems lost in the world of Indian spices and creams. If you want a true Greek feast, let me teach you how to make a traditional Spanakopita or Souvlaki. Enough with this culinary confusion, bring on some real Greek flavors!
            </code>
        </td>
        <td>
            This criticises the recipe generated by another agent [here](#dish-recipe-2)
        </td>
    </tr>
    <tr>
        <td>
            Arjun
        </td>
        <td>
            <code>
            Criticise the following recipe:
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
            </code>
        </td>
        <td>
            <code>
            It seems like you're sharing a recipe for a layered eggplant and ground lamb dish with a bechamel sauce. While the overall combination sounds delicious, there are a few suggestions and critiques to enhance the dish:

1. **Eggplant Prep:** Drawing out the bitter juices is a good step, but make sure to rinse the eggplant well after salting to remove excess salt, which can make the dish too salty.

2. **Flavor Enhancement:** Consider adding more herbs and spices to the meat sauce for depth of flavor. Traditional Mediterranean herbs like oregano and thyme could complement the cinnamon and allspice nicely.

3. **Bechamel Sauce:** While a classic bechamel sauce is delicious, consider infusing it with additional flavors like garlic or bay leaves for extra depth.

4. **Cheese:** Using Parmesan cheese is lovely, but you might also consider adding a layer of creamy mozzarella in the dish for that stringy, cheesy goodness when baked.

5. **Assembly:** When layering the dish, make sure to spread the sauces evenly to ensure each bite has a perfect balance of flavors.

6. **Baking Time:** Keep an eye on the dish while it bakes to prevent the top from burning. Cover it with foil if it browns too quickly.

Overall, the recipe sounds tasty, but feel free to play with the flavors and ingredients to make it your own and suit your preferences! Happy cooking!
            </code>
        </td>
        <td>
            This criticises the recipe generated by another agent [here](#dish-recipe-1)
        </td>
    </tr>
    <tr>
        <td>Lorenzo</td>
        <td>Criticise the following recipe:
Best of British platter recipe
Host an unforgettable Christmas celebration with this impressive party platter showcasing the best of classic British flavours. From beef and horseradish Yorkshire pudding wraps and honey mustard sausages, to creamy whipped Stilton with crunchy carrot and celery crudités, there's something for everyone to enjoy. See method

Serves 8
30 mins to prepare and 30 mins to cook
327 calories / serving
Ingredients
350g pack celery sticks
4 carrots, quartered lengthways
240g pack radishes, trimmed and halved
For the Yorkshire pudding wraps
140g plain flour
4 eggs
200ml milk
4 tbsp creamed horseradish
100g roast beef slices
60g bag wild rocket
For the honey mustard sausages
212g pack cocktail sausages
2 tbsp clear honey
2 tbsp wholegrain mustard
English or wholegrain mustard, to serve (optional)
For the whipped Stilton
100g Stilton
80ml single cream
Method
To make the Yorkshire pudding wraps, preheat the oven to gas 8, 230°C, fan 210 ̊C and line a baking tray (about 30 x 15cm) with noonstick baking paper. In a large bowl, whisk the flour and eggs until smooth, then slowly whisk in the milk. Pour the mixture into the baking tray and bake for 20-25 mins until puffed up and golden. Set aside to cool.
Reduce the oven to gas 4, 180 ̊C, fan 160 ̊C. Roast the sausages on a baking tray for 10-15 mins or until cooked through. Mix the   honey and mustard in a bowl and set aside.
Meanwhile, crumble the Stilton into a bowl, add the cream and whisk until thick and smooth.
Pour the honey and mustard mix over the sausages. Transfer to a serving dish.
Remove the cooled Yorkshire pudding from the tray and turn upside down. Spread with the horseradish, layer with beef and rocket; season. Roll up, then skewer 1cm apart with cocktail sticks and slice into wheels.
Transfer the pinwheels to a platter with the honey mustard sausages and the mustard, if using. Arrange the celery, carrots and radishes next to the Stilton.</td>
        <td>Oh, mio caro... what is this British monstrosity you've brought to Nonna's kitchen? A platter full of Yorkshire pudding wraps and honey mustard sausages... Che schifezza! Let me tell you, this is not how we do things in Italia.

First off, let's talk about those Yorkshire pudding wraps. Yorkshire pudding belongs next to a beautiful Sunday roast, not being filled with horseradish and roast beef. And then wrapping it up? Sacrilege! It should be crispy on the outside, fluffy on the inside, not turned into some strange wrap.

And those honey mustard sausages? Mamma Mia... clear honey and wholegrain mustard slathered over cocktail sausages? Nonna has never heard of such a thing! Sausages should be cooked with amore, maybe in a rich tomato sauce or with some bell peppers and onions, not drowned in honey and mustard.

And lastly, whipped Stilton served with celery and carrots... Stilton is a fine cheese, but whipping it up like that? Nonna prefers her Stilton crumbled over a fresh salad or paired with a lovely glass of red wine, not turned into some creamy concoction.      

My advice to you, caro mio, is to ditch this British platter and come to Nonna's kitchen where I'll teach you how to make a proper Italian meal with fresh tomatoes, fragrant basil, and amore in every bite! Viva l'Italia!</td>
        <td>Tesco Recipe https://realfood.tesco.com/recipes/world-flavours/british-recipes.html</td>
    </tr>
</table>
