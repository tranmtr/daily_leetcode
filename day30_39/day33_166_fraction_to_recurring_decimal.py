class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        flag = True
        if numerator < 0 and denominator > 0:
            numerator = -numerator
            flag = False
        elif numerator > 0 and denominator < 0:
            denominator = -denominator
            flag = False
        quotient_before_dot = str(numerator // denominator)
        quotient_after_dot = []
        remainder_dict = {}
        current_remainder = numerator % denominator

        i = 0
        while current_remainder:
            if (current_remainder not in remainder_dict):
                remainder_dict[current_remainder] = i
            else:
                j = remainder_dict[current_remainder]
                not_loop = "".join(quotient_after_dot[0 : j])
                loop = "".join(quotient_after_dot[j : i])
                result = quotient_before_dot + "." + not_loop + "(" + loop + ")"
                if flag:
                    return result
                else:
                    return "-" + result
            numerator = current_remainder * 10
            quotient_after_dot.append(str(numerator // denominator))
            current_remainder = numerator % denominator
            i += 1
        
        if (i == 0):
            if flag:
                return quotient_before_dot
            else:
                return "-" + quotient_before_dot
        not_loop = "".join(quotient_after_dot[0 : i])
        result = quotient_before_dot + "." + not_loop
        if flag:
            return result
        else:
            return "-" + result