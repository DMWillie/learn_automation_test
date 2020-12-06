
import os
import unittest
from APITestFramework.common.html_reporter import GenerateReport

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover(os.path.join
                (os.path.dirname(__file__),"tests"),pattern="*.py",top_level_dir=os.path.dirname(__file__))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
    # 应用HtmlTestRunner生成测试报告
    html_report = GenerateReport()
    html_report.generate_report(suite)