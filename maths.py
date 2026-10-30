length = float(input("Enter rectangle length (cm):"))
breadth = float(input("Enter rectangle breadth (cm):"))

if length > 0 and breadth > 0:
   area = length * breadth
   perimeter = 2 * (length + breadth)
   print(f"Area : {area:.2f} sq. cm")
   print(f"Perimeter : {perimeter:.2f} cm")
else:
   print("Length and breadth must be positive.")