Height<-c(178,182,183,172,177,161,163,185,143,157,171,182,182,178,157,165,153,178,164,168,180,166,192,182,172,164,163,182,165,141,157,158,188,168,161,158,160,162,163,170,171,183,173,160,178,171,159,170,190,179,159,173,160,174,179,172,176,181,171,186,155,165,175,191,169,179,166,184,181,166,158,168,165,168,155,185,196,145,153,163,172,163,177,184,165,156,140,202,162,157,176,176,171,166,185,171,184,173,174,162)
p<-length(Height)
p
#a)..........
#Population average
Average<-mean(Height)
Average #170.19
#Standard deviation......
sigma<-sd(Height)
sigma #11.85833
#b)..........
set.seed
x<-sample(Height,20,replace=TRUE)
x
y<-mean(x)
y #Point Estimator for Mean = 172.7
#c)..........
choose(100,20) #5.3598e+20
set.seed(125)
#a<-rep(0,53598)
#for(i in 1:53598){
#meanx[i]<-mean(sample(Height,20,replace=TRUE))}
#mean(meanx) #Expected value E(x ber)= 170.1931
#mean(Height) #population mean
#bais=mean(meanx)-mean(Height)
#bais #bias is 0.003123811 that is almost zero, so Sampling mean or (x ber) is an unbiased estimator of
#population mean µ.
#hist(a)
#qqnorm(a)
#qqline(a)
#Comment: Sampling mean is an unbiased estimator of population mean. 
meanx<-rep(0,50000);
for(i in (1:50000)){
meanx[i]<-mean(rnorm(100,0,1))
}
mean(meanx);
s<-sd(meanx);
s;
hist(meanx);






####d)............

n= ((2*1.96*sigma)/2)^2 
n # Probable Sample size will be 540.2062
pnorm(-1.96,0,1) #0.0249979

####e)............
x<-sample(Height,20,replace=TRUE)
y<-mean(x) #168.5
#Interval estimation 
qnorm(0.025,0,1) #1.96

#lower class interval
y-(1.96*sigma)/sqrt(100)  #166.1758

#upper class interval
y+(1.96*sigma)/sqrt(100) #170.8242
#99% Confidence interval for population mean is(166.1758, 170.8242)


