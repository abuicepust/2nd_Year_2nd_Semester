x_bar<-6.7;
mue<-5;
sd<-7.1;
n<-29;
alpha<-0.05;
z_tab<-qnorm(0.05,lower.tail=FALSE);
z_tab;
z_cal<-(x_bar-mue)/(sd/sqrt(n));
z_cal;
p_value<-pnorm(z_cal,lower.tail=FALSE);
p_value;