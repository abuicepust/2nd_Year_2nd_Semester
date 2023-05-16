clc;
close all;
A=input('Enter Amplitude of transmitting signal: ');
f=50;
T=1/f;
t=0:T/100:2*T;
y=A*sin(2*pi*f*t);
subplot(4,1,1);
plot(t,y,'r','Linewidth',3);
title('Transmitting signal');
xlabel('Time');
ylabel('Amplitude');

n=1:1:40;
y1=A*sin(2*pi*f*(.001)*n);
subplot(4,1,2);
stem(n,y1);
title('Discrete Time signal after sampling');
xlabel('Time');
ylabel('Amplitude');

y2=A+y1;
subplot(4,1,3);
stem(n,y2);
title('DC level+Discrete Time signal');
xlabel('Time');
ylabel('Amplitude');

y3=round(y2);
subplot(4,1,4);
stem(n,y3);
title('Quantized Signal');
xlabel('Time');
ylabel('Amplitude');

y4=dec2bin(y3);
disp('Binary Information: ')
disp(y4);