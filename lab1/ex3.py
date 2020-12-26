start1 = 10
end1 = 11
start2 = 12
end2 = 13

def checkSchedule():
  if start1 > start2:
    s = start1
  else: s = start2
  if end1 < end2:
    e = end1
  else:  e = end2
  if s < e:
    print ("The appointments overlap")
  else:
   print ("The appointments don't overlap")
  return

checkSchedule ()
