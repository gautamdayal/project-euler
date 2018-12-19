s = str(sum([n ** n for n in range(1, 1001)]))
endslice = s[len(s) - 10:len(s) - 1]
print(endslice)
# Output: 911084670
