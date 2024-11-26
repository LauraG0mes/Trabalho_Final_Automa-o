import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

class HomePage:
  def __init__(self, driver):
     self._driver = driver
    
  def wait_load(self):
    elements = self._driver.find_elements(By.CSS_SELECTOR, ".smooth")
    while len(elements) > 0:
        elements = self._driver.find_elements(By.CSS_SELECTOR, ".smooth")
        sleep(0.5)

  def subscribe_student_discipline(self, student_id, discipline_id):
      self._driver.find_element(By.ID, "subscribe-student-id").click()
      self._driver.find_element(By.ID, "subscribe-student-id").clear()
      self._driver.find_element(By.ID, "subscribe-student-id").send_keys(student_id)
      self._driver.find_element(By.ID, "subscribe-discipline-id").click()
      self._driver.find_element(By.ID, "subscribe-discipline-id").send_keys(discipline_id)
      self._driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(6) > #course-btn").click()

  def add_discipline(self, discipline):
      self._driver.find_element(By.ID, "discipline-nome").click()
      self._driver.find_element(By.ID, "discipline-nome").send_keys(discipline)
      self._driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn").click()

  def add_course(self, course):
      self._driver.find_element(By.ID, "course-nome").click()
      element = self._driver.find_element(By.ID, "course-nome")
      actions = ActionChains(self._driver)
      actions.double_click(element).perform()
      self._driver.find_element(By.ID, "course-nome").send_keys(course)
      self._driver.find_element(By.ID, "course-btn").click()

  def sub_dicipline_to_course(self):
      self._driver.find_element(By.ID, "discipline-nome").click()
      self._driver.find_element(By.ID, "discipline-nome").send_keys("mat")
      self._driver.find_element(By.ID, "course-discipline-id").click()
      self._driver.find_element(By.ID, "course-discipline-id").send_keys("1")
      self._driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn").click()

  def add_student_to_course(self):
      self._driver.find_element(By.ID, "student-id").click()
      self._driver.find_element(By.ID, "student-id").send_keys("1")
      self._driver.find_element(By.ID, "course-id").click()
      self._driver.find_element(By.ID, "course-id").send_keys("1")
      self._driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #course-btn").click()

  def add_student(self, student):
      self._driver.find_element(By.ID, "student-nome").click()
      self._driver.find_element(By.ID, "student-nome").send_keys(student)
      self._driver.find_element(By.ID, "student-btn").click()