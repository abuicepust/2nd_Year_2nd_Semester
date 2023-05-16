#H0: mui=14.6
#Ha: mui<14.6

data<- c(12.3,11.4,14.2,15.3,14.8,13.8,11.1,15.1,15.8,13.2);
n<-length(data);
n;
x_bar<-mean(data);
x_bar;
sample_sd<-sd(data);
sample_sd;
mui<-14.6;
t_tab<-qt(0.01,n-1);
t_tab;
t_cal<-((x_bar-mui)/(sample_sd/sqrt(n)));
t_cal;
p_value<-pt(t_cal,n-1);
p_value;
boxplot(data,main="Boxplot",ylab="Hblevel");
qqnorm(data,main="Normal plot of Hb level");
qqline(data);