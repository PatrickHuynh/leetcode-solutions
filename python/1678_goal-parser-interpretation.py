# easy mode
# class Solution:
#     def interpret(self, command: str) -> str:
#         return command.replace("()","o").replace("(al)","al")

class Solution:
    def interpret(self, command: str) -> str:
        parse = ''
        counting = False
        count = 0
        for s in command:
            if s == "(":
                counting = True
                
            if s == ")":
                counting = False
                if count == 1:
                    parse += "o"
                elif count == 3:
                    parse += "al"
                count = 0
            
            if s == "G":
                parse += "G"
                
            if counting:
                count += 1
        return parse