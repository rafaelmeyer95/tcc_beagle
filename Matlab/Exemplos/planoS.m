% O Plano-s

% G(s) = k * (s + a) / ((s+b)   *   (s+c)) 
%       a<b<c

sys = zpk([-10],[-5 -4], [2])   % Cria uma função de transferência a partir dos pólos, zeros e ganho da função

figure(1)
pzplot(sys)         % Mapa de pólos e zeros no plano-s da função de transferência


sys = tf([-5 25],[1 6 25])      % Função de transferência com polos complexos com parte real negativa e um zero no semiplano da direita

figure(2)
pzplot(sys)         % Mapa de pólos e zeros no plano-s da função de transferência

roots([1 6 25])     % Retorna as raízes do polinômio


