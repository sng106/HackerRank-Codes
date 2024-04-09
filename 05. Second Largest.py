def ur(array):
  unique=sorted(set(array), reverse=True)
  if len(unique) >= 2:
      return unique[1]
  else:
    return "Invalid "
n=int(input())
elements=list(map(int, input().split( )))
print(ur(elements))
