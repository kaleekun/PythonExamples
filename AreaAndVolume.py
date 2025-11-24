def FindSurfaceAreaANdVolume(filepathToSTLFile):
  """Givern a filepath to a STL file, this function returns Area and Volume as a tuple."""
  with open(filepathToSTLFile) as f:
      p, area, vol = [],0, 0
      for i in f.readlines():
          if 'normal' in i or 'vertex' in i:
              p.append([float(x) for x in i.split()[-3:]])
              if len(p)%4 == 0:
                  n, v1, v2, v3 = p
                  a = ((v1[0]-v2[0])**2+(v1[1]-v2[1])**2+(v1[2]-v2[2])**2)**0.5
                  b = ((v1[0]-v3[0])**2+(v1[1]-v3[1])**2+(v1[2]-v3[2])**2)**0.5
                  c = ((v3[0]-v2[0])**2+(v3[1]-v2[1])**2+(v3[2]-v2[2])**2)**0.5
                  s = (a+b+c)/2.0
                  ap = [sum(v)/3 for v in zip(v1, v2, v3)] # calculating centroid of the triangle
                  da = (s * (s-a) * (s-b) * (s-c))**0.5 # small area
                  area = area + da
                  vol = vol + (ap[0]*n[0]+ap[1]*n[1]+ap[2]*n[2])*da/3 # gauss divergence theorem
                                                                      # Field vector taken is xi + yj + zk, whose divergence is a scalar 3.
                  p.clear()
      print(area, vol)
  return area, vol # Return this as a tuple containing 2 values - area and volume respectively.
