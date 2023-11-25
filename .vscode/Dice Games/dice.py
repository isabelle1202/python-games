
import random
# ask the user how many dice they'd like to roll


def get_rolls():
    """gets the amount of dice the player wants to roll"""
    while True:
        rolls = int(input("How many dice would you like to roll? [1-6] "))
        if 1 <= rolls <= 6:
            return rolls
        else:
            print("Please enter a digit between 1 and 6.")


dice = [1, 2, 3, 4, 5, 6]
player_rolls = get_rolls()
dice_rolls = []

for number in range(player_rolls):
    dice_roll = (random.choice(dice))
    dice_rolls.append(dice_roll)
    print(f"Dice roll: {dice_roll}")

total = sum(dice_rolls)


# ● ┌ ─ ┐ │ └ ┘
dice_art = {
    1: ("""
        ┌─────────┐
        │         │
        │    ●    │
        │         │
        └─────────┘
        """),
    2: ("""
        ┌─────────┐
        │  ●      │
        │         │
        │      ●  │
        └─────────┘
        """),
    3: ("""
        ┌─────────┐
        │  ●      │
        │    ●    │
        │      ●  │
        └─────────┘
        """),
    4: ("""
        ┌─────────┐
        │  ●   ●  │
        │         │
        │  ●   ●  │
        └─────────┘
        """),
    5: ("""
        ┌─────────┐
        │  ●   ●  │
        │    ●    │
        │  ●   ●  │
        └─────────┘
        """
        ),
    6: ("""
        ┌─────────┐
        │  ●   ●  │
        │  ●   ●  │
        │  ●   ●  │
        └─────────┘
        """)

}

for dice_roll in dice_rolls:
    dice_face = dice_art.get(dice_roll)
    print(dice_face)


print(f"Total roll: {total}")
