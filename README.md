
개발환경 설치방법 (with Anaconda(python), Tensorflow)

## 선확인 사항
1. Windows bit수 확인
- 현재 Tensorflow의 경우 64 bit Windows만 설치 가능

2. Python 버전 확인
- 현재 Python 최신 버전은 3.6 이나 Tensorflow 설치는 3.5까지만 가능
- 공유폴더내 Anaconda의 경우 Python 3.5를 설치
- 기존 Python 혹은 Anaconda 버전 확인 

- vitualenv를 통해서 multi version 관리 가능하나 ... 귀찮음. (http://leegomo.blog.me/220846849492) 


## Python & Package 설치
1. 구글 드라이브 공유 폴더 내 Anaconda3-4.2.0-Windows-x86_64.exe 파일 설치
2. Anaconda Navigator 수행후 왼쪽 Environments Tab에서 필수 패키지 설치/업그레이드
- numpy  : Numeracal Python, 고성능 과학계산 컴퓨팅 및 데이터 분석 패키지
- pandas : 고수준 자료구조 및 파이선을 통한 데이터 분석 도구 제공
- scikit-learn : 

## 기타 Package (한글 형태소) 설치
1. 한글 자연어 처리 Python 패키지 설치 (konlpy)  
- 구글 드라이브 공유 폴더 내 JPype1-0.6.2-cp35-cp35m-win_amd64.whl 다운로드
- cmd 창에서 pip intall JPype1-0.6.2-cp35-cp35m-win_amd64.whl 수행
  [command] 
  >> pip install --upgrade pip
  >> pip install JPype1-0.5.7-cp27-none-win_amd64.whl
- cmd 창에서 pip install konlpy 수행
- 구글 드라이브 공유 폴더 > 관련문서 > 자연어처리 > konlpy-ko.pdf 설치

## Tensorflow 설치
1. Tensorflow 는 python 3.5 버전까지 지원 (현재 3.6 버전으로 설치시 지원하는 python 버전이 없다고 뜸 ....)
- cmd 창에서 pip install tensorflow-cpu (CPU 버전)
             pip install tensorflow-gpu (GPU 버전)
- GPU를 사용시 CUDA, cuDNN 추가 설치 필요 (http://datamasters.tistory.com/12)
