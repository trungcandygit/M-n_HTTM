%% Hình minh họa khác biệt kép, dựng theo đúng figures.m của pmichaillat/matlab-figures
% Phần thiết lập giữ nguyên template; chỉ thay dữ liệu. Chuỗi là MINH HỌA (ngẫu nhiên có seed), không phải dữ liệu.
% Template ghi nhãn bằng Keynote sau khi xuất PDF, nên code không ghi nhãn.

%% Clear workspace

close all
clear
clc

%% Set default properties for 4:3 figure

figureWidth = 8.5;
figureHeight = 6.375;
set(groot, 'defaultFigureUnits', 'inches')
set(groot, 'defaultFigurePosition', [1,1,figureWidth,figureHeight]);
set(groot, 'defaultFigurePaperPosition', [0, 0, figureWidth,figureHeight]);
set(groot, 'defaultFigurePaperSize', [figureWidth,figureHeight]);

%% Set default properties for axes

set(groot, 'defaultAxesFontName', 'Helvetica')
set(groot, 'defaultAxesFontSize', 24)
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

%% Predefine qualitative color palettes

darkPalette = ['#1b9e77';'#d95f02';'#7570b3';'#e7298a';'#66a61e';'#e6ab02';'#a6761d';'#666666'];
orangeColor = darkPalette(2,:);
purpleColor = darkPalette(3,:);

%% Create data (minh họa, theo tháng 2020-2028)

rng(7)
time = [2020:1/12:2029]';
event = 2027;
pre = time < event;

% Hai chuỗi nhấp nhô kiểu bước ngẫu nhiên có quay về trung bình
shock = @() filter(1, [1 -0.85], 0.06*randn(size(time)));
control = 0.45 + shock();                       % mã HOSE đối sánh
treated = 0.85 + shock();                       % mã chuyển sàn
counterfactual = treated;                       % nếu không chuyển sàn
treated(~pre) = treated(~pre) - 0.30;           % sau chuyển sàn: thanh khoản tốt hơn, Amihud thấp hơn

%% Predefine properties for x-axis

clear obj
obj.XLim = [2020, 2029];
obj.XTick = [2020:3:2029];
xAxis = [fieldnames(obj), struct2cell(obj)]';

%% Predefine properties for y-axis

clear obj
obj.YLim = [0, 1.4];
obj.YTick = [0:0.2:1.4];
obj.YTickLabel = {};
yAxis = [fieldnames(obj), struct2cell(obj)]';

%% Predefine properties for lines

clear obj
obj.Color = purpleColor;
obj.LineWidth = 3;
obj.LineStyle = '-';
purpleLine = [fieldnames(obj), struct2cell(obj)]';

clear obj
obj.Color = purpleColor;
obj.LineWidth = 3;
obj.LineStyle = ':';
purpleDotted = [fieldnames(obj), struct2cell(obj)]';

clear obj
obj.Color = orangeColor;
obj.LineWidth = 3;
obj.LineStyle = '-';
orangeLine = [fieldnames(obj), struct2cell(obj)]';

%% Predefine properties for period areas

clear obj
obj.FaceColor = 'black';
obj.LineStyle = 'none';
obj.FaceAlpha = 0.2;
periodArea = [fieldnames(obj), struct2cell(obj)]';

%% Plot

iFigure = 1;
figure(iFigure)
clf
hold on

% Giai đoạn chuyển tiếp 7/2025-12/2026: loại khỏi kiểm định chính
xregion(2025.5, 2027, periodArea{:});

% Vùng tác động (cách tô higher_lower.pdf của template)
post = ~pre;
a = area(time(post), [treated(post), counterfactual(post) - treated(post)], 'LineStyle', 'none');
a(1).FaceAlpha = 0;
a(2).FaceAlpha = 0.2;
a(2).FaceColor = purpleColor;

plot(time(post), counterfactual(post), purpleDotted{:})
plot(time, control, orangeLine{:})
plot(time, treated, purpleLine{:})

%Populate axes
set(gca, xAxis{:}, yAxis{:})
ylabel('Amihud (log)')

%Print figure
print('-dpdf', 'did_matlab.pdf')
