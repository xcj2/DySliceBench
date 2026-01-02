
        
        
class Building:
    def __init__(self,max_floor,max_room):
        self.max_floor=max_floor
        self.max_room=max_room
        #[floor][room]で管理
        row=max_floor
        col=max_room
        self.room_info=[[0 for j in range(col)] for i in range(row)]
        
    def update_visited(self,f,r,v):
        self.room_info[f][r]+=v
        

class OfficialHouse:
    def __init__(self,max_building=4,max_floor=3,max_room=10):
        self.buildings=[]
        for building_id in range(max_building):
            self.buildings.append(Building(max_floor=max_floor,max_room=max_room))
            
    def update_visited(self,notice):
        
        #indexずれの修正
        b=notice.building_id-1
        f=notice.floor-1
        r=notice.room_number-1
        v=notice.visited_number
        self.buildings[b].update_visited(f,r,v)
        

    def print_official_house_info(self):
        b_max=len(self.buildings)
        f_max=self.buildings[0].max_floor
        r_max=self.buildings[0].max_room
        
        for b in range(b_max):
            for f in range(f_max):
                for r in range(r_max):
                    v=self.buildings[b].room_info[f][r]
                    print(f" {v}",end="")
                print("")
            if b != b_max-1:
                print("####################")
        

class Notice:
    def __init__(self,building_id,floor,room_number,visited_number):
        self.building_id=building_id
        self.floor=floor
        self.room_number=room_number
        self.visited_number=visited_number


def tell_notice(notice_list,house):
    for notice in notice_list:
        house.update_visited(notice)


def input_notice():
    n=int(input())
    
    notice_list=[]
    
    for i in range(n):
        b,f,r,v=tuple(map(int,input().split()))
    
        notice=Notice(building_id=b,floor=f,room_number=r,visited_number=v)
        
        notice_list.append(notice)

        
    return notice_list
    
    
def exe_notice():
    notice_ls=input_notice()
    
    house=OfficialHouse()
    
    tell_notice(notice_ls,house)
    
    house.print_official_house_info()



exe_notice()
