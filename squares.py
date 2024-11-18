import argparse

def average_of_squares(list_of_numbers, list_of_weights=None):
    """计算一个数字列表的加权平方平均值。"""
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)

def convert_numbers(list_of_strings):
    """将字符串列表转换为数字，忽略空白字符。"""
    all_numbers = []
    for s in list_of_strings:
        all_numbers.extend([token.strip() for token in s.split()])
    return [float(number_string) for number_string in all_numbers]

if __name__ == "__main__":
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description="计算一组数字的加权平方平均值")
    parser.add_argument("numbers", type=float, nargs="+", help="输入的数字列表")

    # 解析命令行参数
    args = parser.parse_args()
    numbers = args.numbers  # 获取输入的数字

    # 使用硬编码的 weights = None
    result = average_of_squares(numbers)

    # 打印结果
    print(result)
