import warnings

def api_call_v2():
	warnings.warn('use v3 of this api', DeprecationWarning)
	return 200

with deprecated_call():
	assert api_call_v2() == 200