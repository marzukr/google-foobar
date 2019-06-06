#You probably have python 3

import base64

MESSAGE = '''
FkYBDxYIFx4SVVpPS1UKExcbAUxeTUYRFRkHFwwGBx9SS0hNRhcJAQ4XAAQWXVlLVQgHFBUHHwFK QUhaUgIcDhMXHhwJHghGXlpSChEFCBcMEAYXAxVVWk9LVRgPHhUWABcJRl5aUhkTDwMbDgZMUldB VQkUDRdKTVJdEwQdSkFIWlIcGwNAVQc=
'''

KEY = 'marzukr'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))