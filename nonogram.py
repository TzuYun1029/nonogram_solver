# from itertools import combinations
import itertools

# initial
grid = input()
grid = tuple(int(x) for x in grid.split(" "))
row_num = grid[0]
col_num = grid[1]
map = [[2 for col in range(col_num)] for row in range(row_num)] # the last block records finish
# 存放所有可能
row_table = []
col_table = []

def main():
    # row_input = ((5,),(5,2),(4,4),(2,2,5),(4,1,2,2),(4,2,5),(5,1,6),(6,6),(2,8),(5,),(5,),(7,),(7,),(15,),(15,))
    # col_input = ((3,2),(5,2),(6,2),(2,5,2),(3,2,4),(4,8),(5,9),(2,1,7),(1,3,8),(3,9),(3,4,4),(3,4,2),(7,2),(4,2),(2,2))
    row_input = []
    col_input = []
    for i in range(row_num):
        a = input()
        a = tuple(int(x) for x in a.split(" "))
        row_input.append(a)
    for i in range(col_num):
        a = input()
        a = tuple(int(x) for x in a.split(" "))
        col_input.append(a)



    # 找出所有可能
    for index in range(row_num):
        row_table.append(find_all_combinations_from_input(row_input[index], row_num))
        # print(index)
        # print(row_table[index])
    for index in range(col_num):
        col_table.append(find_all_combinations_from_input(col_input[index], col_num))
        # print(index)
        # print(col_table[index])

    count = 0
    while(check_finish() != True):
        for index in range(row_num):
            find_sure_answer(index,1)
        for index in range(col_num):
            find_sure_answer(index,0)
        for index in range(row_num):
            delete_impossible(index,1)
        for index in range(col_num):
            delete_impossible(index,0)
        count += 1


        # if count % 5 == 0:
        #     for row in range(row_num):
        #         for col in range(col_num):
        #             if map[row][col] == 1:
        #                 if col == col_num - 1:
        #                     print("■")
        #                 else:
        #                     print("■ ", end = "")
                            
        #             else:
        #                 if col == col_num - 1:
        #                     print("□")
        #                 else:
        #                     print("□ ", end = "")
        #     print("==========================================")

    for row in range(row_num):
        for col in range(col_num):
            if map[row][col] == 1:
                if col == col_num - 1:
                    print("■")
                else:
                    print("■ ", end = "")
                    
            else:
                if col == col_num - 1:
                    print("□")
                else:
                    print("□ ", end = "")
                    
    

def check_finish():
    for row in range(row_num):
        for col in range(col_num):
            if map[row][col] == 2:
                return False
    return True




def find_all_combinations_from_input(input, grid):
    yes_num = 0
    for i in range(len(input)):
        yes_num = yes_num + input[i]
    space = grid - yes_num
    place_to_seperate = []
    for i in range(space + 1):
        place_to_seperate.append(i)
    seperation = len(input)
    comb = itertools.combinations(place_to_seperate, seperation)
    table_all_possible_set = []
    for i in list(comb):
        table_all_possible_set.append(trans_comb_to_yes_no(i, input, space))
    return table_all_possible_set
        

def trans_comb_to_yes_no(combination, input, space):
    to_print = []
    to_print.append(0)
    for i in range(len(input)):
        to_print.append(combination[i])
    to_print.append(space)
    # print(to_print)
    table = []
    for i in range(len(input) + 1):
        for x in range(to_print[i+1] - to_print[i]):
            table.append(0)
        if i < len(input):
            for o in range(input[i]):
                table.append(1)
    return table


def find_sure_answer(index, row):
    if row: #row
        #第幾個row
        for index in range(row_num):
            #row的第幾格(格數=col數)
            for i in range(col_num):
                row_ans_sum = 0
                #計算該格的所有可能的和
                for possible_set_index in range(len(row_table[index])):
                    row_ans_sum = row_ans_sum + row_table[index][possible_set_index][i]
                #把確定的答案填入map
                if row_ans_sum == 0:
                    map[index][i] = 0
                elif row_ans_sum == len(row_table[index]):
                    map[index][i] = 1
                # else:
                #     map[index][i] = 2
    else: #col
        #第幾個col
        for index in range(col_num):
            #col的第幾格(格數=row數)
            for i in range(row_num):
                col_ans_sum = 0
                #計算該格的所有可能的和
                for possible_set_index in range(len(col_table[index])):
                    col_ans_sum = col_ans_sum + col_table[index][possible_set_index][i]
                #把確定的答案填入map
                if col_ans_sum == 0:
                    map[i][index] = 0
                elif col_ans_sum == len(col_table[index]):
                    map[i][index] = 1
                # else:
                #     map[i][index] = 2

def delete_impossible(index, row):
    if row: #row 
        ok = []
        for possible_set_index in range(len(row_table[index])):
            for i in range(col_num):
                if map[index][i] != 2 and row_table[index][possible_set_index][i] != map[index][i]:
                    break
                elif i == col_num - 1:
                    ok.append(row_table[index][possible_set_index])
        row_table[index] = ok
    else: #col
        ok = []
        for possible_set_index in range(len(col_table[index])):
            for i in range(row_num):
                if map[i][index] != 2 and col_table[index][possible_set_index][i] != map[i][index]:
                    break
                elif i == row_num - 1:
                    ok.append(col_table[index][possible_set_index])
        col_table[index] = ok


if __name__ == '__main__':
    main()