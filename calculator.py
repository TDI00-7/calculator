import argparse


def evaluate(expr):
    ops = []
    for expr_lst in expr:
        ops.append(expr_lst)
       # print(ops)
        if len(ops) == 3:
            oper = ops.pop()
           # print(ops)
            ops2 = int(ops.pop())
            #print(ops)
            ops1 = int(ops.pop())
            #print(ops)

            results= 0

            if oper == "+":
                results= ops1 + ops2
            elif oper == "-":
                results= ops1 - ops2
            elif oper == "*":
                results= ops1 * ops2
            elif oper == "/":
                if ops == 0:
                    print("Error, Cant devide by zero. Dumbass")
                    exit()
                results= ops1 / ops2
            # print(results)
            ops.append(results)
    print(ops[0])


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--expr", nargs="+", default=[])
    args = parser.parse_args()
    evaluate(args.expr)


if __name__ == '__main__':
    main()