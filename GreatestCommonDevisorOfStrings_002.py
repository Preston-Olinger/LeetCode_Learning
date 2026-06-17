class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #find lenght of both strings
        len1 = len(str1)
        len2 = len(str2)
        print("Length of str1: ", len1),
        print("Length of str2: ", len2)

    
        #find the greatest common denominator

        gcd_len = math.gcd(len1, len2)
        print("gcd_len: ", gcd_len)

        #get first chunk from str1 and gcd_len
        str1_prefix = []
        i=0
        while i < gcd_len:
            str1_prefix.append(str1[i])
            i=i+1
        mashed_str1_prefix = ''.join(str1_prefix)
        print("mashed_str1_prefix: ",mashed_str1_prefix)

        str1_repeat_count = len(str1) // len(mashed_str1_prefix)
        str2_repeat_count = len(str2) // len(mashed_str1_prefix)

        rebuilt_str1 = mashed_str1_prefix * str1_repeat_count
        rebuilt_str2 = mashed_str1_prefix * str2_repeat_count

        if rebuilt_str1 == str1 and rebuilt_str2 == str2:
            final_output = mashed_str1_prefix
        else:
            final_output = ""

        return final_output
        
        

        return final_output
        

    

        
        