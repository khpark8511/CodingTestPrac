-- 코드를 입력하세요
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE, DECODE(STATUS,'SALE','판매중','RESERVED','예약중','DONE','거래완료') STATUS
FROM USED_GOODS_BOARD 
WHERE CREATED_DATE BETWEEN TO_DATE('20221005','YYYYMMDD') AND TO_DATE('20221006','YYYYMMDD') -1/86400
ORDER BY BOARD_ID DESC;