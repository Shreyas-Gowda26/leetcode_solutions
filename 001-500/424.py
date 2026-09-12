#Brute-Force approach
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0

        # Outer loop for starting index of substrings
        for i in range(len(s)):

            # Array to track frequency of characters in window
            freq = [0] * 26

            # Variable to store the frequency of most common character in window
            max_freq = 0

            # Inner loop to go from current start to end of string
            for j in range(i, len(s)):

                # Increment count of current character
                freq[ord(s[j]) - ord('A')] += 1

                # Update max frequency seen so far
                max_freq = max(max_freq, freq[ord(s[j]) - ord('A')])

                # Length of current window
                window_len = j - i + 1

                # Number of characters to replace
                replace = window_len - max_freq

                # Check if we can replace within k
                if replace <= k:
                    max_length = max(max_length, window_len)

        return max_length
    

#Better-Approach

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to count frequency of characters in current window
        freq = {}

        # Left pointer of sliding window
        left = 0

        # Stores max frequency of any char in current window
        max_freq = 0

        # Stores result
        max_len = 0

        # Traverse through each character with right pointer
        for right in range(len(s)):

            # Increase frequency of current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Update the max frequency in current window
            max_freq = max(max_freq, freq[s[right]])

            # If window is invalid (more than k replacements)
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # Update max_len with current valid window size
            max_len = max(max_len, right - left + 1)

        return max_len