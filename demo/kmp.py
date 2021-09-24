import sys
sys.path.append('..')

from qcpm.searcher.kmp import KMP

haystack = "abxabcabcabyabcababcabyabcaby"
needle = "abcaby"

kmp = KMP()

for ans in kmp.apply(haystack, needle):
    print(ans)

print("--------------------")


haystack = "ababababababa"
needle = "aba"

for ans in kmp.apply(haystack, needle):
    print(ans)