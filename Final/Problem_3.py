trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    usNumInt = int(us_num)
    if 0 <= usNumInt <= 10:
        mand_num = trans[us_num]
    elif 11 <= usNumInt <= 19:
        secondDigit = us_num[1]
        mand_num = trans['10'] + ' ' + trans[secondDigit]
    elif 20 <= usNumInt <= 99:
        firstDigit = trans[us_num[0]]
        secondDigit = trans['10']
        if usNumInt % 10 == 0:
            mand_num = ' '.join([firstDigit, secondDigit])
        else:
            thirdDigit = trans[us_num[1]]
            mand_num = ' '.join([firstDigit, secondDigit, thirdDigit])
    return mand_num

