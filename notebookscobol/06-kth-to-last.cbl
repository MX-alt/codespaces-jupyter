       IDENTIFICATION DIVISION.
       PROGRAM-ID. KTH-TO-LAST.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       
       DATA DIVISION.
       FILE SECTION.
       
       WORKING-STORAGE SECTION.
       01 WS-NODE-VALUES           PIC 9(3) OCCURS 100 TIMES.
       01 WS-NODE-COUNT            PIC 999.
       01 WS-K-VALUE               PIC 999.
       01 WS-RESULT-VALUE          PIC 999.
       01 WS-INDEX                 PIC 999.
       01 WS-POSITION              PIC 999.
       
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           PERFORM TEST-CASES.
           STOP RUN.
       
       TEST-CASES.
           DISPLAY "Testing Kth Node to Last:".
           
           PERFORM TEST-CASE-1.
           PERFORM TEST-CASE-2.
           PERFORM TEST-CASE-3.
           PERFORM TEST-CASE-4.
           
           DISPLAY SPACE.
           DISPLAY "All test cases completed ✅".
       
       TEST-CASE-1.
           MOVE 5 TO WS-NODE-COUNT.
           MOVE 1 TO WS-NODE-VALUES(1).
           MOVE 2 TO WS-NODE-VALUES(2).
           MOVE 3 TO WS-NODE-VALUES(3).
           MOVE 4 TO WS-NODE-VALUES(4).
           MOVE 5 TO WS-NODE-VALUES(5).
           MOVE 2 TO WS-K-VALUE.
           
           PERFORM FIND-KTH-TO-LAST.
           
           DISPLAY "  List [1,2,3,4,5], k=2".
           DISPLAY "  Result: " WS-RESULT-VALUE 
               " (Expected: 4)".
       
       TEST-CASE-2.
           MOVE 5 TO WS-NODE-COUNT.
           MOVE 1 TO WS-NODE-VALUES(1).
           MOVE 2 TO WS-NODE-VALUES(2).
           MOVE 3 TO WS-NODE-VALUES(3).
           MOVE 4 TO WS-NODE-VALUES(4).
           MOVE 5 TO WS-NODE-VALUES(5).
           MOVE 1 TO WS-K-VALUE.
           
           PERFORM FIND-KTH-TO-LAST.
           
           DISPLAY "  List [1,2,3,4,5], k=1".
           DISPLAY "  Result: " WS-RESULT-VALUE 
               " (Expected: 5)".
       
       TEST-CASE-3.
           MOVE 5 TO WS-NODE-COUNT.
           MOVE 1 TO WS-NODE-VALUES(1).
           MOVE 2 TO WS-NODE-VALUES(2).
           MOVE 3 TO WS-NODE-VALUES(3).
           MOVE 4 TO WS-NODE-VALUES(4).
           MOVE 5 TO WS-NODE-VALUES(5).
           MOVE 5 TO WS-K-VALUE.
           
           PERFORM FIND-KTH-TO-LAST.
           
           DISPLAY "  List [1,2,3,4,5], k=5".
           DISPLAY "  Result: " WS-RESULT-VALUE 
               " (Expected: 1)".
       
       TEST-CASE-4.
           MOVE 3 TO WS-NODE-COUNT.
           MOVE 10 TO WS-NODE-VALUES(1).
           MOVE 20 TO WS-NODE-VALUES(2).
           MOVE 30 TO WS-NODE-VALUES(3).
           MOVE 1 TO WS-K-VALUE.
           
           PERFORM FIND-KTH-TO-LAST.
           
           DISPLAY "  List [10,20,30], k=1".
           DISPLAY "  Result: " WS-RESULT-VALUE 
               " (Expected: 30)".
       
       FIND-KTH-TO-LAST.
           COMPUTE WS-POSITION = WS-NODE-COUNT - WS-K-VALUE + 1.
           MOVE WS-NODE-VALUES(WS-POSITION) TO WS-RESULT-VALUE.
