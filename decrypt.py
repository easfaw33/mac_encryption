import os, threading, queue
from os import system
from queue import Queue

#DECRYPT
def decrypt(key):
    file = q.get()
    print(f'Decrypting {file}')
    try:
        key_index = 0
        max_key_index = len(key) -1
        encrypted_data = ''
        with open(file, 'rb') as f:
            data = f.read()
        with open(file, 'w') as f:
            f.write('')
        for byte in data:
            xor_byte = byte ^ ord(key[key_index])
            with open(file, 'ab') as f:
                f.write(xor_byte.to_bytes(1, 'little'))
            if key_index >= max_key_index:
                key_index = 0
            else:
                key_index += 1
            print(f'{file} successfully decrypted')
    
    except:
        print(f'Faield to encrypt {file}')
    q.task_done()
#ENCYRPTION INFO
encryption_level = 512 // 8
key_char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[]#@></\?.,'
key_char_pool_len =  len(key_char_pool)
#PATHS
home = os.environ['HOME']
enc_path = home + '/Projects/mac_enc/test'
files = os.listdir(enc_path)
abs_files = []
for f in files:
    if os.path.isfile(f'{enc_path}/{f}') and f != __file__[:-2]+'txt':
        abs_files.append(f'{enc_path}/{f}')
#KEY
key = input(f'Input Decryption Key: ')
#QUEUE
q = queue.Queue()
for f in abs_files:
    q.put(f)
#THREADS
for i in range(10):
    t = threading.Thread(target=decrypt, args=(key,), daemon=True)
    t.start()
q.join()
input()
