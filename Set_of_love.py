
def love_meet(bob, alice):
    meeting = set()
    for loc in bob:
        for loc2 in alice:
            if loc == loc2:
                meeting.add(loc)
    return meeting

def affair_meet(bob, alice, silvester):
    bob_places = set(bob)
    alice_places = set(alice)
    silvester_places = set(silvester)
    
    # Find common places where Alice and Silvester go
    alice_silvester_meet = alice_places.intersection(silvester_places)
    
    # Exclude places where Bob goes
    safe_meet_places = alice_silvester_meet - bob_places
    
    return safe_meet_places



bob = ['XIV', 'XIX', 'XII', 'XVIII']
alice = ['XIV', 'X', 'XI', 'XII']
silver = ['XII', 'XX', 'II', 'XIV'] 
# meet = XII, XIV

print(affair_meet(bob, alice, silver))




'''
From Pyris, with love.
Once upon a time, in Paris, the city of romance, Bob and Alice met and fall in love with each other.

Love

Exercise 1
To fullfill their romance, they want to meet as much as possible. They share their daily paths among Paris districts to know where they can find each other at the same place.

As you know there is 20 districts in Paris:

{"Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ", "Ⅴ", "Ⅵ", "Ⅶ", "Ⅷ", "Ⅸ", "Ⅹ", "ⅩⅠ", "ⅩⅡ", "ⅩⅢ", "ⅩⅣ", "ⅩⅤ", "ⅩⅥ", "ⅩⅦ", "ⅩⅧ", "ⅩⅠⅩ", "ⅩⅩ"}
Code a function named love_meet taking bob and alice's daily paths as two lists and returning a set of the districts they both visit during the day.
'''