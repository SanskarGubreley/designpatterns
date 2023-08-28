from infoLogProcessor import *
from debugLogProcessor import *
from errorLogProcessor import *

obj = InfoLogProcessor(DebugLogProcessor(ErrorLogProcessor(None)))

obj.log(obj.ERROR, "exception happens")