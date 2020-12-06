"""
用 unittest 的测试用例全部换成用 pytest 执行
做法如下
"""

import pytest
import glob
import os

# 查找所有待执行的测试用例module
def find_modules_from_folder(folder):
    absolute_f = os.path.abspath(folder)
    md = glob.glob(os.path.join(absolute_f, "*.py"))
    return [f for f in md if os.path.isfile(f) and not f.endswith('__init__.py')]

if __name__ == '__main__':
    # 得出测试文件夹地址
    test_folder = os.path.join(os.path.dirname(__file__), 'tests')
    # 得出测试文件夹下的所有测试用例
    target_files = find_modules_from_folder(test_folder)
    # 直接运行所有的测试用例
    pytest.main([*target_files,'-v'])
    #然后在命令行下执行：python main.py