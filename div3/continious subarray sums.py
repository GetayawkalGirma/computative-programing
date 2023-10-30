        n=(len(nums))
        currsums=0
        hashmap=Counter({0:-1})
        for index in range(n):
            currsums+=nums[index]
            modulus=currsums%k
            if modulus in hashmap and index-hashmap[modulus]>1:
                return True
            elif modulus not in hashmap:
                hashmap[modulus]=index
        return False
