       IDENTIFICATION DIVISION.
       PROGRAM-ID. IS-UNIQUE.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       
       DATA DIVISION.
       FILE SECTION.
       
       WORKING-STORAGE SECTION.
       01 WS-INPUT-STR             PIC X(100).
       01 WS-STR-LENGTH            PIC 999.
       01 WS-CHAR-ARRAY            PIC X(26).
       01 WS-INDEX                 PIC 999.
       01 WS-CHAR-INDEX            PIC 999.
       01 WS-CURRENT-CHAR          PIC X.
       01 WS-RESULT                PIC 9 VALUE 1.
       01 WS-MARK                  PIC S9(9) COMP VALUE 0.
       01 WS-MOVE-BIT              PIC 999.
       01 WS-BIT-MASK              PIC S9(9) COMP.
       
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           PERFORM TEST-CASES.
           STOP RUN.
       
       TEST-CASES.
           DISPLAY "Testing IsUnique with Set approach:".
           
           MOVE "abc" TO WS-INPUT-STR.
           MOVE 3 TO WS-STR-LENGTH.
           PERFORM IS-UNIQUE-SET.
           EVALUATE WS-RESULT
               WHEN 1 DISPLAY "  'abc' -> PASS (unique)"
               WHEN OTHER DISPLAY "  'abc' -> FAIL"
           END-EVALUATE.
           
           MOVE "leetcode" TO WS-INPUT-STR.
           MOVE 8 TO WS-STR-LENGTH.
           PERFORM IS-UNIQUE-SET.
           EVALUATE WS-RESULT
               WHEN 0 DISPLAY "  'leetcode' -> PASS (not unique)"
               WHEN OTHER DISPLAY "  'leetcode' -> FAIL"
           END-EVALUATE.
           
           MOVE "hello" TO WS-INPUT-STR.
           MOVE 5 TO WS-STR-LENGTH.
           PERFORM IS-UNIQUE-SET.
           EVALUATE WS-RESULT
               WHEN 0 DISPLAY "  'hello' -> PASS (not unique)"
               WHEN OTHER DISPLAY "  'hello' -> FAIL"
           END-EVALUATE.
           
           MOVE "" TO WS-INPUT-STR.
           MOVE 0 TO WS-STR-LENGTH.
           PERFORM IS-UNIQUE-SET.
           EVALUATE WS-RESULT
               WHEN 1 DISPLAY "  '' -> PASS (empty is unique)"
               WHEN OTHER DISPLAY "  '' -> FAIL"
           END-EVALUATE.
           
           DISPLAY SPACE.
           DISPLAY "Testing IsUnique with Bit approach:".
           
           MOVE "abc" TO WS-INPUT-STR.
           MOVE 3 TO WS-STR-LENGTH.
           PERFORM IS-UNIQUE-BIT.
           EVALUATE WS-RESULT
               WHEN 1 DISPLAY "  'abc' -> PASS (unique)"
               WHEN OTHER DISPLAY "  'abc' -> FAIL"
           END-EVALUATE.
           
           MOVE "algorithm" TO WS-INPUT-STR.
           MOVE 9 TO WS-STR-LENGTH.
           PERFORM IS-UNIQUE-BIT.
           EVALUATE WS-RESULT
               WHEN 1 DISPLAY "  'algorithm' -> PASS (unique)"
               WHEN OTHER DISPLAY "  'algorithm' -> FAIL"
           END-EVALUATE.
           
           DISPLAY SPACE.
           DISPLAY "All test cases completed ✅".
       
       IS-UNIQUE-SET.
           PERFORM VARYING WS-INDEX FROM 1 BY 1
               UNTIL WS-INDEX > WS-STR-LENGTH
               MOVE WS-INPUT-STR(WS-INDEX:1) TO WS-CURRENT-CHAR
               PERFORM VARYING WS-CHAR-INDEX FROM WS-INDEX + 1 BY 1
                   UNTIL WS-CHAR-INDEX > WS-STR-LENGTH
                   IF WS-CURRENT-CHAR = 
                       WS-INPUT-STR(WS-CHAR-INDEX:1)
                       MOVE 0 TO WS-RESULT
                       MOVE WS-STR-LENGTH TO WS-INDEX
                       MOVE WS-STR-LENGTH TO WS-CHAR-INDEX
                   END-IF
               END-PERFORM
           END-PERFORM.
       
       IS-UNIQUE-BIT.
           MOVE 1 TO WS-RESULT.
           MOVE 0 TO WS-MARK.
           PERFORM VARYING WS-INDEX FROM 1 BY 1
               UNTIL WS-INDEX > WS-STR-LENGTH
               MOVE WS-INPUT-STR(WS-INDEX:1) TO WS-CURRENT-CHAR
               COMPUTE WS-MOVE-BIT = 
                   FUNCTION ORD(WS-CURRENT-CHAR) - 
                   FUNCTION ORD("a")
               COMPUTE WS-BIT-MASK = FUNCTION MOD(WS-MARK, 
                   FUNCTION MOD(1, 2 ** (WS-MOVE-BIT + 1)))
               IF WS-BIT-MASK NOT = 0
                   MOVE 0 TO WS-RESULT
                   MOVE WS-STR-LENGTH TO WS-INDEX
               ELSE
                   COMPUTE WS-MARK = WS-MARK + 
                       2 ** WS-MOVE-BIT
               END-IF
           END-PERFORM.
