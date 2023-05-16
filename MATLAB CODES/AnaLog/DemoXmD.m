clc;
close all;
t=0:0.0001:1;
fm=10;
fc=100;
mf=8;
fd=mf*fm;
m=cos(2*pi*fm*t);
c=sin(2*pi*fc*t);
subplot(5,1,1);
plot(t,m);
title('Message Signal');
xlabel('Time');
ylabel('Amplitude');
subplot(5,1,2);
plot(t,c);
title('Carrier Signal');
xlabel('Time');
ylabel('Amplitude');
s=sin((2*pi*fc*t)+mf.*(sin(2*pi*fm*t)));
subplot(5,1,3);
plot(t,s);
title('FrequencyModulation Signal');
xlabel('Time');
ylabel('Amplitude');
x=diff(s);
y=abs(x);
[b,a]=butter(3,0.023);
final=filter(b,a,y);
subplot(5,1,4);
plot(final);
title('Demod Signal');
xlabel('Time');
ylabel('Amplitude');

