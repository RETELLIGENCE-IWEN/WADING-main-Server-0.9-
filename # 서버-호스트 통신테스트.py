# 서버 호스팅

# 문법 간결화를 위해 'import socket' 대신 사용
from socket import *

# 동적 ip 주소 검색
def get_ipaddress():
  s = socket(AF_INET, SOCK_DGRAM)
  s.connect(("gmail.com",80)) # 모든 사이트 가능
  r = s.getsockname()[0]
  s.close()
  # 호스트 서버 IPv4 프로토콜 출력 및 리턴
  print('Server IP address : ', r)
  return (r)

# 클라이언트 에서 전송한 코드 연산
def code_trs(cin):
    cin = cin.decode()
    cin = cin.upper()
    if cin == 'TEST':
        return ('Success')
    elif cin != None:
        ret = ('Unidentified code'+ cin)
        return (ret)
    else:
        return('No input')
    


# 통신 포트 번호 : 12000
serverPort = 12001

#서버의 IP(학교 컴)
serverIP = get_ipaddress()


serverSocket = socket(AF_INET,SOCK_STREAM)

# 동적 IP주소
ipv4_add = get_ipaddress()

# 포트에 연결
serverSocket.bind((serverIP, serverPort))

# 포트로부터 수신
serverSocket.listen(1)
print('The server is ready to receive')
 
while (1):

    #소켓 연결 허용
    connectionSocket, addr = serverSocket.accept()
    print("accepted")

    # 클라이언트로부터 코드 수신
    sentence = connectionSocket.recv(1024)
    print(sentence)
    
    # 수신된 코드 연산
    capitalizedSentence = sentence
    
    # 연산 결과 전송
    connectionSocket.send(capitalizedSentence)
    print('Data Sent...')

