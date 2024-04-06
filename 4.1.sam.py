from time import sleep
class Warrior():
  #конструктор класса
  def __init__(self, name, health, armor):
    self.name = name
    self.health = health #число
    self.armor = armor #строка
  #печать параметров персонажа
  def print_info(self):
    print('-> НОВЫЙ ГЕРОЙ')
    print('Верхом на коне появился бравый воин по имени',self.name)
    print('Уровень здоровья:', self.health)
    print('Класс брони:', self.armor, '\n')
  def attac(self,enemy):

    print('Удар! храбрый воин ' + self.name + ' атакует ' + enemy.name +'мечом! страшный удар обрушился на противника''теперь его броня ',self.armor, 'а уровень здоровья:',self.health)
    if enemy.armor < 0:
       enemy.health += enemy.armor
       enemy.armor = 0
class Magican():
  #конструктор класса
  def __init__(self, name, health, armor):
    self.name = name
    self.health = health #число
    self.armor = armor #строка
  #печать параметров персонажа
  def print_info(self):
    print('-> НОВЫЙ ГЕРОЙ')
    print('откуда ни возмись появился искустный волшебник',self.name)
    print('Уровень здоровья:', self.health)
    print('Класс брони:', self.armor, '\n')
  def atac(self,enemy):
    print('Удар! ловкий маг ' + self.name + ' накладывает заклинание на ' +enemy.name +' сложное заклинание оглушило противника''теперь его броня ',self.armor, 'а уровень здоровья:',self.health)
    if enemy.armor < 0:
       enemy.health += enemy.armor
       enemy.armor = 0

Henry = Warrior('Henry', 100, 50)
Henry.print_info()
Luke = Magican('Luke', 50, 20)
Luke.print_info()
Henry.attac(Luke)
Luke.atac(Henry)