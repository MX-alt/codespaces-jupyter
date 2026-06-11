       IDENTIFICATION DIVISION.
       PROGRAM-ID. URLIFY.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       
       DATA DIVISION.
       FILE SECTION.
       
       WORKING-STORAGE SECTION.
       01 WS-INPUT-STR             PIC X(200).
       01 WS-TRUE-LENGTH           PIC 999.
       01 WS-OUTPUT-STR            PIC X(200).
       01 WS-SPACE-COUNT           PIC 999 VALUE 0.
       01 WS-NEW-INDEX             PIC 999.
       01 WS-INDEX                 PIC 999.
       01 WS-CURRENT-CHAR          PIC X.
       01 WS-RESULT                PIC X(200).
       01 WS-RESULT-LENGTH         PIC 999.
       
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           PERFORM TEST-CASES.
           STOP RUN.
       
       TEST-CASES.
           DISPLAY "Testing URLify:".
           
           MOVE "Mr John Smith    " TO WS-INPUT-STR.
           MOVE 13 TO WS-TRUE-LENGTH.
           PERFORM REPLACE-SPACES.
           IF WS-RESULT = "Mr%20John%20Smith"
               DISPLAY "  'Mr John Smith' -> PASS"
           ELSE
               DISPLAY "  'Mr John Smith' -> FAIL"
               DISPLAY "    Expected: Mr%20John%20Smith"
               DISPLAY "    Got:      " WS-RESULT
           END-IF.
           
           MOVE "a b  " TO WS-INPUT-STR.
           MOVE 3 TO WS-TRUE-LENGTH.
           PERFORM REPLACE-SPACES.
           IF WS-RESULT = "a%20b"
               DISPLAY "  'a b' -> PASS"
           ELSE
               DISPLAY "  'a b' -> FAIL"
               DISPLAY "    Expected: a%20b"
               DISPLAY "    Got:      " WS-RESULT
           END-IF.
           
           MOVE "abc" TO WS-INPUT-STR.
           MOVE 3 TO WS-TRUE-LENGTH.
           PERFORM REPLACE-SPACES.
           IF WS-RESULT = "abc"
               DISPLAY "  'abc' (no spaces) -> PASS"
           ELSE
               DISPLAY "  'abc' (no spaces) -> FAIL"
           END-IF.
           
           DISPLAY SPACE.
           DISPLAY "All test cases completed ✅".
       
       REPLACE-SPACES.
           MOVE 0 TO WS-SPACE-COUNT.
           MOVE 1 TO WS-INDEX.
           MOVE SPACES TO WS-OUTPUT-STR.
           
           PERFORM VARYING WS-INDEX FROM 1 BY 1
               UNTIL WS-INDEX > WS-TRUE-LENGTH
               IF WS-INPUT-STR(WS-INDEX:1) = " "
                   ADD 1 TO WS-SPACE-COUNT
               END-IF
           END-PERFORM.
           
           COMPUTE WS-NEW-INDEX = WS-TRUE-LENGTH + 
               (WS-SPACE-COUNT * 2).
           MOVE WS-NEW-INDEX TO WS-RESULT-LENGTH.
           
           PERFORM VARYING WS-INDEX FROM WS-TRUE-LENGTH BY -1
               UNTIL WS-INDEX < 1
               MOVE WS-INPUT-STR(WS-INDEX:1) TO WS-CURRENT-CHAR
               IF WS-CURRENT-CHAR = " "
                   MOVE "0" TO WS-OUTPUT-STR(WS-NEW-INDEX:1)
                   SUBTRACT 1 FROM WS-NEW-INDEX
                   MOVE "2" TO WS-OUTPUT-STR(WS-NEW-INDEX:1)
                   SUBTRACT 1 FROM WS-NEW-INDEX
                   MOVE "%" TO WS-OUTPUT-STR(WS-NEW-INDEX:1)
                   SUBTRACT 1 FROM WS-NEW-INDEX
               ELSE
                   MOVE WS-CURRENT-CHAR TO 
                       WS-OUTPUT-STR(WS-NEW-INDEX:1)
                   SUBTRACT 1 FROM WS-NEW-INDEX
               END-IF
           END-PERFORM.
           
           MOVE WS-OUTPUT-STR(1:WS-RESULT-LENGTH) TO WS-RESULT.
