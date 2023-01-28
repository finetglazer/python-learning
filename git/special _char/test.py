x=[1.2,2.3,3.4,4.5,5.6,6.7,7.8,8.9]
y=[9.8,8.7,7.6,8.5,5.4,4.3,3.2,2.1]
def dis(x,y):
  ans=0
  for i in range(0,len(x)):
      ans+=abs(x[i]-y[i])
  return ans
ans=dis(x,y)
print(ans)