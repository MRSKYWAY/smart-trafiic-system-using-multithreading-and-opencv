import cars as c
import multiprocessing

def lane1(result):
    result[0] +=c.givec('video.mp4')
    
def lane2(result):
    result[1] +=c.givec('video.mp4')
    
def lane3(result):
    result[2] +=c.givec('video.mp4')

def lane4(result):
    result[3] +=c.givec('video.mp4')

if __name__ == "__main__":
    global result
    ind = 0

    result = multiprocessing.Array('i', 4)
    def maxi(result):
        m=0
        index = 0
        for i in range(len(result)):
            if(m<result[i]):
                m=result[i]
                index = i
        # print(*result)
        # print(index)
        return index
    def mani(result, ind):  
        p1 = multiprocessing.Process(target=lane1, args=(result,))
        p2 = multiprocessing.Process(target=lane2, args=(result,))
        p3 = multiprocessing.Process(target=lane3, args=(result,))
        p4 = multiprocessing.Process(target=lane4, args=(result,))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        # cun=cv2.VideoCapture('display.mp4')
        while True:
            # frame1 = cun.read()
            # cv2.imshow("Video Original" , frame1)
            if(ind ==0):
                print("Green Light at lane:", ind+1)
                # cv2.putText(frame1, "Green Light at lane:", str(ind+1) , (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
                result[0] = 0
                ind = maxi(result)
                mani(result,ind)
            if(ind ==1):
                print("Green Light at lane:", ind+1)
                # cv2.putText(frame1, "Green Light at lane:", str(ind+1) , (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
                result[1] = 0
                ind = maxi(result)
                mani(result,ind)
            if(ind ==2):
                print("Green Light at lane:", ind+1)
                # cv2.putText(frame1, "Green Light at lane:", str(ind+1) , (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
                result[2] = 0
                ind = maxi(result)
                mani(result,ind)
            if(ind ==3):
                print("Green Light at lane:", ind+1)
                    # cv2.putText(frame1, "Green Light at lane:", str(ind+1) , (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
                result[3] = 0
                ind = maxi(result)
                mani(result,ind)
                # if cv2.waitKey(1) == 27:
                #             break
    mani(result, 0)
    # # for i in range(4):
    # #     result[i] = (result[i], i)

    # # def cmp(x):
    # #     return x[-1]
    
    # # result.sort(key = cmp)
    # print(result)
