#!/usr/bin/env python3

import sys
import csv
from collections import namedtuple

IncomeTaxQuickLookupItem = namedtuple(
    'IncomeTaxQuickLookupItem',
    ['start_point', 'tax_rate', 'quick_subtractor']
)

INCOME_TAX_START_POINT = 5000

INCOME_TAX_QUICK_LOOKUP_TABLE = [
    IncomeTaxQuickLookupItem(80000, 0.45, 15160),
    IncomeTaxQuickLookupItem(55000, 0.35, 7160),
    IncomeTaxQuickLookupItem(35000, 0.30, 4410),
    IncomeTaxQuickLookupItem(25000, 0.25, 2660),
    IncomeTaxQuickLookupItem(12000, 0.2, 1410),
    IncomeTaxQuickLookupItem(3000, 0.1, 210),
    IncomeTaxQuickLookupItem(0, 0.03, 0)
]

#config
class Args(object):
	def __init__(self):
		self._args = sys.argv[1:]

	def get_filename(self,value):
		index = self._args.index(value)
		return self._args[index + 1]

	@property
	def config_path(self):
		return self.get_filename('-c')
	@property
	def userdate_path(self):
		return self.get_filename('-d')
	@property
	def output_path(self):
		return self.get_filename('-o')

args = Args()

class Config(object):
	def __init__(self):
		self._config = self._read_config()

	def _read_config(self):
		config = {}
		with open(args.config_path) as file:
			for line in file.readlines():
				key,value = line.strip().split('=')
				config[key.strip()] = float(value.strip())
		return config

	def _get_config(self,key):
		return self._config[key]

	@property
	def social_insurance_baseline_low(self):
		return self._get_config('JiShuL')

	@property
	def social_insurance_baseline_high(self):
		return self._get_config('JiShuH')

	@property
	def social_insurance_total_rate(self):
		return sum([
        	self._get_config('YangLao'),
        	self._get_config('YiLiao'),
        	self._get_config('ShiYe'),
        	self._get_config('GongShang'),
        	self._get_config('ShengYu'),
        	self._get_config('GongJiJin')
        	])

config = Config()

class UserData(object):
	def __init__(self):
		self.userdata = self._read_users_data()

	def _read_users_data(self):
		userdata = []
		with open(args.userdate_path) as file:
			for line in file.readlines():
				eid,income = line.strip().split(',')
				int_income = int(income)
				userdata.append((eid,int_income))
			return userdata

	def _get_user_data(self):
		return self.userdata

class IncomeTaxCalculator(object):
	def __init__(self,userdata):
		self.userdata = userdata

	@classmethod
	def calc_social_insurance_money(cls, income):
		if income < config.social_insurance_baseline_low:
			return config.social_insurance_baseline_low * \
			config.social_insurance_total_rate
		elif income > config.social_insurance_baseline_high:
			return config.social_insurance_baseline_high * \
			config.social_insurance_total_rate
		else:
			return income * config.social_insurance_total_rate

	@classmethod
	def calc_income_tax_and_remain(cls, income):
		social_insurance_money = cls.calc_social_insurance_money(income)
		real_income = income - social_insurance_money
		taxable_part = real_income - INCOME_TAX_START_POINT

		for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
			if taxable_part > item.start_point:
				tax = taxable_part * item.tax_rate - item.quick_subtractor
				return '{:.2f}'.format(tax), '{:.2f}'.format(real_income - tax)

		return '0.00', '{:.2f}'.format(real_income)

	def calc_for_all_userdata(self):
		result = []
		for eid, income in self.userdata._get_user_data():
			social_insurance_money = '{:.2f}'.format(self.calc_social_insurance_money(income))
			tax, remain = self.calc_income_tax_and_remain(income)
			result.append([eid, income, social_insurance_money, tax, remain])
		return result

	def export(self):
		result = self.calc_for_all_userdata()

		with open(args.output_path, 'w', newline='') as file:
			writer = csv.writer(file)
			writer.writerows(result)

if __name__ == '__main__':
	#print(args.config_path)
	#print(args.userdate_path)
	#userdata = UserData()
	#print(userdata._get_user_data())
	incometaxcalulator = IncomeTaxCalculator(UserData())
	incometaxcalulator.export()
