class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        car=1
        for i in range(len(digits)-1,-1,-1):
            e=digits[i]
            if e+car>9:
                digits[i]=0
                car=1

            else:
                digits[i]=e+car
                car=0

                break

        if car:
            digits.insert(0, car)

        return digits



        