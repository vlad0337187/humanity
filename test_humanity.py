#! /usr/bin/python3
'''
Проверяет модуль humanity на различные ошибки.
Если знаем, что в самом методе проверки ошибка - используем 
декоратор @unittest.expectedFailure.

Revision: 3
'''




import unittest
from humanity import *








def create_sequence(sequence, classname):  # чтобы несколько раз не писать
	'''Создает и возвращает объект нужно типа из входных данных последовательности
	и имени класса возвращаемого объекта.
	'''
	# a = (1,2,3) >>> str(a) >>> '(1, 2, 3)'
	if classname == 'humlist' or classname == 'humtuple':
		return eval("{0}{1}".format(classname, str(sequence)))  # результат всегда в скобках
	elif classname == 'humstr':
		sequence = str(sequence).replace(', ', '')
		sequence = sequence.replace(' ', '')  # чтобы не было ошибки
		return eval("{0}{1}".format(classname, sequence))

def create_object(value, classname):
	if classname == 'humlist' or classname == 'humtuple':
		return value
	elif classname == 'humstr':
		return str(value)




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
	self.assertEqual( self.i.__class__, eval(self.classname) )
	
def sequence_test_get_1(self):
	'''Проверяем метод .get().'''
	self.assertEqual( self.i.get(3), create_object(3, self.classname) )
	
def sequence_test_get_2(self):
	'''Проверяем метод .get(). Выход за пределы.'''
	self.assertEqual( self.i.get(18), None )








testclass_variants = 'list', 'tuple', 'str'
testclass = """

class TestHum{0}(unittest.TestCase):
	classname = 'hum{0}'  # для того чтобы методы вынести
	
	def setUp(self):
		self.i = create_sequence((1,2,3,4,5,6,7,8,9), TestHum{0}.classname)
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
	test_classname = sequence_test_classname
	test_get_1 = sequence_test_get_1
	test_get_2 = sequence_test_get_2
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
		
	def test_get_2(self):
		self.assertEqual( self.i.get('df'), '3242345' )








class TestHumrange(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	
	
	def test_humrange_1(self):
		self.assertEqual( list(humrange(4, 4, 1)), [4] )
		
	def test_humrange_2(self):
		with self.assertRaises(ValueError):
			list(humrange(4, 4, -1))
	
	def test_humrange_3(self):
		self.assertEqual( list(humrange(4, 4)), [4] )
	
	def test_humrange_4(self):
		with self.assertRaises(ValueError):
			list(humrange(4, 4, 0))
	
	def test_humrange_5(self):
		self.assertEqual( list(humrange(4, 8)), [4, 5, 6, 7, 8] )
	
	def test_humrange_6(self):
		self.assertEqual( list(humrange(0, 2)), [0, 1, 2] )
	
	def test_humrange_7(self):
		with self.assertRaises(ValueError):
			list(humrange(4, 2))
	
	def test_humrange_8(self):
		self.assertEqual( list(humrange(4, 2, -1)), [4, 3, 2] )
	
	def test_humrange_9(self):
		self.assertEqual( list(humrange(4, 2, -2)), [4, 2] )
	
	def test_humrange_10(self):
		self.assertEqual( list(humrange(1, -1, -2)), [1, -1] )
	
	def test_humrange_11(self):
		self.assertEqual( list(humrange(1, -1, -1)), [1, 0, -1] )
	
	def test_humrange_12(self):
		with self.assertRaises(ValueError):
			list(humrange(4, 2, 1))
	
	def test_humrange_13(self):
		with self.assertRaises(ValueError):
			list(humrange(0))
	
	def test_humrange_14(self):
		self.assertEqual( list(humrange(1)), [1] )
	
	def test_humrange_15(self):
		self.assertEqual( list(humrange(2)), [1, 2] )




class TestHumfrange(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	
	
	def test_humfrange_1(self):
		self.assertEqual( list(humfrange(4, 4, 1)), [4] )
		
	def test_humfrange_2(self):
		with self.assertRaises(ValueError):
			list(humfrange(4, 4, -1))
	
	def test_humfrange_4(self):
		with self.assertRaises(ValueError):
			list(humrange(4, 4, 0))
	
	def test_humfrange_8(self):
		self.assertEqual( list(humfrange(4, 2, -1)), [4, 3, 2] )
	
	def test_humfrange_9(self):
		self.assertEqual( list(humfrange(4, 2, -2)), [4, 2] )
	
	def test_humfrange_10(self):
		self.assertEqual( list(humfrange(1, -1, -2)), [1, -1] )
	
	def test_humfrange_11(self):
		self.assertEqual( list(humfrange(1, -1, -1)), [1, 0, -1] )
	
	def test_humfrange_12(self):
		with self.assertRaises(ValueError):
			list(humfrange(4, 2, 1))
	
	def test_humfrange_13(self):
		self.assertEqual( list(humfrange(4, 3, -0.5)), [4, 3.5, 3] )
	
	def test_humfrange_14(self):
		self.assertEqual( list(humfrange(3, 4, 0.5)), [3, 3.5, 4] )
	
	def test_humfrange_15(self):
		with self.assertRaises(ValueError):
			list(humfrange(4, 3, 0.5))
	
	def test_humfrange_16(self):
		with self.assertRaises(ValueError):
			list(humfrange(3, 4, -0.5))

		



unittest.main()
