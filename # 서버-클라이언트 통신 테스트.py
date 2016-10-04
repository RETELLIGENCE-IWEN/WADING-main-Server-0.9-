# 서버-클라이언트 통신 테스트

import time
from socket import *

def get_ipaddress():
  s = socket(AF_INET, SOCK_DGRAM)
  s.connect(("gmail.com",80))
  r = s.getsockname()[0]
  s.close()
  print('Client IP address : ', r)
  return (r)

# 동적 ip 주소 
serverName = get_ipaddress()

# 통신 포트번호 : 12000
serverPort = 12000


clientSocket = socket(AF_INET, SOCK_STREAM)

# 포트 연결
while(1):
    
  while(1):
      try:
          print('Initializing...\n')
          clientSocket.connect((serverName, serverPort))
      except:
          print("connection denied")
          continue
      else:
          print("connected")
          break

  while(1):
    
    try:
      
      # 전송할 코드 입력
      sentence = input('Input Code: ')
      if sentence == 'quit':
        clientSocket.close()
        print('quiting')
        time.sleep(1)
        break

      # 코드 전송
      clientSocket.send(sentence.encode())

      # 서버로부터 받은 코드연산결과 저장
      modifiedSentence = clientSocket.recv(1024)

      # 출력
      print('From Server : ',modifiedSentence.decode())
      continue


    except:
      print('error')
      clientSocket.close()
      print('quiting')
      break
