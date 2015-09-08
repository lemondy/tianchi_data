#
import os,math

def isExist(data,element):
    for i in data:
        if i == element:
            return True

    return False


notInTrainpath = r'C:\Users\lemon\Desktop\weibo\userNotInTrain.txt'
trainpath = r'C:\Users\lemon\Desktop\weibo\user-train'
output = r'C:\Users\lemon\Desktop\weibo\average2.txt'

def average():
    notInTrainUser = [line.strip() for line in open(notInTrainpath)]
    out = open(output,'ab')
    forwards = []
    comments = []
    likes = []
    
    #for i in notInTrainUser:
        #print i
    for root,dirnames,filenames in os.walk(trainpath):
        for filename in filenames:
            name = filename.split('.')
            weibo_count = 0
            if isExist(notInTrainUser,name[0]) == False:
                print 'read file',filename
                userfile = open(trainpath+'\\'+filename,'r')
                for line in userfile.readlines():
                    weibo_count = weibo_count + 1
                    line_split = line.split('\t')
                    forwards.append(int(line_split[3]))
                    comments.append(int(line_split[4]))
                    likes.append(int(line_split[5]))
                
                forwards_sum = 0
                comments_sum =0
                likes_sum = 0
                for i in forwards:
                    forwards_sum = forwards_sum + i
                    #print i
                for j in comments:
                    comments_sum = comments_sum + j
                    #print i
                for k in likes:
                    likes_sum = likes_sum + k
                print 'forwards_sum '+str(forwards_sum)+' comments_sum '+str(comments_sum)+' likes_sum '+str(likes_sum)
                average_forward = math.ceil(forwards_sum/weibo_count) 
                average_comment = math.ceil(comments_sum/weibo_count) 
                average_like = math.ceil(likes_sum/weibo_count) 
                out.write(name[0]+'\t'+str(int(average_forward))+'\t'+str(int(average_comment))+'\t'+str(int(average_like))+'\n')
                
                forwards = []
                comments = []
                likes = []
                    
                average_forward = 0
                average_comment = 0
                average_like = 0



    

average()
