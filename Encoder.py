list_ = [(0, 0, 0, 255), (255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255)]
Enc_str = ""


def encode(list_):
    dict1 ={1: 'I*@',
            2: 'hNy',
            3: '^9a',
            4: 'h8%',
            5: '6$D',
            6: 'oj#',
            7: '$fs',
            8: '?H2',
            9: 'p(5',
            0: '&tc'}

    for tup in list_:
        for num in tup:
            for char in str(num):
                print(dict1[int(char)],end="")
        #Enc_str.append()

encode(list_)


