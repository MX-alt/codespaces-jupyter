       IDENTIFICATION DIVISION.
       PROGRAM-ID. PALINDROME-PERMUTATION.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       
       DATA DIVISION.
       FILE SECTION.
       
       WORKING-STORAGE SECTION.
       01 WS-INPUT-STR             PIC X(200).
       01 WS-CLEAN-STR             PIC X(200).
       01 WS-STR-LENGTH            PIC 999.
       01 WS-CLEAN-LENGTH          PIC 999.
       01 WS-INDEX                 PIC 999.
       01 WS-CURRENT-CHAR          PIC X.
       01 WS-ODD-CHARS              PIC X(26) VALUE SPACES.
       01 WS-CHAR-INDEX            PIC 999.
       01 WS-ODD-COUNT             PIC 999 VALUE 0.
       01 WS-RESULT                PIC 9 VALUE 1.
       01 WS-FOUND                 PIC 9.
       01 WS-LOWER-CHAR            PIC X.
       
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           PERFORM TEST-CASES.
           STOP RUN.
       
       TEST-CASES.
           DISPLAY "Testing Palindrome Permutation:".
           
           MOVE "code" TO WS-INPUT-STR.
           PERFORM CAN-PERMUTE-PALINDROME.
           EVALUATE WS-RESULT
               WHEN 0 DISPLAY "  'code' -> PASS (cannot permute)"
               WHEN OTHER DISPLAY "  'code' -> FAIL"
           END-EVALUATE.
           
           MOVE "tactcoa" TO WS-INPUT-STR.
           PERFORM CAN-PERMUTE-PALINDROME.
           EVALUATE WS-RESULT
               WHEN 1 DISPLAY "  'tactcoa' -> PASS (can permute)"
               WHEN OTHER DISPLAY "  'tactcoa' -> FAIL"
           END-EVALUATE.
           
           MOVE "a" TO WS-INPUT-STR.
           PERFORM CAN-PERMUTE-PALINDROME.
           EVALUATE WS-RESULT
               WHEN 1 DISPLAY "  'a' -> PASS (can permute)"
               WHEN OTHER DISPLAY "  'a' -> FAIL"
           END-EVALUATE.
           
           MOVE "aab" TO WS-INPUT-STR.
           PERFORM CAN-PERMUTE-PALINDROME.
           EVALUATE WS-RESULT
               WHEN 1 DISPLAY "  'aab' -> PASS (can permute)"
               WHEN OTHER DISPLAY "  'aab' -> FAIL"
           END-EVALUATE.
           
           MOVE "ab" TO WS-INPUT-STR.
           PERFORM CAN-PERMUTE-PALINDROME.
           EVALUATE WS-RESULT
               WHEN 0 DISPLAY "  'ab' -> PASS (cannot permute)"
               WHEN OTHER DISPLAY "  'ab' -> FAIL"
           END-EVALUATE.
           
           DISPLAY SPACE.
           DISPLAY "All test cases completed ✅".
       
       CAN-PERMUTE-PALINDROME.
           MOVE 1 TO WS-RESULT.
           MOVE SPACES TO WS-ODD-CHARS.
           MOVE 0 TO WS-ODD-COUNT.
           
           MOVE FUNCTION LENGTH(
               FUNCTION TRIM(WS-INPUT-STR)) TO WS-STR-LENGTH.
           
           PERFORM VARYING WS-INDEX FROM 1 BY 1
               UNTIL WS-INDEX > WS-STR-LENGTH
               MOVE WS-INPUT-STR(WS-INDEX:1) TO WS-CURRENT-CHAR
               IF WS-CURRENT-CHAR NOT = " "
                   MOVE FUNCTION LOWER-CASE(WS-CURRENT-CHAR) 
                       TO WS-LOWER-CHAR
                   PERFORM CHECK-ODD-CHAR
               END-IF
           END-PERFORM.
           
           IF WS-ODD-COUNT > 1
               MOVE 0 TO WS-RESULT
           END-IF.
       
       CHECK-ODD-CHAR.
           MOVE 0 TO WS-FOUND.
           PERFORM VARYING WS-CHAR-INDEX FROM 1 BY 1
               UNTIL WS-CHAR-INDEX > WS-ODD-COUNT
               IF WS-ODD-CHARS(WS-CHAR-INDEX:1) = WS-LOWER-CHAR
                   MOVE 1 TO WS-FOUND
                   MOVE 100 TO WS-CHAR-INDEX
               END-IF
           END-PERFORM.
           
           IF WS-FOUND = 0
               ADD 1 TO WS-ODD-COUNT
               MOVE WS-LOWER-CHAR TO 
                   WS-ODD-CHARS(WS-ODD-COUNT:1)
           ELSE
               MOVE WS-ODD-CHARS(1:WS-ODD-COUNT)
                   TO WS-ODD-CHARS
               MOVE WS-ODD-CHARS(WS-CHAR-INDEX:1) 
                   TO WS-ODD-CHARS(26:1)
               SUBTRACT 1 FROM WS-ODD-COUNT
           END-IF.
