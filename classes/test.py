class Poly1:
    coeffs = []
    def __init__(self , coeffs):
        index = 0
        self.coeffs = []
        self.poly = ""
        self.degree = len(coeffs) - 1
        for coeff in coeffs:
            self.coeffs.append(coeff)
            string = "{}*x^{} + ".format(coeff , index)
            index += 1
            self.poly = string + self.poly
        
        self.poly = self.poly[:-2]
        
    
    def __repr__(self):
        return self.poly
    
    def __call__(self , value):
        index = 0
        result = 0
        added_coeffs = []
        print(self.coeffs)
        for coeff in self.coeffs:
            result = result + (coeff)*(value**index)
            index += 1
        return result

    def __add__(self, other):
        index = 0
        added_coeffs = []
        if len(self.coeffs) > len(other.coeffs):
            length = len(self.coeffs)
            while index < length:
                try:
                    added_coeffs.append(self.coeffs[index] + other.coeffs[index])
                    index += 1
                except:
                    added_coeffs.append(self.coeffs[index])
        else:
            length = len(other.coeffs)
            while index < length:
                try:
                    added_coeffs.append(self.coeffs[index] + other.coeffs[index])
                    index += 1
                except:
                    added_coeffs.append(other.coeffs[index])
        return Poly1(added_coeffs)

    def __sub__(self, other):
        index = 0
        subbed_coeffs = []
        if len(self.coeffs) > len(other.coeffs):
            length = len(self.coeffs)
            while index < length:
                try:
                    subbed_coeffs.append(self.coeffs[index] - other.coeffs[index])
                    index += 1
                except:
                    subbed_coeffs.append(self.coeffs[index])
        else:
            length = len(other.coeffs)
            while index < length:
                try:
                    subbed_coeffs.append(self.coeffs[index] - other.coeffs[index])
                    index += 1
                except:
                    subbed_coeffs.append(other.coeffs[index])
        return subbed_coeffs


Poly1([1,2,3])

p = Poly1([1,2,3])

p(2)