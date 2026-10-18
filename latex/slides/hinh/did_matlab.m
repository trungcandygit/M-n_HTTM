%% Hình minh họa thiết kế khác biệt kép theo template pmichaillat/matlab-figures
% Chạy trong MATLAB R2023a trở lên (cần hàm xregion). Kết quả: did_matlab.pdf cùng thư mục.
% Chuỗi được sinh bằng hàm tất định, giống hinh/taodulieu.py: đây là HÌNH MINH HỌA, KHÔNG PHẢI DỮ LIỆU.
% Template gốc ghi nhãn bằng Keynote. Ở đây nhãn ghi bằng text(); nếu muốn đúng quy trình template,
% đặt showLabels = false rồi tự ghi nhãn trong Keynote hoặc PowerPoint.

%% Clear workspace

close all
clear
clc

showLabels = true;

%% Set default properties for 4:3 figure (giữ nguyên thông số của template)

figureWidth = 8.5;
figureHeight = 6.375;
set(groot, 'defaultFigureUnits', 'inches')
set(groot, 'defaultFigurePosition', [1,1,figureWidth,figureHeight]);
set(groot, 'defaultFigurePaperPosition', [0, 0, figureWidth,figureHeight]);
set(groot, 'defaultFigurePaperSize', [figureWidth,figureHeight]);

%% Set default properties for axes

% Nếu Helvetica trên máy thiếu dấu tiếng Việt, đổi thành 'Arial'
fontName = 'Helvetica';
set(groot, 'defaultAxesFontName', fontName)
set(groot, 'defaultTextFontName', fontName)
set(groot, 'defaultAxesFontSize', 24)
set(groot, 'defaultTextFontSize', 24)
set(groot, 'defaultAxesLabelFontSizeMultiplier', 1)
set(groot, 'defaultAxesTitleFontSizeMultiplier', 1)
set(groot, 'defaultAxesTitleFontWeight', 'normal')
set(groot, 'defaultAxesXColor', 'k')
set(groot, 'defaultAxesYColor', 'k')
set(groot, 'defaultAxesGridColor', 'k')
set(groot, 'defaultAxesLineWidth', 1)
set(groot, 'defaultAxesYGrid', 'on')
set(groot, 'defaultAxesXGrid', 'off')
set(groot, 'defaultAxesTickDirMode', 'manual')
set(groot, 'defaultAxesTickDir', 'out')
set(groot, 'defaultAxesTickLength',[0.005, 0.005])
set(groot, 'defaultAxesBox','off')

%% Colors (bảng Dark2 của template)

orangeColor = '#d95f02';
purpleColor = '#7570b3';

%% Create illustrative series (theo tháng, 1/2024 đến 1/2029)

k = (0:60)';
time = 2024 + k/12;
noise = @(k,s) 0.016*sin(1.31*k+s) + 0.011*sin(0.47*k+2.1*s) + 0.007*sin(2.93*k+0.7*s);
event = 2027;
pre = time <= event;
post = time >= event;

control = 0.55 - 0.02*(time-2024) + noise(k,1.9);              % mã HOSE đối sánh
treatedPre = 1.05 - 0.02*(time(pre)-2024) + noise(k(pre),0.3);  % mã chuyển sàn, trước
treatedPost = 0.75 - 0.02*(time(post)-2024) + noise(k(post),0.3); % mã chuyển sàn, sau
counterfactual = 1.05 - 0.02*(time(post)-2024);                % nếu không chuyển sàn

%% Predefine properties for axes

clear obj
obj.XLim = [2024, 2029];
obj.XTick = [2024:1:2029];
obj.XTickLabel = {'2024','','2026','2027','2028','2029'};
xAxis = [fieldnames(obj), struct2cell(obj)]';

clear obj
obj.YLim = [0.2, 1.4];
obj.YTick = [0.2:0.3:1.4];
obj.YTickLabel = {};
yAxis = [fieldnames(obj), struct2cell(obj)]';

%% Predefine properties for lines and areas

clear obj
obj.Color = purpleColor;
obj.LineWidth = 3;
obj.LineStyle = '-';
purpleLine = [fieldnames(obj), struct2cell(obj)]';

clear obj
obj.Color = purpleColor;
obj.LineWidth = 2;
obj.LineStyle = '--';
purpleDashed = [fieldnames(obj), struct2cell(obj)]';

clear obj
obj.Color = orangeColor;
obj.LineWidth = 3;
obj.LineStyle = '-';
orangeLine = [fieldnames(obj), struct2cell(obj)]';

clear obj
obj.FaceColor = 'black';
obj.LineStyle = 'none';
obj.FaceAlpha = 0.2;
periodArea = [fieldnames(obj), struct2cell(obj)]';

%% Plot

figure(1)
clf
hold on

% Giai đoạn chuyển tiếp 7/2025 đến 12/2026, bị loại khỏi kiểm định chính
xregion(2025.5, 2027, periodArea{:});

% Vùng tác động: giữa đường "nếu không chuyển sàn" và đường thực tế sau sự kiện
a = area(time(post), [treatedPost, counterfactual - treatedPost], 'LineStyle', 'none');
a(1).FaceAlpha = 0;
a(2).FaceAlpha = 0.2;
a(2).FaceColor = purpleColor;

plot(time(post), counterfactual, purpleDashed{:})
plot(time, control, orangeLine{:})
plot(time(pre), treatedPre, purpleLine{:})
plot(time(post), treatedPost, purpleLine{:})

set(gca, xAxis{:}, yAxis{:})
ylabel('Độ phi thanh khoản (log)')

if showLabels
    text(2024.05, 1.20, 'Mã chuyển sàn', 'Color', purpleColor)
    text(2024.05, 0.36, 'Mã HOSE đối sánh', 'Color', orangeColor)
    text(2028.0, 1.30, 'Tác động', 'Color', purpleColor, 'HorizontalAlignment', 'center')
    quiver(2028.0, 1.25, 0.1, -0.37, 0, 'Color', purpleColor, 'LineWidth', 1, 'MaxHeadSize', 0.4)
    text(2029.05, 0.92, {'Nếu không','chuyển sàn'}, 'Color', purpleColor)
end

%% Print figure

print('-dpdf', 'did_matlab.pdf')

% Đưa vào slide: trong slides.tex thay \input{hinh/did.tex} bằng
%   \includegraphics[width=0.62\textwidth]{hinh/did_matlab.pdf}
% (template đặt hình bằng \includegraphics, chú thích bằng \caption như hiện tại).
