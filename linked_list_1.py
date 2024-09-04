class Node:
    def __int__(self,data):
        self.data=data
        self.next=None
class LL:
    def __int_(self):
        self.head=None
        self.head2=None
    def create_LL(self,n):
        while n>0:
            data=int(input('enter data:'))
            newnode = Node(data)
            if self.head== None:
                self.head = newnode
            else:
                t=self.head
                while t.next:
                    t=t.next
                t.next=newnode
            n-=1
            
    def print_LL(self,head):
        t=head
        print('linked list data:')
        while t:
            print(t.data, end='-->')
            t=t.next
        print('x')

        
    def findDuplicate(self):
        t=self.head
        dic={}
        dup_flag=0
        while t:
            if t.data not in dic:
                dic[t.data]=1
            else:
                dic[t.data]=+1
                
            if dic[t.data]>1:
                
                dup_flag=1
                break
            t=t.next
        if dup_flag==1:
            print('duplicate found')
        else:
            print('no duplicate found')

            
    def checkPalindrome(self):
        t=self.head
        s=''
        while t:
            s+=t.data
            t=t.next
        if s==s[::-1]:
            print('palindrome')
        else:
            print('not a palindrome')
        print(s)

        
    def split_LL(self):
        t=self.head
        slow=t
        fast=t
        while fast.next.next:
            slow =slow.next
            fast=fast.next.next
        self.head2=slow.next
        slow.next=None
        self.print_LL(self.head)
        self.print_LL(self.head2)

        
    def square_odd(self):
        t=self.head
        while t:
            if t.data%2 ==1:
                t.data=t.data**2
            t=t.next
        self.print_LL(self.head)
        
          
        



        
#driver
n=int(input("enter n val:"))
obj=LL()
obj.create_LL(n)
obj.print_LL(obj.head)
obj.findDuplicate()
obj.checkPalindrome()
obj.split_LL()
obj.square_odd()

