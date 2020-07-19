class Solution:
    def isHappy(self, n: int) -> bool:
        st={n}
        sm=0
        while(n!=1 and sm!=1):
            sm=0
            for x in str(n):
                d=int(x)
                sm+=d*d
            if(sm in st):
                return False
            else:
                st.add(sm)
                n=sm
        
        return True
