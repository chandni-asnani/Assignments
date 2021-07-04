from base import Base
class Armstrong(Base):

    def run(self):
        arm= list(str(self.number))
        count = 0
        for i in arm:
            i = pow(int(i),3)
            count+= int(i)
            #print(count)
        if count == self.number:
            return True
        else:
            return False
            