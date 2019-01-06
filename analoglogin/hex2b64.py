class HB64(object):

    b64byte = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    b64cpt = "="

    def hex2b64(self, string):
        result = ""
        ptr = 0
        b1 = int("111111000000000000000000", 2)
        b2 = int("000000111111000000000000", 2)
        b3 = int("000000000000111111000000", 2)
        b4 = int("000000000000000000111111", 2)
        lenth = len(string)
        while ptr+6 <= lenth:
            temp = int(string[ptr:ptr+6], 16)
            result += self.b64byte[(temp & b1) >> 18] 
            result += self.b64byte[(temp & b2) >> 12]
            result += self.b64byte[(temp & b3) >> 6]
            result += self.b64byte[temp & b4]
            ptr += 6
        if lenth-ptr == 4:
            temp = int(string[ptr:ptr+4], 16) << 2
            result += self.b64byte[(temp & b2) >> 12]
            result += self.b64byte[(temp & b3) >> 6]
            result += self.b64byte[temp & b4]
            result += self.b64cpt
        elif lenth-ptr == 2:
            temp = int(string[ptr:ptr+2], 16) << 4
            result += self.b64byte[(temp & b3) >> 6]
            result += self.b64byte[temp & b4]
            result += self.b64cpt * 2
        elif lenth-ptr == 0:
            pass
        else:
            raise Exception
        return result

    def b642hex(self, string):
        result = ""
        ptr = 0
        lenth = len(string)
        b1 = int("111111110000000000000000", 2)
        b2 = int("000000001111111100000000", 2)
        b3 = int("000000000000000011111111", 2)
        while ptr+8 <= lenth:
                temp = string[ptr:ptr+4]
                temp_result = 0
                for cell in range(4):
                    temp_result += self.b64byte.index(temp[cell]) << (6 * (3 - cell))
                r1 = hex((temp_result & b1) >> 16)[2:]
                r2 = hex((temp_result & b2) >> 8)[2:]
                r3 = hex(temp_result & b3)[2:]
                if len(r1) == 1:
                    r1 = '0' + r1
                if len(r2) == 1:
                    r2 = '0' + r2
                if len(r3) == 1:
                    r3 = '0' + r3
                result += r1
                result += r2
                result += r3
                ptr += 4
        if string[-1]=="=" and string[-2]=="=":
            temp = string[ptr:ptr+2]
            temp_result = 0
            temp_result += self.b64byte.index(temp[0]) << 18
            temp_result += self.b64byte.index(temp[1] >> 4) << 12
            r1 = hex((temp_result & b1) >> 16)[2:]
            r2 = hex((temp_result & b2) >> 8)[2:]
            if len(r1) == 1:
                r1 = '0' + r1
            if len(r2) == 1:
                r2 = '0' + r2
            result += r1
            result += r2

        elif string[-1]=="=":
            temp = string[ptr:ptr+3]
            temp_result = 0
            for cell in range(2):
                temp_result += self.b64byte.index(temp[cell]) << (6 * (3 - cell))
            temp_result += self.b64byte.index(temp[2] >> 2) << 6
            r1 = hex((temp_result & b1) >> 16)[2:]
            r2 = hex((temp_result & b2) >> 8)[2:]
            r3 = hex(temp_result & b3)[2:]
            if len(r1) == 1:
                r1 = '0' + r1
            if len(r2) == 1:
                r2 = '0' + r2
            if len(r3) == 1:
                r3 = '0' + r3
            result += r1
            result += r2
            result += r3
        elif "=" not in string:
            temp = string[ptr:ptr+4]
            temp_result = 0
            for cell in range(4):
                temp_result += self.b64byte.index(temp[cell]) << (6 * (3 - cell))
            r1 = hex((temp_result & b1) >> 16)[2:]
            r2 = hex((temp_result & b2) >> 8)[2:]
            r3 = hex(temp_result & b3)[2:]
            if len(r1) == 1:
                r1 = '0' + r1
            if len(r2) == 1:
                r2 = '0' + r2
            if len(r3) == 1:
                r3 = '0' + r3
            result += r1
            result += r2
            result += r3
        else:
            raise Exception
        return result
if __name__ == "__main__":
    print(HB64().b642hex("AIWQuVkw1C4XWngusF1MJpi3nuXDIloAOeWm+WbKDY2UJM1c+JJdYMqqq9lmSrDrUPR6ay9iFwhLSsCALpa/HCSo5ACVX/oRNdQwzFgZ4NBP/nyLw8V39w+aVX4snSTXlCDwUnbt1Q0Ff3qYNFBJKyvHHLHm4tNGZqO7RNutCPlP"))
