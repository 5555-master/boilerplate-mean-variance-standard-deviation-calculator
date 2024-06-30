import numpy as np

def calculate(l):
  if len(l) < 9 :
    raise ValueError("List must contain nine numbers.")
  else:
    calculations = {
    'mean': [],
    'variance': [],
    'standard deviation': [],
    'max': [],
    'min': [],
    'sum': []
    }
    l = np.array(l)
    l=l.reshape(3,3)
    calculations["mean"].append(list(np.mean(l,0)))
    calculations["mean"].append(list(np.mean(l,1)))
    calculations["mean"].append(np.mean(l))
    calculations["variance"].append(list(np.var(l,0)))
    calculations["variance"].append(list(np.var(l,1)))
    calculations["variance"].append(np.var(l))
    calculations["standard deviation"].append(list(np.std(l,0)))
    calculations["standard deviation"].append(list(np.std(l,1)))
    calculations["standard deviation"].append(np.std(l))
    calculations["max"].append(list(np.max(l,0)))
    calculations["max"].append(list(np.max(l,1)))
    calculations["max"].append(np.max(l))
    calculations["min"].append(list(np.min(l,0)))
    calculations["min"].append(list(np.min(l,1)))
    calculations["min"].append(np.min(l))
    calculations["sum"].append(list(np.sum(l,0)))
    calculations["sum"].append(list(np.sum(l,1)))
    calculations["sum"].append(np.sum(l))




    return calculations

