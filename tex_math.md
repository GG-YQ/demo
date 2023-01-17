- [行内与独行](#行内与独行)
- [上下标与组合](#上下标与组合)
- [定界符与组合](#定界符与组合)
- [运算](#运算)
- [逻辑运算](#逻辑运算)
- [集合运算](#集合运算)
- [数学符号](#数学符号)
- [其他](#其他)
  - [max](#max)
  - [方程式](#方程式)
  - [矩阵](#矩阵)
  - [等号对齐](#等号对齐)
  - [希腊字母](#希腊字母)


[katex语法](https://katex.org/docs/supported.html)
# 行内与独行
行内公式：将公式插入到本行内，如：$xyz$
独行公式：将公式插入到新的一行内，并且居中，如：$$xyz$$
展示样式：\displaystyle，独行公式默认；\textstyle，行内公式默认，在公式开始指定displaystyle即可修改，$\displaystyle \sum_{x>0}$、$\sum_{x>0}$
# 上下标与组合
上下标：$x_1^2$
组：一个组即单个字符或者使用{}包裹起来的内容，$x^{5^6}$
下划线符号，符号：$\underline{x+y}$
公式标签，符号：\tag{数字}，如：$$x+y=z \tag{1}$$
上大括号，符号：$\overbrace{a+b+c+d}^{2.0}$
下大括号，符号：$a+\underbrace{b+c}_{1.0}+d$
上位符号，符号：\stacrel{小字号的上位符号}{正常字号的基位符号}，如：$\vec{x}\stackrel{def}{=}{x_1,\dots,x_n}$
空格，符号：$x \! y$；$xy$；$x \ y$；$x \quad y$；$x \qquad y$
# 定界符与组合
括号，符号：$（）\big(\big) \Big(\Big) \bigg(\bigg) \Bigg(\Bigg)$
中括号，符号：$[x+y]$
大括号，符号：由于大括号{} 被用于分组，因此需要使用$\{$和$\}$表示大括号，也可以使用$\lbrace$和$\rbrace$来表示。${x+y}+\{x+y\}$
尖括号：区分于小于号和大于号，$\langle$和$\rangle$
自适应括号，符号：\left \right，$\left(x^{y^{z^w}}\right)$；单边自适应，$\left(x^{y^{z^w}}\right.$
组合公式，符号：${n+1 \choose k}={n \choose k}+{n \choose k-1}$
组合公式，符号：${上位公式 \atop 下位公式}，
$$
\sum_{k_0,k_1,\ldots>0 \atop k_0+k_1+\cdots=n}A_{k_0}A_{k_1}\cdots$

# 运算
基本运算，符号：$+ - \pm \mp \times \cdot \div$
分式表示，符号：\tfrac 设置分数为 textstyle；\dfrac 设置分数为 displaystyle；\frac 根据上下文决定使用 \tfrac 还是 \dfrac；\cfrac 用于表示连续分数。$\frac{x+y}{y+z}$
分式表示，符号：${x+y} \over {y+z}$
绝对值表示，符号：$|x+y|$
平均数运算，符号：$\overline{xyz}$
开二次方运算，符号：$\sqrt x$
开方运算，符号：$\sqrt[x]{y}$
对数运算，符号：$\log(x)$；$\log_28$；
极限运算，符号：$\lim^{x \to \infty}_{y \to 0}{\frac{x}{y}}$
极限运算，符号：$\displaystyle \lim^{x \to \infty}_{y \to 0}{\frac{x}{y}}$；
求和运算，符号：$\sum^{x \to \infty}_{y \to 0}{\frac{x}{y}}$
求和运算，符号：$\displaystyle \sum^{x \to \infty}_{y \to 0}{\frac{x}{y}}$
求积运算，符号：$\prod^{x \to \infty}_{y \to 0}{\frac{x}{y}}$；$\coprod$
积分运算，符号：$\int^{\infty}_{0}{xdx}$；$\iint$；$\iiint$；$\oint$
积分运算，符号：$\displaystyle \int^{\infty}_{0}{xdx}$
微分运算，符号：$\frac{\partial x}{\partial y}$
矩阵表示，符号：\begin{matrix} \end{matrix}，
$$
\left[ 
    \begin{matrix} 
    1 & 2 & \cdots &4\\
    5 & 6 & \cdots &8\\
    \vdots & \vdots & \ddots & \vdots\\
    9 & 10 & \cdots & 11
    \end{matrix} 
\right]
$$
下三角：$\nabla$

# 逻辑运算
等于运算，符号：=，如：$x+y=z$
大于运算，符号：>，如：$x+y>z$
小于运算，符号：<，如：$x+y<z$
大于等于运算，符号：\geq，如：$x+y \geq z$
小于等于运算，符号：\leq，如：$x+y \leq z$
不等于运算，符号：\neq，如：$x+y \neq z$
不大于等于运算，符号：\ngeq，如：$x+y \ngeq z$
不大于等于运算，符号：\not\geq，如：$x+y \not\geq z$
不小于等于运算，符号：\nleq，如：$x+y \nleq z$
不小于等于运算，符号：\not\leq，如：$x+y \not\leq z$
约等于运算，符号：\approx，如：$x+y \approx z$
恒定等于运算，符号：\equiv，如：$x+y \equiv z$

# 集合运算
元素：$\exists$；$\forall$
属于运算，符号：\in，如：$x \in y$
不属于运算，符号：\notin，如：$x \notin y$
不属于运算，符号：\not\in，如：$x \not\in y$
子集运算，符号：\subset，如：$x \subset y$
子集运算，符号：\supset，如：$x \supset y$
真子集运算，符号：\subseteq，如：$x \subseteq y$
非真子集运算，符号：\subsetneq，如：$x \subsetneq y$
真子集运算，符号：\supseteq，如：$x \supseteq y$
非真子集运算，符号：\supsetneq，如：$x \supsetneq y$
非子集运算，符号：\not\subset，如：$x \not\subset y$
非子集运算，符号：\not\supset，如：$x \not\supset y$
并集运算，符号：\cup，如：$x \cup y$
交集运算，符号：\cap，如：$x \cap y$
差集运算，符号：\setminus，如：$x \setminus y$
同或运算，符号：\bigodot，如：$x \bigodot y$
同与运算，符号：\bigotimes，如：$x \bigotimes y$
空集，符号：\emptyset，如：$\emptyset$
其他：$\bigvee$；$\bigwedge$
# 数学符号
无穷，符号：\infty，如：$\infty$
数学符号，符号\hat{a}，如：$\hat{a}$
数学符号，符号\check{a}，如：$\check{a}$
数学符号，符号\breve{a}，如：$\breve{a}$
数学符号，符号\tilde{a}，如：$\tilde{a}$
数学符号，符号\bar{a}，如：$\bar{a}$
矢量符号，符号\vec{a}，如：$\vec{a}$
数学符号，符号\acute{a}，如：$\acute{a}$
数学符号，符号\grave{a}，如：$\grave{a}$
数学符号，符号\mathring{a}，如：$\mathring{a}$
一阶导数符号，符号\dot{a}，如：$\dot{a}$
二阶导数符号，符号\ddot{a}，如：$\ddot{a}$
上箭头，符号：\uparrow，如：$\uparrow$
上箭头，符号：\Uparrow，如：$\Uparrow$
下箭头，符号：\downarrow，如：$\downarrow$
下箭头，符号：\Downarrow，如：$\Downarrow$
左箭头，符号：\leftarrow，如：$\leftarrow$
左箭头，符号：\Leftarrow，如：$\Leftarrow$
右箭头，符号：\rightarrow，如：$\rightarrow$
右箭头，符号：\Rightarrow，如：$\Rightarrow$
底端对齐的省略号，符号：\ldots，如：$1,2,\ldots,n$
中线对齐的省略号，符号：\cdots，如：$x_1^2 + x_2^2 + \cdots + x_n^2$
竖直对齐的省略号，符号：\vdots，如：$\vdots$
斜对齐的省略号，符号：\ddots，如：$\ddots$

# 其他
## max
$$\max_{a<x<b}\{f(x)\}$$
## 方程式
$$
c(x)=
\begin{cases}
\sqrt{x},x>=0 \\
x^2,x<0
\end{cases}
$$
$$
c(x)=\left\{\begin{aligned}
\sqrt{x} &, x>=0 \\
x^2 &, x<0
\end{aligned}
\right.
$$

## 矩阵
在起始、结束标记处用下列词替换matrix
pmatrix ：小括号边框
bmatrix ：中括号边框
Bmatrix ：大括号边框
vmatrix ：单竖线边框
Vmatrix ：双竖线边框
横省略号：\cdots
竖省略号：\vdots
斜省略号：\ddots
例如
$$
X=\left|
    \begin{matrix}
x_{11} & x_{12} & \cdots & x_{1n}\\
x_{21} & x_{22} & \cdots & x_{2n}\\
\vdots & \vdots & \ddots & x_{1n}\\
x_{n1} & x_{n2} & \cdots & x_{nn}
    \end{matrix}
    \right|
$$
## 等号对齐
$$
\begin{aligned}
a+b+c&=d\\
e+f&=g
\end{aligned}
$$

## 希腊字母
大写	Markdown	小写	Markdown
A	A	α	\alpha
B	B	β	\beta
Γ	\Gamma	γ	\gamma
Δ	\Delta	δ	\delta
E	\Epsilon	ϵ	\epsilon
ε	\varepsilon		
Z	\Zeta	ζ	\zeta
H	\Eta	η	\eta
Θ	\Theta	θ	\theta
I	\lota	ι	\iota
K	\Kappa	κ	\kappa
Λ	\Lambda	λ	\lambda
M	\Mu	μ	\mu
N	\Nu	ν	\nu
Ξ	\Xi	ξ	\xi
O	O	ο	\omicron
Π	\Pi	π	\pi
P	\Rho	ρ	\rho
Σ	\Sigma	σ	\sigma
T	\Tau	τ	\tau
Υ	\Upsilon	υ	\upsilon
Φ	\Phi	ϕ	\phi
φ	\varphi		
X	\Chi	χ	\chi
Ψ	\Psi	ψ	\psi
Ω	\Omega	ω	\omega
