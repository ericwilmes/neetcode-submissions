class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        position_to_letter_freqs = {}
        position = 0
        for s in strs:
            # if s anagram of anything in counts:
            #     output[position of anagram].append(counts)
            freqs = self.create_frequency_dict(s)
            if freqs in position_to_letter_freqs:
                output[position_to_letter_freqs[freqs]].append(s)
            else:
                position_to_letter_freqs[freqs] = position
                output.append([s])
                position += 1
        return output

    def create_frequency_dict(self, s: str) -> dict[str, int]:
        freqs = [0 for _ in range(26)]
        for letter in s:
            pos = ord(letter) - 97
            freqs[pos] += 1
        return tuple(freqs)