### WEEK02

### Week 01 회고

#### 1
- 문제의 요구사항을 정확히 파악하지 못함.
  - 문제를 많이 풀어보지 않아서, 문제 자체에 익숙하지 않음
  - 문제를 읽어도 어떤 맥락이 숨어있는지 파악하지 못함

- 문제의 유형에 따른 접근 방식을 이해하지 못함.
- 주요 개념이 가지고 있는 맥락을 파악하지 못함
  - 재귀 -> 자기자신을 호출한다. -> 자신의 부분을 호출 -> 부분합, 경우의 수 -> 완전탐색


#### 2
- 코드의 구현이 익숙해 졌음

- 변수와 데이터, 자료구조에 **의미**에 대해서 생각해보게 되었음
- 프로그램을 바라보는 관점이 생김.
- 디버거를 이용해서 코드를 디버깅 해봄.
- 재귀 함수에 조금더 익숙해짐.

#### 3
- 컴퓨팅 사고로의 전환 아직 멀었다.
- 깨달음..

#### 프로그램의 구조와 실행
- 프로세서, 메모리 서브시스템으로 구성된 컴퓨터 자체
- 정수와 실수의 근사값과 같은 기본 데이터 타입을 표시하는 방법
- 기계 수준 인스트럭션들이 어떻게 데이터를 처리하는지
- 컴파일러가 어떻게 c 프로그램을 인스트럭션으로 번역하는지
- 프로세서를 더 잘 만드는 방법, 하드웨어 자원이 인스트럭션을 실행하는 데 어떻게 사용되는지 이해
- 컴파일러와 기계수준의 코드 > 어떻게 프로그램의 성능을 극대화할 수 있는지 분석 > 최대 성능을 만들어 낼 수 있도록
  #### 정보의 표현과 처리
  - 파일은 어떻게 저장되고, 사용될까?

  #### 2.0 Intro
  - 컴퓨터에서 정보는 어떻게 저장되고 사용될까?
  - 컴퓨터에서 정보를 저장하고, 계산하는 방식을 이해하는 것은 중요하다. 계산 방식을 이해함으로써 일관된 결과값을 보장할 수 있도록 하기 위해서이다.
  - 정보의 표현(비부호형 인코딩, 2의 보수 인코딩, 부동소수점 인코딩)
  - 실제 수의 표시 방법
    - 실제 수의 표시방법을 학습하면서 표시 가능한 값의 범위와 여러 산술연상의 특성을 이해할 수 있다.
  - 컴퓨터는 숫자를 인코딩하기 위해 여러 가지 이진수 표시를 사용한다. 숫자의 비트 수준 표시 방법을 직접적으로 조작하여 산술연산을 하는 여러 가지 방법을 도출한다.

  #### 2.1 정보의 저장
  - 8바이트
  - 가상메모리
  - 바이트 배열
  - 가상주소공간
  - 컴파일러
  - 런타임 시스템
  - 프로그램 객체들
  - c / c 포인터 / c 컴파일러
  - 16진수 표시

  #### 알고리즘 특강
  - 재귀 / reduction

  #### 컴퓨터 시스템

1. 리셋 벡터
전원을 넣으면 PC에 “공장에서 하드코딩된 물리 주소”가 자동 로드 → 펌웨어 시작.
2. 펌웨어 & 부트로더
펌웨어가 메모리에 부트 코드(부트로더 1단계)를 복사하고 jmp 로 PC 갱신.
부트로더는 OS 커널 이미지를 RAM에 배치한 뒤 또 jmp kernel_entry.
3. 커널이 가상 메모리 초기화
페이지 테이블을 만들고 CR3/TTBR0 레지스터를 설정한 뒤,
jmp or ret 같은 명령으로 **“동일 코드의 가상 주소”**로 PC 변경.
이 순간부터 PC에 들어가는 모든 주소는 가상 주소.
4. 새 프로세스 시작 (execve)
커널은 ELF 프로그램 헤더에서 e_entry(시작 VA)를 읽음.
페이지 테이블에 코드·데이터를 mmap 한 뒤,
PCB(Task Struct) → regs.ip = e_entry.
5. 사용자 모드로 건네주기
스케줄러가 CPU를 그 프로세스에 할당할 때
커널 스택에 저장해 둔 레지스터 집합을 pop/iretq → RIP = e_entry.
최초 명령어 fetch 시 페이지 폴트가 일어나면 커널이 4 KiB를 RAM으로 “당겨온” 뒤 재개.
실행 중 PC 업데이트
6. 순차 명령어: 디코더가 명령 길이(1–15 B x86) 알려주면 하드웨어가 PC += n.
분기/호출: ALU가 계산(상대 오프셋 + PC) → 결과를 PC 레지스터에 직접 씀.
리턴: 스택에서 이전 PC 값을 pop 하여 복원.

#### 이분 탐색
- 정렬된 데이터에서 탐색 범위를 절반씩 줄여나가면서 특정한 원소를 찾는 방법
- O(logN) 시간복잡도

#### 분할 정복
- 데이터를 나누어서 접근하고, 합치면서 문제를 해결하는 방법.
- 병합정렬, 퀵정렬이 대표적인 사례이다.

#### 스택
- 후입선출의 데이터를 임시 저장하는 자료구조.
- collections.deque로 스택 구현

#### 큐
- 선입순출의 데이터를 임시 저장하는 자료구조.
- 링버퍼를 이용한 큐 구현

#### 우선순위 큐
- heap 자료형을 이용해서 구현한 자료구조.
-

#### Linked List
- 단일 연결 리스트
- 이중 연결 리스트
- 노드의 중간지점에서도 자료의 추가와 삭제가 O(1)의 시간복잡도를 가진다.
- 다만 특정 위치의 데이터를 검색해 내는데에는 O(n)의 시간이 걸리는 단점도 갖고 있다.

#### 해시 테이블
- 해시 테이블, 해시 맵은 키를 값에 매핑할 수 있는 구조인, 연관 배열 추가에 사용되는 자료구조.
- 개체가 해시값에 따라 인덱싱


#### 0525

#### 2.3 정수의 산술연산
- 2.3.1 비부호형 덧셈
  - 법칙: 비부호형 덧셈
    -
  - 법칙: 비부호형 덧셈에서 오버플로우 검출하기
  - 법칙: 비부호형 비트반전

- 2.3.2 2의 보수의 덧셈
  - 법칙: 2의 보수의 덧셈
  - 법칙: 2의 보수 덧셈에서 오버플로우 감지

- 2.3.3 2의 보수에서의 비트반전
  - 법칙: 2의 보수 비트반전

- 2.3.4 비부호형 곱셈
  - 법칙: 비부호형 곱셈

- 2.3.5 2의 보수 곰셈
  - 법칙: 2의 보수 곱셈
  - 법칙: 비부호형과 2의 보수 곱셈의 비트수준 동일성

- 2.3.6 상수를 사용한 곱셈
  - 법칙: 2의 제곱을 곱하는 경우
  - 법칙: 2의 제곱으로 비부호형 곱셈하기
  - 법칙: 2의 제곱을 2의 보수에 곱하기

- 2.3.7 2의 제곱으로 나눗셈하기
  - 법칙: 2의 제곱 값으로 비부호형 나눗셈하기
  - 법칙: 2의 제곱으로 2의 보수 나눗셈하기, 반내림
  - 법칙: 2의 제곱으로 2의 보수 나눗셈하기, 반올림

- 2.3.8 정수 산술연산에 대한 마지막 고찰

#### WEEK2 키워드 공부
- stack
  - 원소의 삽입: append
  - 원소의 삭제: pop
  - 파이썬에서는 list를 사용하여 구현

- queue
  - 원소의 삽입: enque
  - 원소의 삭제: deque

  ```python
  from collections import deque
  queue = deque()

  queue.append(10)
  queue.append(20)
  queue.popleft()

  ```

- 해시법
  - 데이터를 저장할 위치 인덱스를 간단한 연산으로 구하는 것을 의미한다.
- 해시 충돌
  - 해시 함수를 이용해서

- 우선순위 큐
  - 인큐할 때에는 데이터에 우선순위를 부여하여 추가하고, 디큐할 때에는 우선순위가 가장 높은 데이터를 꺼내는 방식
  - 파이썬에서 최대 힙으로 사용하고 싶다면 값을 음수로 저장하고, 꺼낼 때 -1을 곱해주는 트릭을 사용한다.
  ```python
  import heapq

  hq = []
  heapq.heappush(hq, 3)
  heapq.heappush(hq, 4)
  heapq.heappush(hq, 5)

  heapq.heappop(hq)
  heapq.heappop(hq)
  heapq.heappop(hq)
  ```

- 힙
  - 최댓값, 최솟값을 찾아내는 연산을 빠르게 하기 위해 고안된 완전이진트리를 기본으로 한 자료구조
  - 힙의 종류는 최대힙, 최소힙이 있다.
  - bottom-up heapify(sift-up)
    - 시간복잡도 o(N)
  - top-down heapify(sift-down)
    - 시간복잡도 o(NlonN)

- 링 버퍼로 큐 구현하기
  - 링 버퍼를 이용해서 큐를 구현하면, 원소의 삽입 삭제의 수행 시간을 O(1)로 단축할 수 있다.

- 해시테이블
  - 키를 값에 매핑할 수 있는 구조인, 연관 배열 추가에 사용되는 자료구조
  - 해시테이블은 해시 함수를 이용하여 색인을 인덱스로 계산해서 사용한다. 키가 문자열인 경우 라이브러리를 이용해서 형변환을 하고 사용한다.
  - 해시 충돌이 발생하면, 오픈 주소법과 체인법을 통해서 해결한다.
  - 오픈 주소법: 빈 버킷을 찾을 때가지 해시를 반복한다.
  - 체인법: 해시값이 같은 원소를 연결 리스트로 관리한다.

- 링크드 리스트

#### 0526

- 알고리즘 문제를 풀 때, 문제를 잘 읽자.
- 변수의 설정이 문제의 절반

#### 0527

- 알고리즘
  - 이분탐색
    - 나무 자르기(반복문/재귀)
    - 공유기 설치
    - 두 용액

- CSAPP
  - 부동소수점: 부동소수점 표현은 실수 표현을 위해 사용하는 형식
  - 비율 이진수
  - 부동소수점 표시
    - 정규화 값
    - 비정규화 값
    - 특수값
    - 근사법

#### 0528
- 이진탐색: lower bound / upper bound
- bisect 라이브러리
- 부동소수점은 실수의 표현 뿐만 아니라, 무한, NaN 같은 값들을 표현할 때에도 사용할 수 있다.
- 긍정적인 마인드로, 초심. 이곳에 들어온 이유

