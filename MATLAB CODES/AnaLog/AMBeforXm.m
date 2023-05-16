clc;
close all;
t=0:0.001:2;
fm=5;
m=sin(2*pi*fm*t);
subplot(5,1,1);
plot(t,m);
title('Message signal');
xlabel('Time(s)');
ylabel('Amplitude');
fc=50;
c=sin(2*pi*fc*t);
subplot(5,1,2);
plot(t,c);
title('Carrier Signal');
xlabel('Time(s)');
ylabel('Amplitude');
ma=0.5;
s1=(1+ma*m).*c;
subplot(5,1,3);
plot(t,s1);
title('UnderModulated signal');
xlabel('Time(s)');
ylabel('Amplitude');
m1=1;
s2=(1+m1*m).*c;
subplot(5,1,4);
plot(t,s2);
title('CriticalModulated signal');
xlabel('Time(s)');
ylabel('Amplitude');
m2=1.5;
s3=(1+m2*m).*c;
subplot(5,1,5);
plot(t,s3);
axis([0,2,-2,2]);
title('OverModulated signal');
xlabel('Time(s)');
ylabel('Amplitude');