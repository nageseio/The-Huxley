def VolumeEsfera(r):
  pi=3.1416
  volume=((4*pi)*(r**3))/3
  return volume
for i in range(0,3):
 r=float(input())
 print("%.2f"%VolumeEsfera(r))
