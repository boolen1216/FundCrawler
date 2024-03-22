"""
通过基金网站的全部基金列表，获取到 初始的，需要爬取的基金任务
"""
import re
from typing import NoReturn

import requests

from process_manager import NeedCrawledFundModule


class GetNeedCrawledFundByWeb(NeedCrawledFundModule):

    def init_generator(self) -> NoReturn:
        # 全部（不一定可购） 的开放式基金
        url = 'http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?page=1,&onlySale=0'
        page = requests.get(url, headers={
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/78.0.3904.108 Safari/537.36'})

        # 基金目录
        fund_pairs = re.findall(r'"[0-9]{6}",".+?"', page.text)

        # # 万家基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '万家' in pair]

        # # 中欧基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '中欧' in pair]

        # # 交银基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '交银' in pair]

        # # 华安基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '华安' in pair]

        # # 嘉实基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '嘉实' in pair]

        # # 富国基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '富国' in pair]

        # # 国富基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '国富' in pair]

        # # 大成基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '大成' in pair]

        # # 兴全基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '兴全' in pair]

        # # 景顺长城基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '景顺长城' in pair]

        # # 华夏基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '华夏' in pair]

        # # 广发基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '广发' in pair]

        # # 工银基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '工银' in pair]

        # # 安信基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '安信' in pair]

        # # 华泰柏瑞基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '华泰柏瑞' in pair]

        # # 西部利得基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '西部利得' in pair]

        # # 易方达基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '易方达' in pair]

        # # 汇添富基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '汇添富' in pair]

        # # 中信建投基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '中信建投' in pair]

        # # 博时基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '博时' in pair]

        # # 华宝基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '华宝' in pair]

        # # 前海基金；
        # fund_list = [pair for pair in fund_pairs if '混合' in pair and '前海' in pair]

        # 南方基金；
        fund_list = [pair for pair in fund_pairs if '混合' in pair and '南方' in pair]

        self.total = len(fund_list)
        self.task_generator = (NeedCrawledFundModule.NeedCrawledOnceFund(i[1:7], i[10:-1]) for i in fund_list)


class GetNeedCrawledFundByWeb4Test(NeedCrawledFundModule):
    """
    测试用的 基金任务 提供者
    """
    test_case_num = 2

    def init_generator(self) -> NoReturn:
        # 全部（不一定可购） 的开放式基金
        url = f'http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?page=1,{self.test_case_num}&onlySale=0'
        page = requests.get(url, headers={
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/78.0.3904.108 Safari/537.36'})

        # 基金目录
        fund_list = re.findall(r'"[0-9]{6}",".+?"', page.text)
        self.total = len(fund_list)

        self.task_generator = (NeedCrawledFundModule.NeedCrawledOnceFund(i[1:7], i[10:-1]) for i in fund_list)


class GetSpecialNeedCrawledFund(NeedCrawledFundModule):
    """
    测试用的 基金任务 提供者
    """

    def init_generator(self) -> NoReturn:
        # 基金目录
        fund_list = ({'code': '007746', 'name': '华安现金润利'}, {'code': '020282', 'name': '益民优势安享混合C'})
        self.total = len(fund_list)

        self.task_generator = (NeedCrawledFundModule.NeedCrawledOnceFund(
            code=t['code'], name=t['name']) for t in fund_list)
