import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.homepage import Homepage


def get_driver():
    geckodriver_path = GeckoDriverManager().install()
    service = FirefoxService(geckodriver_path)
    return webdriver.Firefox(service=service)


def before_all(context):
    context.homepage = Homepage(get_driver())


def after_all(context):
    context.homepage.close_page()
