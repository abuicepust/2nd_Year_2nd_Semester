#Ho: mue equal 140
# and H1: mue not equal 140 
data<-c(137.4,140,138.8,139.2,144.4,139.2,141.8,137.3,133.5,138.2,141.1,139.7,136.7,136.3,135.6,138,140.9,140.6,137.7,134.1) 
n<-length(data) 
n 
x_ber<- mean(data) 
x_ber 
sample_sd<- sd(data) 
sample_sd 
mue<- 140 
t_tab<- qt(0.05, n-1) 
t_tab 
t_cal<- ((x_ber-mue)/(sample_sd/sqrt(n))) 
t_cal 
#Comments: since t_cal<t_tab, so Ho is rejected. 
#Using p-value######## 
p_value<- pt(t_cal, n-1) 
p_value 
#Comments: since p_value=0.01077929<0.05, so Ho is rejected. 
###Using function##### 
t.test(data, mu=140, conf.level=0.99, alternative="less") 
boxplot(data,ylab="Avarage capacity", col="red") 
qqnorm(data, main="Normal Q-Q plot of Hb lebel") 
