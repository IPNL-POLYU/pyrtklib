import os
if os.name == 'nt':
	from .Release.pyrtklib import *
else:
	from .pyrtklib import *