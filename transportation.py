# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 14:24:38 2018

@author: Rebecca
"""

def trans(dist, dcs, stores_vol):

    my_team_or_name = "rswood"
    result = []
    
    """
    dist: dictionary (dc, store): distance
    dcs: dictionary dc: (maximum volume, number of doors, number of drivers)
    stores_vol: store, volume needed
    """
    
    check = dcs.copy()
    used_stores = []
    store_dict = {}
    for i in stores_vol:
        store_dict[i[0]] = i[1]
    
    dist_pair = dist.keys()
    distance = []
    for i in dist_pair:
        distance.append(dist.get(i))
    
    # sorts (dc_id, store_id) by shortest distance
    distance, dist_pair = zip(*sorted(zip(distance, dist_pair)))
    
    # switches to (store_id, dc_id)
    dist_pairs = []
    for d in dist_pair:
        dist_pairs.append((d[1], d[0]))
    
    for i in dist_pairs:
        debate = i
        #print debate
        # store_id cannot already be used
        if debate[0] not in used_stores:
            # size of store_id cannot exceed size of dc_id
            if store_dict[debate[0]] <= check[debate[1]][0]:
                # number of times dc is used cannot exceed number of doors
                if dcs[debate[1]][1] > 0:
                    result.append(debate)
                    check[debate[1]] = (check[debate[1]][0] - store_dict[debate[0]], check[debate[1]][1] - 1, check[debate[1]][2] - 1)
                    used_stores.append(debate[0])
            
            
    return my_team_or_name, result