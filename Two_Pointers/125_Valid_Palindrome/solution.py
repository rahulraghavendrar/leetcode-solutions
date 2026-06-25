class Solution(object):
    def isPalindrome(self, s):
        newstr=''

        for i in range(len(s)):
            if s[i].isalnum()==True:
                newstr+=s[i].lower()

        l,r=0,len(newstr)-1

        if len(newstr)==0:
            return True

        while l<r:

            if newstr[l]!=newstr[r]:
                return False

            l=l+1
            r=r-1

        return True