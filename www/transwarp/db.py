#!/usr/bin/python
# _*_ coding:utf-8 _*
# db.py


#数据库引擎对象
class _Engine(object):
	def  __init__(self, connect):
		self._connect = connect
	def connect(self):
		return self.connect()

engine = None

# 持有数据库连接的上下文对象:
class _DbCtx(threading.local):
	def __init__(self):
		self.connection = None
		self.transactions = 0

	def is_init(self):
		return not self.connection is None

	def init(self):
		self.connection = _LasyConnection()
		self.transactions = 0

	def cleanup(self):
		self.connection.cleanup()
		self.connection = None

	def cursor(self):
		return self.connection.cursor()

_db_ctx = _DbCtx()


def _ConnectionCtx(object):
	def __enter__(self):
		global _db_ctx
		self.should_cleanup = False
		if not _db_ctx.is_init():
			_db_ctx.init()
			self.should_cleanup = True
		return self

