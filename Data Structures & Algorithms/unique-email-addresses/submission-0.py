class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = 0
        seen = set()
        for email in emails:
            terms = email.split('@')
            local = terms[0]
            domain = terms[1]

            clean = ""

            i = 0
            while i < len(local) and local[i] != '+':
                if local[i] != '.':
                    clean += local[i]
                i += 1

            if (clean, domain) not in seen:
                seen.add((clean, domain))
                ans += 1
            
            
            
        return ans

        