import json
import re
import base64

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7123124dfsdfsdfsdfsdf"

def generate_fingerprint(payload,key):
    payload_bytes = json.dumps(payload).encode('utf-8')
    base64_encoded = base64.encodebytes(payload_bytes) #OUTPUT : b''
    
    pad_left = key[0 : len(key)//2]
    pad_right = key[len(key)//2 : ]
    
    fingerprint = pad_left + str(base64_encoded) + pad_right
    
    return fingerprint


def decode_fingerprint(fingerprint, key):
    pad_length = len(key)//2
    if key[0:pad_length]!= fingerprint[0:pad_length]:
        raise Exception("Invalid  Key")
    
    pad_left = key[0 : len(key)//2]
    pad_right = key[len(key)//2 : ]
    
    fingerprint = re.sub(pad_left,"",fingerprint)
    fingerprint = re.sub(pad_right,"",fingerprint)
    
    decoded_bytes = eval(fingerprint)
    
    decoded_base64 = base64.decodebytes(decoded_bytes)
    
    payload = json.loads(decoded_base64.decode('utf-8'))
    
    return payload


data ={"Table":"Sports","Team1":"Barcelona","Team2":"RCB"}

#Encoding the dictionary
encoded_dict = generate_fingerprint(data,SECRET_KEY)
print(encoded_dict)

#Decoding the dictionary fingerprint
print(decode_fingerprint(encoded_dict,SECRET_KEY))