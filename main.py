from bs4 import BeautifulSoup

"""

这是使用 BeautifulSoup 美化HTML的一个小程序，很简单，请享用。

"""

if __name__ == '__main__':
    html_file1 = input('请输入要格式化（美化）的html文件路径及其名称：')
    html_file2 = input('输入格式化后输出的文件路径及其名称：')

    result = None

    with open(html_file1, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        result = soup.prettify()

    with open(html_file2, 'w', encoding='utf-8') as f:
        f.write(result)

    print('格式化完毕')
