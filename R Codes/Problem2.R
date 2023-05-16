#OPutcomes of two dices(s)
s=2:12;

#Vector of probabilities
PS=c(1:6,5:1)/36;

#Expectation of s[E(s)=Sum(s*PS)

ES=sum(s*PS);
ES; #ES is 7

#Variance of S
Esqr=sum(s*s*PS);
Esqr;
vs=(Esqr-(ES^2));
vs;
par(mfrow=c(1,2));
barplot(PS,
ylim=c(0,0.2),
xlab="S",
ylab="Probabilities",
col="White",
space=0,
main="Sum of two dice rolls")

pr=rep(1/6,6);
names(pr)=1:6;
barplot(pr,
ylim=c(0,0.2),
xlab="D",
ylab="Probabilities",
col="white",
space=0,
main="Outcomes of a single dice rolls")