       IDENTIFICATION DIVISION.
       PROGRAM-ID. ANAGRAM.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       
       DATA DIVISION.
       FILE SECTION.
       
       WORKING-STORAGE SECTION.
       01 WS-STRING-1              PIC X(100).
       01 WS-STRING-2              PIC X(100).
       01 WS-LEN-1                 PIC 999.
       01 WS-LEN-2                 PIC 999.
       01 WS-COUNTS                PIC 9(3) OCCURS 26 TIMES.
       01 WS-INDEX                 PIC 999.
       01 WS-CHAR-INDEX            PIC 999.
       01 WS-CURRENT-CHAR          PIC X.
       01 WS-RESULT                PIC 9 VALUE 1.
       01 WS-ARRAY-INDEX           PIC 999.
       
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           PERFORM TEST-CASES.
           STOP RUN.
       
       TEST-CASES.
           DISPLAY "Testing Anagram Check:".
           
           MOVE "abc" TO WS-STRING-1.
           MOVE "cba" TO WS-STRING-2.
           MOVE 3 TO WS-LEN-1.
           MOVE 3 TO WS-LEN-2.
           PERFORM CHECK-PERMUTATION.
           EVALUATE WS-RESULT
               WHEN 1 DISPLAY "  'abc' and 'cba' -> PASS (anagram)"
               WHEN OTHER DISPLAY "  'abc' and 'cba' -> FAIL"
           END-EVALUATE.
           
           MOVE "apple" TO WS-STRING-1.
           MOVE "pale" TO WS-STRING-2.
           MOVE 5 TO WS-LEN-1.
           MOVE 4 TO WS-LEN-2.
           PERFORM CHECK-PERMUTATION.
           EVALUATE WS-RESULT
               WHEN 0 DISPLAY "  'apple' and 'pale' -> PASS (not anagram)"
               WHEN OTHER DISPLAY "  'apple' and 'pale' -> FAIL"
           END-EVALUATE.
           
           MOVE "listen" TO WS-STRING-1.
           MOVE "silent" TO WS-STRING-2.
           MOVE 6 TO WS-LEN-1.
           MOVE 6 TO WS-LEN-2.
           PERFORM CHECK-PERMUTATION.
           EVALUATE WS-RESULT
               WHEN 1 DISPLAY "  'listen' and 'silent' -> PASS (anagram)"
               WHEN OTHER DISPLAY "  'listen' and 'silent' -> FAIL"
           END-EVALUATE.
           
           DISPLAY SPACE.
           DISPLAY "All test cases completed ✅".
       
       CHECK-PERMUTATION.
           MOVE 1 TO WS-RESULT.
           
           IF WS-LEN-1 NOT = WS-LEN-2
               MOVE 0 TO WS-RESULT
               EXIT PARAGRAPH
           END-IF.
           
           PERFORM VARYING WS-ARRAY-INDEX FROM 1 BY 1
               UNTIL WS-ARRAY-INDEX > 26
               MOVE 0 TO WS-COUNTS(WS-ARRAY-INDEX)
           END-PERFORM.
           
           PERFORM VARYING WS-INDEX FROM 1 BY 1
               UNTIL WS-INDEX > WS-LEN-1
               MOVE WS-STRING-1(WS-INDEX:1) TO WS-CURRENT-CHAR
               COMPUTE WS-CHAR-INDEX = 
                   FUNCTION ORD(WS-CURRENT-CHAR) - 
                   FUNCTION ORD("a") + 1
               ADD 1 TO WS-COUNTS(WS-CHAR-INDEX)
           END-PERFORM.
           
           PERFORM VARYING WS-INDEX FROM 1 BY 1
               UNTIL WS-INDEX > WS-LEN-2
               MOVE WS-STRING-2(WS-INDEX:1) TO WS-CURRENT-CHAR
               COMPUTE WS-CHAR-INDEX = 
                   FUNCTION ORD(WS-CURRENT-CHAR) - 
                   FUNCTION ORD("a") + 1
               SUBTRACT 1 FROM WS-COUNTS(WS-CHAR-INDEX)
           END-PERFORM.
           
           PERFORM VARYING WS-ARRAY-INDEX FROM 1 BY 1
               UNTIL WS-ARRAY-INDEX > 26
               IF WS-COUNTS(WS-ARRAY-INDEX) NOT = 0
                   MOVE 0 TO WS-RESULT
                   MOVE 27 TO WS-ARRAY-INDEX
               END-IF
           END-PERFORM.
