INTERVENTIONS = {
    "range_boundary": {
        "title": "Range Boundary Misunderstanding",
        "explanation": (
            "The stop value in Python's range() is excluded. "
            "The sequence stops just before that value."
        ),
        "example": "list(range(5)) produces [0, 1, 2, 3, 4].",
        "follow_ups": [
            {
                "question": "What values does list(range(3)) produce?",
                "expected_answer": "[0, 1, 2]",
            },
            {
                "question": "What values does range(2, 6, 2) produce?",
                "expected_answer": "2, 4",
            },
        ],
    },
    "assignment_equality": {
        "title": "Assignment vs Equality",
        "explanation": (
            "The = operator assigns a value. The == operator compares two values."
        ),
        "example": "x = 5 assigns; x == 5 tests whether x is 5.",
        "follow_ups": [
            {
                "question": "Which operator tests equality in C++?",
                "expected_answer": "==",
            },
            {
                "question": "Which operator assigns a value to a variable in Python?",
                "expected_answer": "=",
            },
        ],
    },
    "return_misunderstanding": {
        "title": "Function Return Misunderstanding",
        "explanation": (
            "return sends a value to the code that called the function; "
            "it does not automatically print that value."
        ),
        "example": "result = add(2, 3) stores the returned value; print(result) displays it.",
        "follow_ups": [
            {
                "question": "Does return automatically print a value from a C function?",
                "expected_answer": "No, it gives the value back to the caller",
            },
            {
                "question": "How do you display a value returned by a Python function?",
                "expected_answer": "print(function())",
            },
        ],
    },
    "indexing": {
        "title": "Zero-Based Indexing",
        "explanation": (
            "C, C++, and Python sequences use zero-based indexes: "
            "the first element is at index 0."
        ),
        "example": "For an array with 5 elements, valid indexes are 0 through 4.",
        "follow_ups": [
            {
                "question": "What is the last valid index of an array with 6 elements?",
                "expected_answer": "5",
            },
            {
                "question": "Which element does items[2] access in Python?",
                "expected_answer": "The third element",
            },
        ],
    },
    "loop_boundary": {
        "title": "Loop Boundary Misunderstanding",
        "explanation": (
            "A loop condition determines whether another iteration runs. "
            "With i < 5, the loop runs for i values 0 through 4."
        ),
        "example": "for (int i = 0; i < 5; ++i) runs five times.",
        "follow_ups": [
            {
                "question": "How many times does for (int i=0; i<4; ++i) run?",
                "expected_answer": "4",
            },
            {
                "question": "What is the final i value used by for (i=0; i<3; i++)?",
                "expected_answer": "2",
            },
        ],
    },
    "pointer_misunderstanding": {
        "title": "Pointer Misunderstanding",
        "explanation": (
            "A pointer stores a memory address. Dereferencing it with * "
            "accesses the value at that address."
        ),
        "example": "int x = 7; int* p = &x; *p is 7.",
        "follow_ups": [
            {
                "question": "What does &x produce in C?",
                "expected_answer": "The address of x",
            },
            {
                "question": "What does *p access when p points to an int?",
                "expected_answer": "The integer value at the address p points to",
            },
        ],
    },
    "memory_management": {
        "title": "Dynamic Memory Management",
        "explanation": (
            "Dynamically allocated memory must be released using the matching "
            "mechanism: free for malloc in C, and delete/delete[] for new in C++."
        ),
        "example": "C++: int* p = new int; delete p;",
        "follow_ups": [
            {
                "question": "Which C function releases memory allocated by malloc?",
                "expected_answer": "free",
            },
            {
                "question": "What should pair with new[] in C++?",
                "expected_answer": "delete[]",
            },
        ],
    },
    "pass_by_value": {
        "title": "Pass-by-Value Misunderstanding",
        "explanation": (
            "A normal value parameter is a copy. To modify a caller's value, "
            "use a pointer in C or a reference in C++."
        ),
        "example": "void update(int& value) in C++ receives a reference.",
        "follow_ups": [
            {
                "question": "Does changing an int passed by value modify the caller's variable?",
                "expected_answer": "No, it changes only the copy",
            },
            {
                "question": "How can a C function modify an integer supplied by its caller?",
                "expected_answer": "Pass a pointer to the integer",
            },
        ],
    },
    "type_misunderstanding": {
        "title": "Type System Misunderstanding",
        "explanation": (
            "Python determines a variable's type at runtime, while C and C++ "
            "variables have declared types."
        ),
        "example": "Python: value = 3; value = 'three' is allowed.",
        "follow_ups": [
            {
                "question": "Can a Python variable hold a string after holding an integer?",
                "expected_answer": "Yes",
            },
            {
                "question": "Can a C variable declared int change its declared type to char?",
                "expected_answer": "No",
            },
        ],
    },
    "string_termination": {
        "title": "C String Termination",
        "explanation": (
            "A C string is a character array ending with the null character "
            "'\\0'. Space for that terminator must be included."
        ),
        "example": "The string \"cat\" needs 4 char slots: c, a, t, and '\\0'.",
        "follow_ups": [
            {
                "question": "Does strlen(\"cat\") count the null terminator?",
                "expected_answer": "No, it returns 3",
            },
            {
                "question": "How much space does char word[] = \"cat\" need in C?",
                "expected_answer": "4",
            },
        ],
    },
}
