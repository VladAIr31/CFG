# Formal Languages and Automata Theory - Homework 3: Context-Free Grammars (Implementation)

This project implements a parser for a Context-Free Grammar (CFG), performs derivations, generates strings, and tests string membership for a given CFG. [cite: 1]

## Tasks Implemented

The Python script `CFG.py` addresses the following tasks as outlined in the assignment:

1.  **Define a CFG**: Programmatic representation of a CFG. [cite: 1, 2]
2.  **String Generator**: A function to randomly generate strings from the defined CFG. [cite: 3]
3.  **Derivation**: A function to display the derivation of a target string. [cite: 5]
4.  **Membership Tester**: A recognizer function to check if a given string belongs to the language of the CFG. [cite: 6]

## CFG Definition (Task 1)

The implemented CFG is based on the example $G = (\{S\}, \{a, b\}, R, S)$, where $R = \{S \rightarrow aSb | \epsilon\}$. [cite: 17] This grammar generates strings of the form $a^n b^n$ where $n \ge 0$. [cite: 18]

* **Non-Terminals (V)**: `{S}`
* **Terminals ($\Sigma$)**: `{a, b}`
* **Production Rules (R)**:
    * `S -> aSb`
    * `S -> ` (epsilon, represented as an empty string `''` in the code)
* **Start Symbol (S)**: `S`

This definition is programmatically represented in the `CFG.py` script.

## How to Run

1.  Ensure you have Python installed on your system.
2.  Save the provided code as `CFG.py`.
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved `CFG.py`.
5.  Run the script using the command:
    ```bash
    python CFG.py
    ```

The script will execute and print the outputs for each task directly to the console.

## Example Outputs

The script will output:
1.  The definition of the CFG (Non-terminals, Terminals, Production Rules, Start Symbol).
2.  Up to 10 randomly generated strings from the CFG, each with a maximum length of 10 characters. [cite: 3, 4]
3.  Derivation steps for predefined test strings (e.g., "aabb", "aaabbb", "ab", "", "aab").
4.  Membership test results (True/False) for a list of predefined test strings (e.g., "aabb", "ab", "", "aaabbb", "aab", "aba").

**Sample Output Snippet (Illustrative):**
