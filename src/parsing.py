# import re

# test = open("test/inputAcc.js", "r")
# teks = test.read()

# symbol = [
# '\\\\',
# '\[',
# '\]', 
# '\^',
# '\.',
# '\|',
# '\?',
# '\*',
# '\+',
# '\{',
# '\}',
# '\(',
# '\)',
# '\;',
# '\<',
# '\>',
# '\,',
# '\"',
# "\'",
# '\-',
# '\=',
# '\=',
# '\!',
# '\#',
# '/'
# ]

# splitted = teks.split()

# # print(splitted)
# # for i in splitted :
# #     print(i)

# for simbol in symbol :
#     result = []
#     for word in splitted :
#         temp = re.split(r"[A-z]*(" + simbol + r")[A-z]*", word)
#         print(temp)
#         for i in temp :
#             if i != '' :
#                 result.append(i)
#     # print(result)
#     splitted = result


# print(result)


# # list = []
# # # print(hasil)
# # for i in hasil :
# #     x = i.split()
# #     for j in x :
# #         list.append(j)

# # print(hasil)

# # for i in list :
# #     for j in range(len(token)) :
# #         if (token[j][0]) == i : 
# #             hasil.append(token[j][1])
# # print(list)
# # print(" ".join(hasil))

# # def, anjay, '(', ')'

from CFG2CNF import *


# f.write(str(CFG_to_CNF(read_grammar("D://ITB 21//KULYAHHH//SEMESTER 3//TBFO//Tubes TBFO - JS Parser//TBFO_JSParser//src//Context_Free_Grammar.txt"))))
# CFG = ast.literal_eval(str(read_grammar("D://ITB 21//KULYAHHH//SEMESTER 3//TBFO//Tubes TBFO - JS Parser//TBFO_JSParser//src//Context_Free_Grammar.txt")))
CFG = read_grammar("D://ITB 21//KULYAHHH//SEMESTER 3//TBFO//Tubes TBFO - JS Parser//TBFO_JSParser//src//Context_Free_Grammar.txt")

newStart = {"START" : [['S']]}
CFG = {**newStart, **CFG}


list_RHS = list(CFG.values())
list_LHS = list(CFG.keys())
list_Rules = list(CFG.items())

epsilonProduct = {}



for i in range(len(list_RHS)) :
    product = list_RHS[i]
    for RHS in product :
        if 'Îµ' in RHS :
        # if 'PARAM ' in RHS :
            epsilonProduct.update({list_Rules[i][0] : list_Rules[i][1]})
            break

for i in list(epsilonProduct.items()) :
    print(i)
    print("\n")
