# Imagine a list as a treasure chest
treasure_chest = ["gold", "silver", "diamond"]
print("Initial treasures:", treasure_chest)  # Display the initial treasures

# A new treasure is discovered and added to the chest
treasure_chest.append("emerald")
print("Added a shiny emerald:", treasure_chest)  # The chest shines brighter!

# We find a whole new stash of treasures and add them to our chest
treasure_chest.extend(["ruby", "sapphire", "pearl"])
print("New stash added:", treasure_chest)  # The chest is now overflowing!

# Oops! The chest is too full, we must remove the last treasure
del(treasure_chest[-1])
print("Had to let go of the last treasure:", treasure_chest)  # The chest is more balanced now.

# The silver was tarnished, let's remove it
treasure_chest.remove("silver")
print("Removed the tarnished silver:", treasure_chest)  # The remaining treasures shine even brighter!

# Time to sell the last item in the chest
sold_treasure = treasure_chest.pop()
print(f"Sold the {sold_treasure}:", treasure_chest)  # The chest feels lighter.

# Let's take out the first treasure from the chest
first_treasure = treasure_chest.pop(0)
print(f"Traded the {first_treasure} for a map:", treasure_chest)  # The adventure continues!
