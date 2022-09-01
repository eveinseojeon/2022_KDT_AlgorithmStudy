## 입양 시각 구하기(2)

(아직 완전히 해결 안 됨)

---

## NULL 처리하기

**SELECT** ANIMAL_TYPE, **COALESCE**(NAME, 'No name') **AS** NAME, SEX_UPON_INTAKE

**FROM** ANIMAL_INS

**ORDER BY** ANIMAL_ID;

- **COALESCE** 함수는 NULL 값을 다른 값으로 치환하는 데 쓰임

---

## DATETIME에서 DATE로 형 변환

- ORACLE에서는 TO_CHAR() 사용
- MySQL에서는 DATE_FORMAT() 사용


