# Part 2: Byzantine Generals

My implementation of the Byzantine General Problem does not quite follow the algorithm provided in the paper provided (Leslie Lamport, et al) as that provides a recursive solution, while mine is iterative. The recursive depth variable “m” is then used as the number of voting rounds.

The algorithm starts by assigning generals the status of being either a traitor or loyal to the Byzantine army. The commander then gives their order to each of the lieutenant generals. These generals then send their received order to every other lieutenant general. They then sum the orders they received and choose the one with the greatest count. A vote is then made on the final decision.

To test this algorithm, statistics for multiple runs of the algorithm were collected and then dumped by the console. These statistics measured the success rate of reaching the correct consensus provided that the general is loyal.

### Sample output for ten runs:

    Commander's order: ATTACK
    factions:  LOYAL LOYAL TRAITOR LOYAL LOYAL LOYAL TRAITOR
    votes:  ATTACK ATTACK ATTACK ATTACK ATTACK ATTACK ATTACK
    Commander status: LOYAL
    Overall consensus: ATTACK at dawn!
    ==================================================
    Commander's order: ATTACK
    factions:  LOYAL LOYAL LOYAL LOYAL TRAITOR LOYAL TRAITOR
    votes:  ATTACK ATTACK ATTACK ATTACK ATTACK ATTACK ATTACK
    Commander status: LOYAL
    Overall consensus: ATTACK at dawn!
    ==================================================
    Commander's order: RETREAT
    factions:  LOYAL LOYAL LOYAL TRAITOR TRAITOR LOYAL LOYAL
    votes:  RETREAT RETREAT RETREAT RETREAT RETREAT RETREAT RETREAT
    Commander status: LOYAL
    Overall consensus: RETREAT at dawn!
    ==================================================
    Commander's order: RETREAT
    factions:  TRAITOR TRAITOR LOYAL LOYAL LOYAL LOYAL LOYAL
    votes:  RETREAT ATTACK ATTACK ATTACK ATTACK ATTACK ATTACK
    Commander status: TRAITOR
    Overall consensus: ATTACK at dawn!
    ==================================================
    Commander's order: ATTACK
    factions:  LOYAL TRAITOR LOYAL TRAITOR LOYAL LOYAL LOYAL
    votes:  ATTACK ATTACK ATTACK ATTACK ATTACK ATTACK ATTACK
    Commander status: LOYAL
    Overall consensus: ATTACK at dawn!
    ==================================================
    Commander's order: RETREAT
    factions:  LOYAL TRAITOR LOYAL LOYAL LOYAL LOYAL TRAITOR
    votes:  RETREAT RETREAT RETREAT RETREAT RETREAT RETREAT RETREAT
    Commander status: LOYAL
    Overall consensus: RETREAT at dawn!
    ==================================================
    Commander's order: ATTACK
    factions:  LOYAL TRAITOR LOYAL LOYAL LOYAL LOYAL TRAITOR
    votes:  ATTACK ATTACK ATTACK ATTACK ATTACK ATTACK ATTACK
    Commander status: LOYAL
    Overall consensus: ATTACK at dawn!
    ==================================================
    Commander's order: ATTACK
    factions:  LOYAL LOYAL LOYAL TRAITOR TRAITOR LOYAL LOYAL
    votes:  ATTACK ATTACK ATTACK ATTACK ATTACK ATTACK ATTACK
    Commander status: LOYAL
    Overall consensus: ATTACK at dawn!
    ==================================================
    Commander's order: RETREAT
    factions:  LOYAL LOYAL LOYAL LOYAL TRAITOR LOYAL TRAITOR
    votes:  RETREAT RETREAT RETREAT RETREAT RETREAT RETREAT RETREAT
    Commander status: LOYAL
    Overall consensus: RETREAT at dawn!
    ==================================================
    Commander's order: ATTACK
    factions:  LOYAL TRAITOR LOYAL LOYAL LOYAL TRAITOR LOYAL
    votes:  ATTACK ATTACK ATTACK ATTACK ATTACK ATTACK ATTACK
    Commander status: LOYAL
    Overall consensus: ATTACK at dawn!
    ==================================================
    9 / 9 of times loyal command was obeyed
