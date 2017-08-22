import pytest
class MyPlugin(object):
	"""docstring for MyPlugin"""
	def pytest_sessionfinish(self):
		print("*** test run reporting finishing")

pytest.main(["-qq"], plugins=[MyPlugin()])