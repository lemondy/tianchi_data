#读入数据
purchase_amt<-read.csv("C:/Users/lemon/Desktop/tianchi-second/lm/R_test_lm_purchase.csv")
redeem_amt<-read.csv("C:/Users/lemon/Desktop/tianchi-second/lm/R_test_lm_redeem.csv")

purchase_amt<-purchase_amt[,-16]


#PCA 分析
#library(psych)
#fa.parallel(purchase_amt[,-1],fa="PC",n.iter=100,show.legend=FALSE,main="Screen plot with parallel analysis")

#回归方程变量选择
purchase_formulaStr<-"purchase_amt~Monday+Tuesday+Wednesday+Thursday+Friday+Saturday+Sunday+head_one_week_month+head_two_week_month+tail_one_week_month+tail_two_week_month+holiday+workday+weekend"
redeem_formulaStr<-"redeem_amt~Monday+Tuesday+Wednesday+Thursday+Friday+Saturday+Sunday+head_one_week_month+head_two_week_month+tail_one_week_month+tail_two_week_month+holiday+workday+weekend"

#leaps<-regsubsets(as.formula(purchase_formulaStr),data=purchase_amt,nbest=3)

purchase_formulaStr<-"purchase_amt~Monday+Tuesday+Wednesday+Thursday+Friday+Saturday+Sunday+head_one_week_month+head_two_week_month+tail_one_week_month+tail_two_week_month+holiday"
#回归方程实现
purchase_model<-lm(as.formula(purchase_formulaStr), purchase_amt, interval="prediction")
redeem_model<-lm(as.formula(redeem_formulaStr), redeem_amt, interval="prediction")

#purchase_glm<-glm(as.formula(purchase_formulaStr),data=purchase_amt,family=binomial(link="logit"))

#purchase_glm_predict<-predict(purchase_glm,feature9)
#查看模型效果
summary(purchase_model)
summary(redeem_model)

#优化，调整参数
purchase_model_step<-step(purchase_model)
redeem_model_step<-step(redeem_model)

summary(purchase_model_step)
#强影响点查看
influence.measures(purchase_model_step)
influence.measures(redeem_model_step)

#残差分析
purchase_model_step_rst<-rstandard(purchase_model_step)
purchase_model_step_fit<-predict(purchase_model_step)
#下面画出的图比较好的情况是随机分布在-2到+2的带状区域内
plot(purchase_model_step_fit~purchase_model_step_rst)

redeem_model_step_rst<-rstandard(redeem_model_step)
redeem_model_step_fit<-predict(redeem_model_step)
plot(redeem_model_step_fit~redeem_model_step_rst)

#异常点查看,查看标准化残差开方与拟合值的残差图或者查看cook统计量的残差图，就可知道异常点
plot(purchase_model_step,which=1:4)
plot(redeem_model_step,which=1:4)

feature9<-read.csv("C:/Users/lemon/Desktop/tianchi-second/feature9.csv")
 purchase_predict<-predict(purchase_model_step,feature9,interval="prediction",level=0.95,set.fit=FALSE) 
 redeem_predict<-predict(redeem_model_step,feature9,interval="prediction",level=0.95,set.fit=FALSE) 


purchase_formulaStr<-"purchase_amt~Tuesday+Friday+Saturday+head_one_week_month+head_two_week_month+tail_two_week_month+holiday+workday"


#20150711 检测出来回归方程中存在异方差
library(lmtest)
gqtest(purchase_model)

bptest(purchase_model)

#修正异方差
lm.test<-lm(log(resid(purchase_model)^2)~Monday+Tuesday+Wednesday+Thursday+Friday+Saturday+Sunday+head_one_week_month+head_two_week_month+tail_one_week_month+tail_two_week_month+holiday+workday+weekend,purchase_amt)

lm.test2<-lm(as.formula(purchase_formulaStr),weights=1/exp(fitted(lm.test)),purchase_amt)

#检验多重共线性,计算解释变量相关稀疏矩阵的条件数k，k<100多重共线性程度很小，100<k<1000较强，>1000严重
xx<-cor(purchase_amt[,2:15])
kappa(xx)

#寻找共线性强的解释变量组合
eigen(xx)
#step函数即可寻找最强解释变量组合


("20140405","20140406","20140412","20140413","20140419","20140420","20140426","20140427",
	"20140503","20140504","20140510","20140511","20140517","20140518","20140524","20140525",
	"20140531","20140601","20140607","20140608","20140614","20140615","20140621","20140622"
	,"20140628","20140629","20140705","20140706","20140712","20140713","20140719","20140720",
	"20140726","20140727","20140802","20140803","20140809","20140810","20140816","20140823",
	"20140824","20140830","20140831")