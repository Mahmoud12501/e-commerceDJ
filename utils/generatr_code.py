import random 

def generate_code(lenght=8):
    
    sample="123456789ABCDEFGHIJKLMNO"
    code= ''.join(random.choice(sample) for i in range(lenght))
    
    return code

def generate_code_orderes(lenght=8):
    
    sample="123456789M"
    code= ''.join(random.choice(sample) for i in range(lenght))
    
    return code