#!/usr/bin/env python3
import math

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    #self.quantity = 1

  #@property
  #def quantity(self):
   # """return quantity property"""
    #return self._quantity
  
  #@quantity.setter
  #def quantity(self, quantity):
   # """quantity setter method"""
    #if isinstance(quantity, (int, float)):
     # self._qauntity = math.ceil(quantity)

  @property
  def discount(self):
    """return the discount property"""
    return self._discount
  
  @discount.setter
  def discount(self, discount):
    """discount setter method"""
    self._discount = discount

  def add_item(self, title, price, quantity = 1):
    self.quantity = math.ceil(quantity)
    self.total += price * self.quantity
    self.last_tansaction = [title, price, quantity]
    for i in range(quantity):
      self.items.append(title)
  
  def apply_discount(self, discount = 200):
    self.total -= discount
    if self.total <= 0:
      print('There is no discount to apply.')
    else:
      print(f'After the discount, the total comes to ${self.total}.')

  def void_last_transaction(self):
    self.total -= (self.last_tansaction[1]*self.last_tansaction[2])
