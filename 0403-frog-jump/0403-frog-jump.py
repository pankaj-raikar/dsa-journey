class Solution:
    def canCross(self, stones: list[int]) -> bool:
        target=stones[-1]
        
        stones_set=set(stones)

        memo={}

        def can_reach(position,last_jump):
            key=(position,last_jump)

            if key in memo:
                return memo[key]


            if position==target:
                memo[key]=True
                return True
            
            for next_jump in (last_jump-1,last_jump,last_jump+1):
                if next_jump > 0:
                    next_position=position+next_jump

                    if next_position in stones_set:
                        if can_reach(next_position,next_jump):
                            memo[key]=True
                            return True

            memo[key]=False

            return False

        return can_reach(0,0)