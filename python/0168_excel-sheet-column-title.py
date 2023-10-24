class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        vals = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'       
        column_title = ''
        col = columnNumber

        tier = 1
        tier_width = 26 ** tier
        tier_min = 0
        tier_max = tier_width
        while tier_min < columnNumber:
            mod = int(-(-(((float(columnNumber - tier_min) % tier_width )/ tier_width * 26) % 26)//1))% 26 # this is the secret to this problem
            column_title = vals[mod] + column_title
            tier_min += tier_width
            tier += 1
            tier_width = 26 ** tier
            tier_max += tier_width
        return column_title



