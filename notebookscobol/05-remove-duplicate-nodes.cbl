       IDENTIFICATION DIVISION.
       PROGRAM-ID. REMOVE-DUPLICATE-NODES.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       
       DATA DIVISION.
       FILE SECTION.
       
       WORKING-STORAGE SECTION.
       01 WS-NODE-VALUES           PIC 9(3) OCCURS 100 TIMES.
       01 WS-RESULT-VALUES         PIC 9(3) OCCURS 100 TIMES.
       01 WS-NODE-COUNT            PIC 999.
       01 WS-RESULT-COUNT          PIC 999.
       01 WS-INDEX                 PIC 999.
       01 WS-CHECK-INDEX           PIC 999.
       01 WS-CURRENT-VAL           PIC 999.
       01 WS-FOUND                 PIC 9.
       01 WS-OUTPUT-STR            PIC X(100).
       01 WS-OUTPUT-POS            PIC 999.
       
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           PERFORM TEST-CASES.
           STOP RUN.
       
       TEST-CASES.
           DISPLAY "Testing Remove Duplicate Nodes:".
           
           PERFORM TEST-CASE-1.
           PERFORM TEST-CASE-2.
           PERFORM TEST-CASE-3.
           
           DISPLAY SPACE.
           DISPLAY "All test cases completed ✅".
       
       TEST-CASE-1.
           MOVE 6 TO WS-NODE-COUNT.
           MOVE 1 TO WS-NODE-VALUES(1).
           MOVE 2 TO WS-NODE-VALUES(2).
           MOVE 3 TO WS-NODE-VALUES(3).
           MOVE 3 TO WS-NODE-VALUES(4).
           MOVE 2 TO WS-NODE-VALUES(5).
           MOVE 1 TO WS-NODE-VALUES(6).
           
           PERFORM REMOVE-DUPLICATES.
           
           DISPLAY "  Test [1,2,3,3,2,1]:".
           DISPLAY "  Result: " WITH NO ADVANCING.
           PERFORM PRINT-RESULT.
           DISPLAY SPACE.
       
       TEST-CASE-2.
           MOVE 4 TO WS-NODE-COUNT.
           MOVE 5 TO WS-NODE-VALUES(1).
           MOVE 5 TO WS-NODE-VALUES(2).
           MOVE 5 TO WS-NODE-VALUES(3).
           MOVE 5 TO WS-NODE-VALUES(4).
           
           PERFORM REMOVE-DUPLICATES.
           
           DISPLAY "  Test [5,5,5,5]:".
           DISPLAY "  Result: " WITH NO ADVANCING.
           PERFORM PRINT-RESULT.
           DISPLAY SPACE.
       
       TEST-CASE-3.
           MOVE 3 TO WS-NODE-COUNT.
           MOVE 1 TO WS-NODE-VALUES(1).
           MOVE 2 TO WS-NODE-VALUES(2).
           MOVE 3 TO WS-NODE-VALUES(3).
           
           PERFORM REMOVE-DUPLICATES.
           
           DISPLAY "  Test [1,2,3]:".
           DISPLAY "  Result: " WITH NO ADVANCING.
           PERFORM PRINT-RESULT.
           DISPLAY SPACE.
       
       REMOVE-DUPLICATES.
           MOVE 0 TO WS-RESULT-COUNT.
           
           PERFORM VARYING WS-INDEX FROM 1 BY 1
               UNTIL WS-INDEX > WS-NODE-COUNT
               MOVE WS-NODE-VALUES(WS-INDEX) TO WS-CURRENT-VAL
               MOVE 0 TO WS-FOUND
               
               PERFORM VARYING WS-CHECK-INDEX FROM 1 BY 1
                   UNTIL WS-CHECK-INDEX > WS-RESULT-COUNT
                   IF WS-RESULT-VALUES(WS-CHECK-INDEX) = 
                       WS-CURRENT-VAL
                       MOVE 1 TO WS-FOUND
                       MOVE WS-RESULT-COUNT TO WS-CHECK-INDEX
                   END-IF
               END-PERFORM
               
               IF WS-FOUND = 0
                   ADD 1 TO WS-RESULT-COUNT
                   MOVE WS-CURRENT-VAL TO 
                       WS-RESULT-VALUES(WS-RESULT-COUNT)
               END-IF
           END-PERFORM.
       
       PRINT-RESULT.
           MOVE SPACES TO WS-OUTPUT-STR.
           MOVE 1 TO WS-OUTPUT-POS.
           
           PERFORM VARYING WS-INDEX FROM 1 BY 1
               UNTIL WS-INDEX > WS-RESULT-COUNT
               STRING WS-RESULT-VALUES(WS-INDEX) DELIMITED BY SIZE
                   INTO WS-OUTPUT-STR
                   POINTER WS-OUTPUT-POS
               END-STRING
               
               IF WS-INDEX < WS-RESULT-COUNT
                   STRING " -> " DELIMITED BY SIZE
                       INTO WS-OUTPUT-STR
                       POINTER WS-OUTPUT-POS
                   END-STRING
               END-IF
           END-PERFORM.
           
           DISPLAY WS-OUTPUT-STR.
