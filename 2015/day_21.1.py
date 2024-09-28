weap = [[8,4],[10,5],[25,6],[40,7],[74,8]]
arm = [[0,0],[13,1],[31,2],[53,3],[75,4],[102,5]]
rin = [[0,0,0],[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3]]

player_points = 100
player_dam = 0
player_arm = 0
boss_points = 109
boss_dam = 8
boss_arm = 2

def fight():
    global player_points
    global player_dam
    global player_arm
    global boss_points
    global boss_dam
    global boss_arm
    while player_points > 0 or boss_points > 0:
        if (player_dam - boss_arm) > 1:
            boss_points -= (player_dam - boss_arm)
        else:
            boss_points -= 1

        if boss_points > 0:
            if (boss_dam - player_arm) > 1:
                player_points -= (boss_dam - player_arm)
            else:
                player_points -= 1

            if player_points <= 0:
                return 0

        else:
            return 1

gold_to_win = []
gold_to_lose = []
cost = 0
for weap_item in weap:
    cost += weap_item[0]
    player_dam += weap_item[1]
    for arm_item in arm:
        cost += arm_item[0]
        player_arm += arm_item[1]   
        for rin_item1 in rin:
            cost += rin_item1[0]
            player_dam += rin_item1[1]
            player_arm += rin_item1[2]
            new_rin = []
            new_rin = rin.copy()
            if rin_item1 != [0,0,0]:
                new_rin.remove(rin_item1)
            for rin_item2 in new_rin:
                cost += rin_item2[0]
                player_dam += rin_item2[1]
                player_arm += rin_item2[2]
                win = fight() 
                player_points = 100
                boss_points = 109
                
                if win == 1:
                    gold_to_win.append(cost) 
                elif win == 0:
                    gold_to_lose.append(cost)

                cost -= rin_item2[0]
                player_dam -= rin_item2[1]
                player_arm -= rin_item2[2]
            cost -= rin_item1[0]
            player_dam -= rin_item1[1]
            player_arm -= rin_item1[2]
        cost -= arm_item[0]
        player_arm -= arm_item[1] 
    cost -= weap_item[0]
    player_dam -= weap_item[1]    

print(min(gold_to_win))
