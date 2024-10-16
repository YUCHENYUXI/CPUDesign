def process_input(input_text):
    # 将输入按行分割
    lines = input_text.split('\n')
    processed_lines = []

    for line in lines:
        # 对每一行中的每个字符用逗号分隔
        processed_line = ','.join(line)
        processed_lines.append(processed_line)

    # 将处理后的行重新组合成一个字符串，保留换行符
    result = '\n'.join(processed_lines)
    return result

# 示例输入
input_text = """000010011001000000001
000110000000000010000
001100000000000000011
100000000001000000100
000001000100000000000
001100000000000000110
100000000010000000000
001000000000001101000
000000100100000000000
011000000000101000000
011000000000011000000
001100000000000001100
000000000100000000000
100000000000001101101"""

# 处理输入
output_text = process_input(input_text)

# 输出结果
print(output_text)
