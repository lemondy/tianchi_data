library(stringr)
#新浪微博预测，线性回归
modelpath="G:/tianchi/weibo/feature/final/"
predictpath = "G:\\tianchi\\weibo\\predict\\feature\\putTogether"
predictforwardresult = "G:\\tianchi\\weibo\\predict\\result\\glm\\forward"
predictcommentresult = "G:\\tianchi\\weibo\\predict\\result\\glm\\comment"
predictlikeresult = "G:\\tianchi\\weibo\\predict\\result\\glm\\like"

forwardformula = 'forward~activity+interest+isat+countat+url'
commentformula = 'comment~activity+interest+isat+countat+url'
likeformula = 'like~activity+interest+isat+countat+url'

LRModel<-function(modelpath,predictpath){
	modelFileList <-list.files(modelpath)
	predictFileList <- list.files(predictpath)

	for (i in 1:length(modelFileList)){
		#read data
		#字符串拼接
		modelfilepath = paste(modelpath,modelFileList[i],sep='/')
		
		data = read.csv(modelfilepath)

		predictfilepath = paste(predictpath,modelFileList[i],sep='/')
		#predictfilepath=c(predictfilepath,'.csv')
		predictdata = read.csv(predictfilepath)

		
		feature<-predictdata[,4:8]
		

		sum<-colSums(data)
		#forwad all are 0
		if(sum[6] != 0){
			forward_model<-glm(as.formula(forwardformula),family=binomial(link="logit"), data)
			forwardpredict<-predict(forward_model,feature,type="response")

			write.csv(forwardpredict,file=paste(predictforwardresult,modelFileList[i],sep="/"))
		}

		if(sum[7] != 0){
			comment_model<-glm(as.formula(commentformula),data,family=binomial(link="logit"))
			commentpredict<-predict(comment_model,feature,type="response")
			write.csv(commentpredict,file=paste(predictcommentresult,modelFileList[i],sep="/"))
		}
		
		if(sum[8] != 0){
			like_model<-glm(as.formula(likeformula),data,family=binomial(link="logit"))
			likepredict<-predict(like_model,feature,type="response")
			write.csv(likepredict,file=paste(predictlikeresult,modelFileList[i],sep="/"))
		}
	


	}
}

LRModel(modelpath,predictpath)