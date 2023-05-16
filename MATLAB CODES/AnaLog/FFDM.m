clc;
close all;
t=0:0.001:1;
fm=5;
message_s=cos(2*pi*fm*t);
subplot(4,1,1);
plot(t,message_s);
xlabel('Time');ylabel('Amplitude');
title('Message Signal');
fc=100;
carrier_s=sin(2*pi*fc*t);
subplot(4,1,2);
plot(t,carrier_s);title('Carrier Signal');
xlabel('Time');ylabel('Amplitude');
mod_index= 15;
%below for fm signal
s=sin((2*pi*fc*t)+(mod_index*sin(2*pi*fm*t)));
subplot(4,1,3);
plot(t,s);xlabel('Time');ylabel('Amplitude');
title('Modulated Signal');
x=diff(s); %for differentiation use diff function
y=abs(x);
%return cutoff and n-th order coefficient for transfer the function and
%aplicable filtering.
[b,a]=butter(3,0.02);
%Finally cutoff and coeffiecient point filtering then output final signal
%output.
final= filter(b,a,y);
subplot(4,1,4);
plot(final);xlabel('Time');ylabel('Amplitude');
title('Demodulated signal')