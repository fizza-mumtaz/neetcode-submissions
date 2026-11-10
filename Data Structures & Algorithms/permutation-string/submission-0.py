
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count1 = {}
        count2 = {}

        for i in range(len(s1)):

            char1 = s1[i]
            char2 = s2[i]

            count1[char1] = count1.get(char1, 0) + 1
            count2[char2] = count2.get(char2, 0) + 1

        if count1 == count2:
            return True

        left = 0

        for right in range(len(s1), len(s2)):

            old_char = s2[left]
            count2[old_char] -= 1

            if count2[old_char] == 0:
                del count2[old_char]

            new_char = s2[right]
            count2[new_char] = count2.get(new_char, 0) + 1

            left += 1

            if count1 == count2:
                return True

        return False
