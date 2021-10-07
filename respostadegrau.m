% Fórmulas da resposta ao Degrau

% G(s) = wn^2   /   (s^2  +   2*qsi*wn*s  +   wn^2)

%Sistema subamortecido
qsi = 0.45;
wn = 2;
sys = tf([wn^2],[1 2*qsi*wn wn^2]);

step(sys)                               %Simulação da resposta ao degrau do sistema

Mp = exp(-qsi*pi/sqrt(1-qsi^2))         % Calculo do Overshoot
Tp = pi/wn/sqrt(1-qsi^2)                % Cálculo do instante de pico
tr =(pi-acos(qsi))/wn/sqrt(1-qsi^2)     % Cálculo de tempo de subida (0% -100%)
ts = 3/qsi/wn                           % Cálculo do tempo de acomodação para 5% do valor final
        