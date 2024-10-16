import sys

def process_input():
    input_text = sys.stdin.read()
    lines = input_text.split('\n')
    processed_lines = []

    for line in lines:
        # 将每一行的字符顺序左右互换
        reversed_line = line[::-1]
        # 对每一行中的每个字符用逗号分隔
        processed_line = ','.join(reversed_line)
        processed_lines.append(processed_line)

    # 将处理后的行重新组合成一个字符串，保留换行符
    result = '\n'.join(processed_lines)
    print(result)

# 运行处理函数
if __name__ == "__main__":
    process_input()
