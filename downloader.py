import requests
import pyfiglet
import uuid

'''
#1 ฟังชั่นดาวน์โหลดคลิป
'''
def downloader(arg1):
    chunk_size = 256
    url = arg1
    r = requests.get(url, stream=True) if arg1 else False

    if r:
        with open(str(uuid.uuid4()) + '.mp4', 'wb') as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
    else:
        print('[!] Error: Link Not Found')
        exit()

'''
#2 แสดงผลแบนเนอร์
'''
def banner():
    ascii_banner = pyfiglet.figlet_format('Pynark Downloader')
    print(ascii_banner)
    print('///////////////////////////////////////////////////////\n')    
    print('github: https://github.com/pynark/pynark_downloader\n')
    print('///////////////////////////////////////////////////////\n')

'''
#3 เริ่มโปรแกรม
'''
def init():
    banner()
    #ตรวจสอบ
    is_requests()
    is_connect()

    uri_download = input('Input Link to download: ')
    if uri_download is not None:
        downloader(str(uri_download))
    else:
        print('Erors: Link Not Found')
        exit()

'''
#4 เชื่อมต่ออินเตอร์เน็ตหรือไม่
'''
def is_connect():
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
        requests.get("https://www.google.com",headers=headers)

    except Exception:
        print("You are not connected To Internet!!!")
        print("\tPlease Connect To Internet To Continue...\n")
        input('Exiting....\n Press Enter To Continue....')
        exit()

    return True

'''
#5 นำเข้า Requests library หรือไม่
'''
def is_requests():
    try:
        import requests
    except ImportError:
        print('[!] Error: some dependencies are not installed')
        print('Type \'pip install -r requirements.txt\' to install all required packages')
        exit()

    return True

'''
สารบัญ
#1 downloader
#2 banner
#3 initial
#4 Is connect to the internet?
#5 Is import requests
'''

#เรียกการใช้งาน
init()




