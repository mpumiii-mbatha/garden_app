# Hardcoded values for the season and plant type
season = "summer"  # TODO: Replace with input() to allow user interaction.
plant_type = "flower"  # TODO: Replace with input() to allow user interaction.

# Dictionary storing gardening advice for multiple seasons and plant types (issue -1 fixed)
gardening_advice = {
    "summer": {
        "flower": "Water your plants regularly and provide some shade.",
        "vegetable": "Water daily and mulch to retain moisture.",
        "herb": "Trim herbs regularly to encourage growth."
    },
    "winter": {
        "flower": "Protect your plants from frost with covers.",
        "vegetable": "Grow hardy vegetables like kale or spinach.",
        "herb": "Keep herbs indoors in a sunny spot."
    },
    "spring": {
        "flower": "Plant new flowers and fertilise the soil.",
        "vegetable": "Start seedlings and keep soil moist.",
        "herb": "Begin planting herbs outdoors after the last frost."
    },
    "autumn": {
        "flower": "Deadhead spent blooms and prepare beds for winter.",
        "vegetable": "Harvest remaining crops and compost dead plants.",
        "herb": "Dry herbs for winter storage."
    }
}

# Dictionary of recommended plants per season (issue -1 fixed)
season_recommendations = {
    "summer": ["Sunflowers", "Tomatoes", "Basil"],
    "winter": ["Kale", "Spinach", "Thyme"],
    "spring": ["Roses", "Lettuce", "Mint"],
    "autumn": ["Marigolds", "Carrots", "Oregano"]
}

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season and plant type (issue -2 fixed)
if season in gardening_advice and plant_type in gardening_advice[season]:
    advice = gardening_advice[season][plant_type]
else:
    advice = "No advice for this combination."

# Print the generated advice
print(advice)

# Recommendations for plants based on the entered season added (issue -2 fixed)
if season in season_recommendations:
    recommendations = season_recommendations[season]
    print(f"Recommended plants for {season.capitalize()}: {', '.join(recommendations)}")
else:
    print("No recommendations for this season.")


# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
