class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="aeiouAEIOU"
        map={}
        positions={}
        l=0
        result=""
        i=0
        list=[]
        for letter in s:
            if letter in vowels:
                map[l+1]=letter
                positions[l+1]=i
                result+=(str)(l+1)
                list.append((str)(l+1))
                l+=1
            else:
                result+=letter
                list.append(letter)
            i+=1

        i=0
        for i in range((int)((l+1)/2)):
            it=i+1
            a=map[it]
            b=map[l-it+1]

            p1=positions[it]
            p2=positions[l-it+1]

            list[p1]=b
            list[p2]=a

        return "".join(list)