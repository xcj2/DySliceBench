def get_input():
    input_data = int(input())
    return input_data

def make_registered_id_set(N):
    registered_id_set = set()
    for i in range(N):
        registered_id = input()
        registered_id_set.add(registered_id)
    return registered_id_set

class SecurityDoor:
    CLOSED = 0
    OPENED = 1
    DUMMY = -1
    def __init__(self, registered_id_set):
        self.flag = SecurityDoor.CLOSED
        self.registered_id_set = registered_id_set

    def check_id(self, user_id):
        if user_id in self.registered_id_set:
            msg = self.change_status() + user_id
        else:
            msg = "Unknown " + user_id
        print(msg)

    def change_status(self):
        if self.flag == SecurityDoor.OPENED:
            self.flag = SecurityDoor.CLOSED
            msg = "Closed by "
        else:
            self.flag = SecurityDoor.OPENED
            msg = "Opened by "
        return msg



if __name__ == "__main__":
    N = get_input()
    registered_id_set = make_registered_id_set(N)
    touch_num = get_input()
    security_door = SecurityDoor(registered_id_set)
    for i in range(touch_num):
        user_id = input()
        security_door.check_id(user_id)


