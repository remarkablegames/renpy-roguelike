label player_turn:

    if enemy.health <= 0:
        $ wins += 1
        hide placeholder boy with dissolve
        "You defeated the enemy!"
        jump combat

    if not player.energy:
        jump enemy_turn

    $ player.turn()

    menu:
        "Choose your action."

        "{color=#EE4B2B}Attack [player.attack]\n{color=#add8e6}Energy -1" if player.energy >= 1:
            $ player.energy -= 1
            $ enemy.health -= player.attack

            show placeholder boy at shake, center

            "You dealt [player.attack] damage to the enemy."

            jump player_turn

        "{color=#af0}Heal [player.heal]\n{color=#add8e6}Energy -2" if player.energy >= 2:
            $ player.energy -= 2
            $ player.apply_heal()

            "You healed [player.heal] health."

            jump player_turn

        "End Turn":
            jump enemy_turn
