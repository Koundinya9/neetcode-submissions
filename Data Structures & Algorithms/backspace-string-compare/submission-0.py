class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:


        def clean(word):
            stack = []

            for c in word: 
                if c == '#':
                    if stack:
                        stack.pop()

                else:
                    stack.append(c)

            return stack

        s1 = clean(s)
        t1 = clean(t)

        print(s1)
        print(t1)

        return s1 == t1