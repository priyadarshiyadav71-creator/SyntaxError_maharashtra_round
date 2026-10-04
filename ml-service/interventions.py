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
# (key, title, explanation, example, (q1, a1), (q2, a2))
_RAW = [
    # ---------------- Python ----------------
    ("integer_division", "Integer vs Float Division",
     "In Python 3, / always gives a float and // floors to an integer. In C and C++, dividing two ints truncates toward zero.",
     "Python: 7 / 2 is 3.5, 7 // 2 is 3. C++: int a=7, b=2; a / b is 3.",
     ("What is 9 // 4 in Python 3?", "2"), ("What does int a=9, b=2; a / b give in C++?", "4")),
    ("string_immutability", "String Immutability",
     "Python strings cannot be changed in place. Methods like upper() and replace() return a new string.",
     "s = 'cat'; s = s.upper() stores 'CAT'; s.upper() alone changes nothing.",
     ("s = 'dog'; s.upper(); print(s). What prints?", "dog"), ("Can you do s[0] = 'X' on a Python string?", "No, TypeError")),
    ("mutable_default_argument", "Mutable Default Arguments",
     "A default value is created once when the function is defined, so a default list is shared across calls.",
     "def add(x, lst=[]) keeps growing; use lst=None and create the list inside.",
     ("What is the safe default for a list parameter?", "None, then create the list inside"), ("When is a default argument evaluated?", "Once, at function definition")),
    ("list_aliasing", "List Aliasing",
     "b = a makes both names point to the same list. Use a.copy() or a[:] to get an independent copy.",
     "a = [1]; b = a; b.append(2) makes a equal [1, 2].",
     ("a = [1]; b = a; b.append(2); print(a). What prints?", "[1, 2]"), ("a = [1]; b = a.copy(); b.append(2); print(a). What prints?", "[1]")),
    ("identity_vs_equality", "is vs ==",
     "== compares values; is checks whether two names refer to the same object.",
     "[1, 2] == [1, 2] is True, but the two lists are different objects so `is` gives False.",
     ("Which operator compares values in Python?", "=="), ("Which is idiomatic to test for None?", "is None")),
    ("variable_scope", "Variable Scope",
     "Variables assigned inside a function are local. They disappear when the function returns, and assigning to a name inside does not change a global of the same name.",
     "def f(): x = 1; f(); print(x) raises NameError.",
     ("Does a local variable exist after its function returns?", "No"), ("Which keyword lets a function assign to a module-level variable?", "global")),
    ("slicing_boundary", "Slice End Exclusive",
     "In s[a:b] the start is included and the stop is excluded, just like range().",
     "'python'[1:3] is 'yt'.",
     ("What is 'hello'[1:3]?", "el"), ("What is 'hello'[::-1]?", "olleh")),
    ("list_method_return", "Methods That Return None",
     "In-place list methods such as sort(), append() and reverse() change the list and return None. Use sorted() for a new list.",
     "x = lst.sort() makes x None; use x = sorted(lst).",
     ("What does lst.append(3) return?", "None"), ("Which function returns a new sorted list?", "sorted")),
    ("operator_precedence", "Operator Precedence",
     "Multiplication and division bind tighter than addition and subtraction; ** binds tighter than *. Use parentheses to override.",
     "2 + 3 * 4 is 14, (2 + 3) * 4 is 20.",
     ("What is 2 + 3 * 4?", "14"), ("What is 2 * 3 ** 2?", "18")),
    ("truthiness", "Truthiness",
     "Empty containers, 0, 0.0, '' and None are falsy. Non-empty values, including the string '0', are truthy.",
     "bool([]) is False, bool('0') is True.",
     ("What is bool('')?", "False"), ("What is bool('0')?", "True")),
    ("string_operations", "String Operations",
     "+ on two strings concatenates, it does not add numbers. Mixing str and int with + raises TypeError. * repeats a string.",
     "'5' + '3' is '53'; 'ab' * 3 is 'ababab'.",
     ("What is '4' + '2'?", "42"), ("What is 'ab' * 2?", "abab")),
    ("dict_access", "Dictionary Access",
     "d[key] raises KeyError for a missing key, while d.get(key) returns None (or a default you give).",
     "d = {'a': 1}; d['z'] raises KeyError; d.get('z') is None.",
     ("What does d.get('missing') return?", "None"), ("What does d['missing'] raise?", "KeyError")),
    # ---------------- C / C++ ----------------
    ("uninitialized_variable", "Uninitialized Variables",
     "A local int in C/C++ has an indeterminate value until you assign one. Reading it is undefined behavior; it is not automatically 0.",
     "int x; cout << x; may print any number. int x = 0; is safe.",
     ("Is an uninitialized local int equal to 0?", "No, its value is indeterminate"), ("What does int arr[3] = {}; contain?", "0, 0, 0")),
    ("array_out_of_bounds", "Array Bounds",
     "Valid indexes are 0 to size-1. Going past the end is undefined behavior in C/C++; vector::at() checks and throws.",
     "int a[5]; a[5] is out of bounds.",
     ("What is the last valid index of int a[10]?", "9"), ("Which vector access throws on a bad index?", "at()")),
    ("switch_fallthrough", "Switch Fallthrough",
     "Without break, execution continues into the following cases until a break or the end of the switch.",
     "case 1: print 'A'; case 2: print 'B'; with x = 1 prints AB.",
     ("What does break do in a switch?", "Exits the switch"), ("Without break, what happens after a matching case?", "Execution falls through to the next case")),
    ("increment_operators", "Pre vs Post Increment",
     "i++ yields the old value then increments; ++i increments then yields the new value.",
     "int i = 5; int j = i++; gives i = 6, j = 5.",
     ("int i = 3; cout << i++; prints what?", "3"), ("int i = 3; cout << ++i; prints what?", "4")),
    ("vector_size", "Vector Size",
     "vector<int> v(n) starts with n elements; push_back adds one more. size() is the element count, capacity() is allocated space.",
     "vector<int> v(3); v.push_back(1); v.size() is 4.",
     ("vector<int> v(2); v.push_back(9); v.size()?", "3"), ("What does an empty vector's size() return?", "0")),
    ("const_misunderstanding", "const Correctness",
     "const means the value cannot be modified through that name. Trying to assign to a const object is a compile error.",
     "const int x = 5; x = 6; does not compile.",
     ("Can you assign to a const int?", "No, compile error"), ("What does const T& promise a function?", "It will not modify the argument")),
    ("char_vs_string", "char vs String Literal",
     "'a' is one char (its numeric code works in arithmetic). \"a\" is a string literal: a char array with a '\\0' terminator.",
     "cout << 'a' + 1 prints 98.",
     ("What is 'a' + 1 as an int?", "98"), ("How many bytes is \"a\" in C?", "2")),
    # ---------------- React ----------------
    ("state_mutation", "Never Mutate State",
     "React detects changes by comparing references. Call the setter with a new value or a new copy of the array/object instead of mutating.",
     "setItems([...items, x]) instead of items.push(x).",
     ("How do you add to an array held in state?", "setItems([...items, x])"), ("How do you update one field of an object in state?", "setUser({ ...user, name: 'x' })")),
    ("state_replace", "State Setters Replace",
     "With useState, the setter replaces the whole value; it does not merge objects like class setState did. Spread the old object to keep fields.",
     "setUser({ ...user, name: 'A' }) keeps the other fields.",
     ("Does setUser({ name: 'A' }) keep the old age field?", "No"), ("How do you keep the old fields?", "Spread the old object")),
    ("setstate_async", "State Updates Are Batched",
     "State from useState is a snapshot for that render. After calling the setter, the variable still holds the old value until the next render. Use the functional form to chain updates.",
     "setCount(c => c + 1) twice adds 2; setCount(count + 1) twice adds 1.",
     ("count = 0; setCount(count + 1) twice. Final count?", "1"), ("count = 0; setCount(c => c + 1) twice. Final count?", "2")),
    ("useeffect_deps", "useEffect Dependencies",
     "[] runs once after mount, no array runs after every render, [dep] runs after mount and when dep changes. Return a function to clean up.",
     "useEffect(() => { fetchUser(id) }, [id]);",
     ("When does useEffect(fn, []) run?", "Once after mount"), ("When does cleanup run?", "Before the next effect and on unmount")),
    ("missing_key", "Keys in Lists",
     "Each item rendered by map() needs a stable, unique key on the outermost element so React can track it across renders.",
     "items.map(i => <li key={i.id}>{i.name}</li>)",
     ("Where does key go in a map callback?", "On the outermost returned element"), ("Is the array index always a safe key?", "No")),
    ("props_readonly", "Props Are Read-Only",
     "A component must not modify its props. To change data owned by a parent, call a callback prop that updates the parent's state.",
     "<Child count={count} onIncrement={() => setCount(c => c + 1)} />",
     ("Can a child assign to props.name?", "No"), ("How does a child request a change?", "Call a callback prop")),
    ("conditional_render", "Conditional Rendering Pitfalls",
     "{0 && <X />} renders the number 0 because 0 is a valid React child. Compare explicitly (count > 0 &&) or use a ternary.",
     "{count > 0 && <Badge />}",
     ("What does {0 && <p>Hi</p>} render?", "0"), ("Safer way to guard on a number?", "count > 0 &&")),
    ("event_handler_invocation", "Passing vs Calling Handlers",
     "onClick expects a function. onClick={handle()} calls it during render; pass onClick={handle} or onClick={() => handle(id)}.",
     "<button onClick={() => remove(id)}>",
     ("What is wrong with onClick={save()}?", "It runs during render"), ("How do you pass an argument?", "onClick={() => save(id)}")),
    ("controlled_input", "Controlled Inputs",
     "An input with a value prop is controlled and needs onChange to update state. Read text with event.target.value. defaultValue makes an uncontrolled input.",
     "<input value={name} onChange={e => setName(e.target.value)} />",
     ("What do you read in onChange?", "event.target.value"), ("What prop sets an uncontrolled initial value?", "defaultValue")),
    ("hooks_rules", "Rules of Hooks",
     "Call hooks only at the top level of function components or custom hooks, never inside conditions, loops or nested functions, so order stays the same each render.",
     "Put `if` logic inside the hook, not around it.",
     ("Can you call useState inside an if?", "No"), ("What must a custom hook name start with?", "use")),
    ("jsx_syntax", "JSX Syntax Rules",
     "JSX uses className, htmlFor, camelCase props, style objects, self-closing tags and a single root (or a Fragment). Embed JS with { }.",
     "<label htmlFor='n' className='lbl' style={{ color: 'red' }} />",
     ("Which prop sets a CSS class in JSX?", "className"), ("How do you write inline style?", "style={{ color: 'red' }}")),
    ("component_naming", "Capitalized Component Names",
     "Lowercase JSX tags are treated as HTML elements. Component names must start with a capital letter.",
     "<ProductCard /> works; <productCard /> does not.",
     ("What must a component name start with?", "A capital letter"), ("How does React treat <card />?", "As an HTML element")),
    ("rerender_trigger", "What Triggers a Re-render",
     "Re-renders come from state changes, new props from a re-rendering parent, or context changes. Plain variables and ref.current do not trigger them.",
     "let n = 0; n++ updates the variable but not the screen.",
     ("Does changing ref.current re-render?", "No"), ("Does a plain let variable change re-render?", "No")),
    ("usestate_initial", "Initial State Runs Once",
     "The argument to useState is used only on the first render. Later renders keep the current state, even if the initial prop changes.",
     "useState(props.start) ignores later changes to props.start.",
     ("Is useState's argument used on every render?", "No, only the first"), ("Does state follow a changed initial prop?", "No")),
    ("lifting_state", "Lifting State Up",
     "When siblings share data, move the state to their closest common parent and pass it down as props, with callbacks to change it.",
     "Parent holds `selected`; passes it and `onSelect` to both children.",
     ("Where should shared sibling state live?", "In the closest common parent"), ("How does a child update parent state?", "Via a callback prop")),
    ("children_prop", "The children Prop",
     "props.children is whatever JSX is nested between a component's opening and closing tags.",
     "<Card><p>Hi</p></Card> gives Card props.children = <p>Hi</p>.",
     ("What is props.children?", "The nested JSX content"), ("Where do you render it?", "Inside the component's returned JSX")),
    ("map_return", "Returning from map",
     "An arrow function with braces needs an explicit return. Without braces the expression is returned implicitly.",
     "items.map(i => <li>{i}</li>) or items.map(i => { return <li>{i}</li>; })",
     ("(i) => { <li>{i}</li> } returns what?", "undefined"), ("How do you fix it?", "Add return or remove the braces")),
    ("context_usage", "Context for Shared Data",
     "Context lets distant components read shared values without passing props through every level. Read it with useContext.",
     "const theme = useContext(ThemeContext);",
     ("Which hook reads context?", "useContext"), ("What problem does context reduce?", "Prop drilling")),
    ("memo_misunderstanding", "Memoization Is an Optimization",
     "useMemo and React.memo skip work when inputs are shallow-equal, but they are performance hints, not guarantees of correctness.",
     "React.memo(Row) re-renders Row only if its props change.",
     ("Does React.memo block updates when props change?", "No"), ("Is useMemo a semantic guarantee?", "No, only an optimization")),
    ("react_core_concepts", "React Core Concepts",
     "React is a UI library. Each component instance has its own state, and the virtual DOM lets React update only what changed.",
     "Two <Counter /> elements keep separate counts.",
     ("Do two instances of a component share state?", "No"), ("Is React a full framework with routing?", "No, a UI library")),
    # ---------------- Basic coding problems ----------------
    ("accumulator_init", "Accumulator Initialization",
     "Start a running total at the identity value: 0 for sums, 1 for products. The wrong start skews every result.",
     "total = 0; for x in nums: total += x",
     ("What should a running sum start at?", "0"), ("What should a running product start at?", "1")),
    ("max_init", "Initializing a Maximum",
     "Starting max at 0 fails for all-negative lists. Start from the first element (or negative infinity).",
     "best = nums[0]; for x in nums: if x > best: best = x",
     ("Why is max = 0 wrong for [-5, -2]?", "0 is larger than every element"), ("Better starting value?", "nums[0]")),
    ("factorial_logic", "Factorial Base Case",
     "n! = n * (n-1)!, and 0! = 1 (also 1! = 1). Base case 1 keeps the recursion from collapsing to 0.",
     "5! = 120.",
     ("What is 0!?", "1"), ("What is 4!?", "24")),
    ("fibonacci_indexing", "Fibonacci Indexing",
     "With fib(0)=0 and fib(1)=1, each term is the sum of the previous two. Check which index the sequence starts from.",
     "0, 1, 1, 2, 3, 5, 8: fib(6) = 8.",
     ("fib(5) with fib(0)=0, fib(1)=1?", "5"), ("fib(7)?", "13")),
    ("even_odd_modulo", "Modulo Basics",
     "a % b is the remainder after division, not the quotient. n % 2 is 0 for even and 1 for odd numbers.",
     "17 % 5 is 2 (17 = 3*5 + 2).",
     ("What is 17 % 5?", "2"), ("What is 8 % 2?", "0")),
    ("swap_variables", "Swapping Two Variables",
     "a = b; b = a overwrites a first, so both end up equal. Use a temporary variable (or tuple swap in Python).",
     "tmp = a; a = b; b = tmp, or a, b = b, a.",
     ("a=1, b=2; a=b; b=a. What are a and b?", "2 and 2"), ("Python one-line swap?", "a, b = b, a")),
    ("reverse_string", "Reversing a String",
     "s[::-1] steps backwards through the whole string. A step of 2 would skip characters instead.",
     "'abc'[::-1] is 'cba'.",
     ("What is 'stop'[::-1]?", "pots"), ("What does [::2] do?", "Takes every second character")),
    ("palindrome_logic", "Palindrome Check",
     "A palindrome reads the same forwards and backwards: compare s with s[::-1].",
     "'level' == 'level'[::-1] is True.",
     ("Is 'noon' a palindrome?", "Yes"), ("Is 'cat' a palindrome?", "No")),
    ("vowel_count", "Counting Matches",
     "When counting a category, make sure the condition tests membership in that category, not its complement.",
     "sum(ch in 'aeiou' for ch in word) counts vowels.",
     ("How many vowels are in 'banana'?", "3"), ("How many in 'rhythm'?", "0")),
    ("nested_loop_count", "Nested Loop Iterations",
     "Inner loops run fully for every outer iteration, so total iterations multiply: a * b, not a + b.",
     "for i in range(3): for j in range(4) runs 12 times.",
     ("How many runs: range(2) outer, range(5) inner?", "10"), ("How many runs: i<3, j<3?", "9")),
    ("fizzbuzz_logic", "FizzBuzz Ordering",
     "Test the most specific condition (divisible by both 3 and 5, i.e. 15) first, or the plain Fizz branch swallows it.",
     "if n % 15 == 0: ... elif n % 3 == 0: ... elif n % 5 == 0: ...",
     ("What prints for 30?", "FizzBuzz"), ("What prints for 9?", "Fizz")),
    ("off_by_one_sum", "Inclusive Range Sums",
     "To include n in range(), use range(1, n + 1). range(1, n) stops at n-1.",
     "sum(range(1, 6)) is 10; sum(range(1, 7)) is 21.",
     ("What does sum(range(1, 5)) give?", "10"), ("How do you sum 1 through 5?", "sum(range(1, 6))")),
    ("sorting_logic", "Sorting Basics",
     "sorted(list)[0] is the smallest element; sorted() returns a new list and leaves the original unchanged.",
     "sorted([3, 1, 2]) is [1, 2, 3].",
     ("What is sorted([5, 2, 9])[0]?", "2"), ("What is the last item of sorted([5, 2, 9])?", "9")),
]

NEW_INTERVENTIONS = {
    key: {
        "title": title,
        "explanation": explanation,
        "example": example,
        "follow_ups": [
            {"question": q1, "expected_answer": a1},
            {"question": q2, "expected_answer": a2},
        ],
    }
    for key, title, explanation, example, (q1, a1), (q2, a2) in _RAW
}

INTERVENTIONS.update(NEW_INTERVENTIONS)