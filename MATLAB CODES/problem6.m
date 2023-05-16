clc;
close all;
n1=-2:1;
x1=[1,2,3,4];
subplot(3,1,1);
stem(n1,x1);
title('n1,x1 signal');
xlabel('n1-->');
ylabel('x1(n1)');
n2=0:3;
x2=[1,1,1,1];
subplot(3,1,2);
stem(n2,x2);
title('n2,x2 signal');
xlabel('n1-->');
ylabel('x2(n2)');
[s,t]=usermul(n1,x1,n2,x2);
subplot(3,1,3);
stem(s,t);
title('Multiplied Signal');
xlabel('s-->');
ylabel('t(s)');

function[n,w]=usermul(n1,x1,n2,x2)
n=min(min(n1),min(n2)):max(max(n1),max(n2));
y1=zeros(1,length(n));
y2=y1;
y1(((n>=min(n1))&(n<=max(n1))==1))=x1;
y2(((n>=min(n2))&(n<=max(n2))==1))=x2;
w=y1.*y2;
end
