def cscan(tracks, arm_position, lrequests, debug=False):
  """
  Elevator Algorithm

  Args:
      tracks (int) : number of cylinders
      arm_position (int): arm position
      lrequests (list<int>): request list
  """

  distance=0
  n = len(lrequests)
  current_pos = arm_position

  lrequests.sort()

  olders = [x for x in lrequests if x > arm_position]
  minors = [x for x in lrequests if x < arm_position]

  request = olders + [tracks] + [0] + minors

  for a_request in request:
    distance += abs(a_request-current_pos)
    current_pos=a_request
    if debug: print("> ", current_pos ,"seeked")
  
  average = distance / n

  return {
    "sequence": [arm_position] + request,
    "average": average,
    "distance": distance,
  }