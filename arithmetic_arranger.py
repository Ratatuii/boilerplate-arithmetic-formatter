def arithmetic_arranger(problems, *args):
    arranged_problems = []
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for i in problems:
        a, b, c = i.split()
        if b not in '+-':
            return "Error: Operator must be '+' or '-'."

        if len(a) > 4 or len(c) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        max_len = max(len(a), len(c)) + 2
        try:
            a = int(a)
            c = int(c)
        except ValueError:
            return 'Error: Numbers must only contain digits.'

        output_1 = f'{a:>{max_len}}'
        output_2 = f'{b}{c:>{max_len - 1}}'
        output_3 = f'{"-" * max_len}'
        try:
            arranged_problems[0] += f'{" " * 4}{output_1}'
        except IndexError:
            arranged_problems.append(f'{output_1}')
        try:
            arranged_problems[1] += f'{" " * 4}{output_2}'
        except IndexError:
            arranged_problems.append(output_2)
        try:
            arranged_problems[2] += f'{" " * 4}{output_3}'
        except IndexError:
            arranged_problems.append(output_3)

        if args:
            output_4 = f'{(a + c) if b == "+" else (a - c):>{max_len}}'
            try:
                arranged_problems[3] += f'{" " * 4}{output_4}'
            except IndexError:
                arranged_problems.append(output_4)
    result = f'{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}'
    result = result + f'\n{arranged_problems[3]}' if args else result

    return result
