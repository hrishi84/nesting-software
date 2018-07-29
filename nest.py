from graphics import*
import numpy as np
def main():
    
    l = np.zeros([100] ,np.uint32)
    b = np.zeros([100] ,np.uint32)
    r = np.zeros([100] ,np.uint32)
    area = np.zeros([100] ,np.uint32)
    area_sum=0
    i = np.zeros([100] ,np.uint32)
    j = np.zeros([100] ,np.uint32)

    print "Enter the dimensions of sheet"
    l1 = int(raw_input("Enter the length of sheet"))
    b1 = int(raw_input("Enter the breadth of sheet"))
    #l1 = 450
    #b1 = 500
    sheet_area = l1*b1


    #input number of shapes
    n = int(raw_input("Enter no of shapes "))

    #input shapes
    
    for i in range(0,n):
        
        l[i] = int(raw_input("enter length : "))
        b[i] = int(raw_input("enter breadth : "))
        area[i] = l[i]*b[i]
        area_sum = area_sum + area[i]
        print "\n"
        if(l[i]<b[i]):
            l[i],b[i]=b[i],l[i]
        


    for i in range(0,n):
        for j in range(0,n-1):
            if(l[j]<l[j+1]):
                  temp=area[j]
                  area[j]=area[j+1]
                  area[j+1]=temp

                  temp=l[j]
                  l[j]=l[j+1]
                  l[j+1]=temp

                  temp=b[j]
                  b[j]=b[j+1]
                  b[j+1]=temp


                  
    if(area_sum < sheet_area ):
        win = GraphWin("My Window", 1000, 1000)
        win.setBackground('black')

        
        rect = Rectangle(Point(10,10),Point(10+l1,10+b1))
        rect.setFill('white')
        rect.draw(win)

        #aLine = Line(Point(0,0),Point(50,60))
        #aLine.setWidth(20)
        #aLine.setFill('red')

        x=0
           # for x in range(0,3):
       # if(a[x] <(l1/4)):
        p=0
        q=0
        z=0
        w=0
        
        for x in range(0,n):
            if(x>=n):
                break
            rect = Rectangle(Point(10+p,10+q),Point(10+b[x]+p,10+l[x]+q))
            
            #print " x = ",
            #print x
            #print " n = ",
#            print n
#            print " (l,b) = ",
#            print l[x],
#            print ", ",
#            print b[x],
#            print ")"
            print 10+p,10+q
            print 10+b[x],10+q
            print 10+b[x],10+l[x]
            print 10+p,10+l[x]
            print 10+p,10+q
            print "\n"
    
            rect.setFill(color_rgb(10+z,10+z,10+z))
            rect.draw(win)
            z=z+10                                                  #rgb incrementer
            if(p==0):
                s=x
            p= p+b[x]+5     #x incrementer
                #y incrementer
            if(p+b[x+1]>l1):
                
                i=2
                while(p+b[x+i] > l1):
                    i=i+1

                if((i>2) & (x+i<n)):
#                    print " i = ",
 #                   print i
  #                  print " x+i = ",
#                    print x+i
#                    print " n = ",
#                    print n
#                    print " (l,b) = ",
#                    print l[x+i],
#                    print ", ",
#                    print b[x+i],
#                    print ")"
                    print 10+p,10+q
                    print 10+b[x+i],10+q
                    print 10+b[x+i],10+l[x+i]
                    print 10+p,10+l[x+i]
                    print 10+p,10+q
                    print "\n"
                    rect = Rectangle(Point(10+p,10+q),Point(10+b[x+i]+p,10+l[x+i]+q))
                    rect.setFill(color_rgb(10+z,10+z,10+z))
                    rect.draw(win)
                    z=z+10  

                    for j in range(i,n-1):
                        b[x+i]=b[x+i+1]
                        l[x+i]=l[x+i+1]
                        area[x+i]=area[x+i+1]

                    n=n-1

                q=q+l[s]+10                 #y incrementer
                p=0
                
                
        win.getMouse()
        win.close()
main()
                      

