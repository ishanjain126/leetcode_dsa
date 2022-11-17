class Solution:
    def checkRecord(self, s: str) -> bool:
        att_arr = [*s]
        absent = 0
        cons_late = 0
        prev_counter = ""
        for i in att_arr:
            if i == "A":
                absent += 1
                cons_late = 0
            elif i == "L":
                cons_late += 1
            else:
                cons_late = 0
            if (absent > 1 or cons_late >= 3):
                return False
        return True
            
