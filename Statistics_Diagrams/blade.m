%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%  Can Özgür Parlak
%  can.parlak@uni-rostock.de
%
%  Lehrstuhl für Windenergietechnik
%  Universität Rostock
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear all
close all

clc
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Schnelllaufzahl, Leistungsbeiwert
load rotorleistungsbeiwerte.mat
% aus Wilson, R. E.; Lissaman, P.B. S.:Applied Aerodynamics of Wind PowerMachines, Oregon
%State University, 1974

lambda_3blades = data_3_blades(:,1);
cp_3blades = data_3_blades(:,2);
lambda_2blades = data_2_blades(:,1);
cp_2blades = data_2_blades(:,2);
lambda_3blades = data_3_blades(:,1);
cp_3blades = data_3_blades(:,2);
lambda_1blade = data_1_blade(:,1);
cp_1blade = data_1_blade(:,2);

% max.&optimum-Werte
cp3_max = max(cp_3blades);
cp2_max = max(cp_2blades);
cp1_max = max(cp_1blade);
lambda_opt3 = lambda_3blades(cp_3blades==cp3_max);
lambda_opt2 = lambda_2blades(cp_2blades==cp2_max);
lambda_opt1 = lambda_1blade(cp_1blade==cp1_max);
[pks3,lage3] = findpeaks(cp_3blades);
[pks2,lage2] = findpeaks(cp_2blades);
[pks1,lage1] = findpeaks(cp_1blade);

%% Plotten
plot(lambda_3blades,cp_3blades,'k','LineWidth',3); grid on;
hold on
plot(lambda_2blades,cp_2blades,'b','LineWidth',3);
plot(lambda_1blade,cp_1blade,'g','LineWidth',3);
plot(lambda_3blades(lage3),pks3,'or','LineWidth',3);
plot(lambda_2blades(lage2),pks2,'or','LineWidth',3);
plot(lambda_1blade(lage1),pks1,'or','LineWidth',3);

title('Approximiertes  Cp - \lambda Kennfeld','FontSize',12,'FontWeight','bold');
xlabel('Schnelllaufzahl   \lambda','FontSize',12,'FontWeight','bold');
ylabel('Leistungsbeiwert  Cp','FontSize',12,'FontWeight','bold');
legend('3-Blatt-Rotor','2-Blatt-Rotor','1-Blatt-Rotor')
hold off

tabelle = zeros(3,3);
tabelle(1,1) = cp1_max;
tabelle(2,1) = cp2_max;
tabelle(3,1) = cp3_max;
tabelle(1,2) = lambda_opt1;
tabelle(2,2) = lambda_opt2;
tabelle(3,2) = lambda_opt3;
tabelle(1,3) = 1;
tabelle(2,3) = 2;
tabelle(3,3) = 3;

fprintf(' \n'); 
fprintf('  Cp-max\t lambda-Opt\t Blattanzahl \n')
disp('-----------------------------------------')
fprintf('%10f\t %10f\t    %0d\n',tabelle');
fprintf(' \n');