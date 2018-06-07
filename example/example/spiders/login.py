# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['example.webscraping.com']
    start_urls = [
        'http://example.webscraping.com/places/default/user/login?_next=%2Fplaces%2Fdefault%2Fview%2FChina-47#']
    login_url = 'http://example.webscraping.com/places/default/user/login?_next=%2Fplaces%2Fdefault%2Fview%2FChina-47#'

    def start_requests(self):
        yield Request(self.login_url, callback=self.login)

    def login(self, response):
        form_dict = {'email': '***', 'password': '12345'}
        yield FormRequest.from_response(response, formdata=form_dict, callback=self.parse_login)

    def parse_login(self, response):
        # 如果登录成功后，继续爬取start_urls中的页面
        if "Welcome" in response.text:
            yield from super().start_requests()

    def parse(self, response):
        pass

