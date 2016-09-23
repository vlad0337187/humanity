#! /usr/bin/python3
'''
Проверяет модуль humanity на различные ошибки.
Если знаем, что в самом методе проверки ошибка - используем 
декоратор @unittest.expectedFailure.
'''

import unittest
from humanity import *





def create_sequence(sequence, classname):  # чтобы несколько раз не писать
	'''Создает и возвращает объект нужно типа из входных данных последовательности
	и имени класса возвращаемого объекта.
	'''
	# a = (1,2,3) >>> str(a) >>> '(1, 2, 3)'
	if classname == 'humlist' or classname == 'humtuple':
		return eval("{0}{1}".format(classname, str(sequence)))
	elif classname == 'humstr':
		sequence = str(sequence).replace(', ', '')
		sequence = str(sequence).replace(' ', '')  # чтобы не было ошибки
		return eval("{0}{1}".format(classname, str(sequence)))





def sequence_test_slices_1(self):  # чтобы несколько раз не писать
	'''Весь вперед.'''
	self.assertEqual( self.i[1:9:1], create_sequence((1,2,3,4,5,6,7,8,9), self.classname) )

def sequence_test_slices_2(self):
	'''Часть вперед.'''
	self.assertEqual( self.i[2:4], create_sequence((2,3,4), self.classname) )

def sequence_test_slices_3(self):
	'''С середины до конца с выходом за правый край.'''
	self.assertEqual( self.i[2:100], create_sequence((2,3,4,5,6,7,8,9), self.classname) )

def sequence_test_slices_5(self):
	'''Срез. Выход за оба края.'''
	self.assertEqual( self.i[0:100], create_sequence((1,2,3,4,5,6,7,8,9), self.classname) )

def sequence_test_slices_6(self):
	'''Весь вперед с шагом.'''
	self.assertEqual( self.i[1:9:2], create_sequence((1,3,5,7,9), self.classname) )

def sequence_test_slices_7(self):
	'''Шаг равен нулю.'''
	with self.assertRaises(ValueError):
		self.i[1:9:0]

def sequence_test_slices_8(self):
	'''Обратный порядок.'''
	self.assertEqual( self.i[9:1:-1], create_sequence((9,8,7,6,5,4,3,2,1), self.classname) )

def sequence_test_slices_9(self):
	'''Обратный порядок. Другой шаг.'''
	self.assertEqual( self.i[9:1:-2], create_sequence((9,7,5,3,1), self.classname) )

def sequence_test_slices_10(self):
	'''Обратный порядок. Выход за левую границу.'''
	self.assertEqual( self.i[10:1:-2], create_sequence((9,7,5,3,1), self.classname) )

def sequence_test_slices_11(self):
	'''Обратный порядок. Выход за обе границы.'''
	self.assertEqual( self.i[10:0:-2], create_sequence((9,7,5,3,1), self.classname) )

def sequence_test_slices_12(self):
	'''Обратный порядок. Выход за обе границы. Другой шаг.'''
	self.assertEqual( self.i[10:0:-1], create_sequence((9,8,7,6,5,4,3,2,1), self.classname) )

def sequence_test_slices_13(self):
	'''Обратный порядок. Шаг равен нулю.'''
	with self.assertRaises(ValueError):
		self.i[9:1:0]

def sequence_test_slices_13(self):
	'''Обратный порядок. Шаг равен размеру массива.'''
	self.assertEqual( self.i[9:1:-9], create_sequence((9,), self.classname) )  # запятая для теста

def sequence_test_slices_14(self):
	'''Обратный порядок. Без шага.'''
	with self.assertRaises(IndexError):
		self.i[9:1:]
		
		
def sequence_test_classname(self):
	'''Имя класса проверяем.'''
	self.assertEqual( self.__class__, eval(self.classname) ) 





testclass_variants = 'list', 'tuple', 'str'
testclass = """
class Hum{0}Test(unittest.TestCase):
	classname = 'hum{0}'  # для того чтобы методы вынести
	
	def setUp(self):
		self.i = create_sequence((1,2,3,4,5,6,7,8,9), Hum{0}Test.classname)
	def tearDown(self):
		del self.i
	
	
	test_slices_1 = sequence_test_slices_1
	test_slices_2 = sequence_test_slices_2
	test_slices_3 = sequence_test_slices_3
	test_slices_5 = sequence_test_slices_5
	test_slices_6 = sequence_test_slices_6
	test_slices_7 = sequence_test_slices_7
	test_slices_8 = sequence_test_slices_8
	test_slices_9 = sequence_test_slices_9
	test_slices_10 = sequence_test_slices_10
	test_slices_11 = sequence_test_slices_11
	test_slices_12 = sequence_test_slices_12
	test_slices_13 = sequence_test_slices_13
	test_slices_14 = sequence_test_slices_14
	sequence_test_classname = sequence_test_classname
"""	
for variant in testclass_variants:  # чтобы несколько раз не писать
	exec(testclass.format(variant))  # создали несколько классов с одинаковыми проверками





class TestHumdict(unittest.TestCase):
	def setUp(self):
		self.i = humdict({'df':'3242345'})
	def tearDown(self):
		del self.i
	
	
	def test_get_1(self):
		self.assertEqual( self.i['df'], '3242345' )
		
	def test_assign_2(self):
		def test_func():
			self.i['333'] = 444
			return self.i['333']
		self.assertEqual( test_func(), 444 )
		
	def test_classname(self):
		self.assertEqual( self.i.__class__, humdict )
	
	def test_get(self):
		self.assertEqual( self.i.get('4'), None )
		



unittest.main()
