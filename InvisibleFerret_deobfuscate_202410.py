# Uage: Paste obfuscated bytearray 
# Example 
# _ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'==AjX1mCf....'))
# In this example, bytearray is ==AjX1mCf...

import zlib
import base64
import re

obfuscated_script = b'<Paste obfuscated bytearray>'

def deobfuscate(data, cnt):
    try:
        decoded_data = base64.b64decode(data[::-1])
        decompressed_data = zlib.decompress(decoded_data)
        if cnt == 50:
            print(decompressed_data.decode('utf-8'))
            return None
        else: 
            match = re.search(r"b'(.*?)'", decompressed_data.decode('utf-8'))
            decompressed_data = match.group(1).encode()
            return decompressed_data
    except Exception as e:
        print(f"Deobfuscation error: {e}")

        return None

current_script = obfuscated_script
iterations = 0

while True:
    iterations += 1
    result = deobfuscate(current_script, iterations)
    
    if result is None:
        #print("Final script reached or an error occurred.")
        break
    else:
        current_script = result

