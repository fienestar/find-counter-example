# find-counter-example

입력한 명제가 거짓이 되게하는 값을 출력합니다.

## 사용 가능한 연산자
- ~
- and
- or
- ->
- <->

우선순위는 나열된 순서와 같습니다.

## 해석 방식

T, F는 각각 참과 거짓을 의미합니다.

연산자, 소괄호, T, F가 아닌 경우 모두 변수로 취급합니다.

## 예

입력

```((A->(B or C)) and (B->D)) -> (A->D)```

출력

```=====모순 발생=====
A: True
B: False
C: True
D: False
```
