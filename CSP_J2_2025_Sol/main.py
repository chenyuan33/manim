from manim import *


class CSP_J2_2025_Sol(Scene):
	def construct(self):
		title = Text('2025 CSP-J2 视频题解')
		self.play(Write(title), run_time=1)
		title_sep = Line(UP * 2 + LEFT * 3, UP * 2 + RIGHT * 3)
		self.play(title.animate.shift(UP * 2.5), run_time=0.5)
		self.play(title.animate.scale(0.7), Create(title_sep), run_time=1)

		title1 = Text('T1. 拼数 / number').shift(UP * 2.5).scale(0.7)
		self.play(ReplacementTransform(title, title1), run_time=1)
		algo_step = Text('算法步骤 / Algorithm Steps').shift(UP * 1.6 + RIGHT * 2.5).scale(0.6)
		algo_step_sep = Line(UP * 2, DOWN * 3)
		self.play(Create(algo_step), Create(algo_step_sep), run_time=1)
		how_sample = Text('290es1q0').shift(LEFT * 2.5)
		self.play(Write(how_sample), run_time=1)
		how_sample2 = Text('290es1q0', t2c={'[0:3]': RED, '[5:6]': RED, '[7:]': RED}).shift(LEFT * 2.5)
		self.play(ReplacementTransform(how_sample, how_sample2), run_time=1)
		how_sample3 = Text('290es1q0', t2c={
			'[0:3]': RED,
			'[3:5]': BLACK,
			'[5:6]': RED,
			'[6:7]': BLACK,
			'[7:]': RED
		}).shift(LEFT * 2.5)
		self.play(ReplacementTransform(how_sample2, how_sample3), run_time=1)
		algo_step1 = Paragraph(
			'1. 删去不必要的非数字字符',
			'Remove unnecessary non-numeric characters'
		).shift(RIGHT * 3.5).scale(0.5)
		how_sample4 = Text('29010', color=RED).shift(LEFT * 2.5)
		self.play(Create(algo_step1), ReplacementTransform(how_sample3, how_sample4), run_time=1)
		algo_step2 = Paragraph(
			'2. 从大到小对每个数字进行排序',
			'Sort each digit from largest to smallest.'
		).shift(DOWN + RIGHT * 3).scale(0.5)
		how_sample5 = Text('92100', color=RED).shift(LEFT * 2.5)
		self.play(Create(algo_step2), ReplacementTransform(how_sample4, how_sample5), run_time=1)
		self.play(Unwrite(how_sample5), Unwrite(algo_step1), Unwrite(algo_step2), run_time=1)

		title2 = Text('T2. 座位 / seat').shift(UP * 2.5).scale(0.7)
		self.play(ReplacementTransform(title1, title2), run_time=1)
		how_sample = Paragraph('94 95 96', '97 98 99', '100 93 92', t2c={'94': RED}).shift(LEFT * 3)
		self.play(Write(how_sample), run_time=1)
		algo_step1 = Paragraph(
			'1. 携带着一号的位置从大到小排序',
			'Sort the positions carrying the No. 1',
			'from largest to smallest.'
		).shift(RIGHT * 3).scale(0.5)
		how_sample1 = Paragraph('100 99 98', '97 96 65', '94 93 92', t2c={'94' : RED}).shift(LEFT * 3)
		self.play(Write(algo_step1), ReplacementTransform(how_sample, how_sample1), run_time=1)
		how_sample2 = VGroup()
		for i in range(2, 5):
			for j in range(-1, 2):
				how_sample2.add(Square(1).shift(LEFT * i + UP * j))
		self.play(Create(how_sample2), how_sample1.animate.shift(DOWN * 2.5).scale(0.75), run_time=1)
		algo_step2 = Paragraph(
			'2. 依照题意模拟或计算出一号的位置',
			'Simulate or calculate the position of No. 1',
			'according to the problem statement.'
		).shift(DOWN + RIGHT * 3.5).scale(0.5)
		self.play(Create(algo_step2), run_time=1)
		how_sample3 = VGroup()
		for i in range(0, 9):
			how_sample4 = Text(str(100 - i)).shift(
				LEFT * (4 - i // 3) + UP * (i % 3 - 1 if i // 3 % 2 else 1 - i % 3)
			)
			if i == 6:
				how_sample4.set_color(RED)
			self.play(Write(how_sample4), run_time=1/9)
			how_sample3.add(how_sample4)
		algo_step3 = VGroup(
			Text('列和行的公式分别为：'),
			Text('The formulas for columns and rows are respectively:'),
			VGroup(Text('列 / Columns: '), Tex(r'$\left\lfloor\frac{x-1}n\right\rfloor+1$')),
			VGroup(Text('行（对于奇数列）/ Rows (for odd-numbered columns): '), Tex(r'$(x-1)\bmod n+1$')),
			VGroup(Text('行（对于偶数列）/ Rows (for even-numbered columns): '), Tex(r'$n-(x-1)\bmod n$'))
		)
		for i in range(2, 5):
			algo_step3[i].arrange(RIGHT, 0.1)
		algo_step3.arrange(DOWN, 0, aligned_edge=LEFT)
		algo_step3 = algo_step3.shift(DOWN * 2.5).scale(0.5)
		self.play(ReplacementTransform(how_sample1, algo_step3), run_time=1)
		self.play(
			Uncreate(how_sample2),
			Unwrite(how_sample3),
			Unwrite(algo_step1),
			Unwrite(algo_step2),
			Unwrite(algo_step3),
			run_time=1
		)

		title3 = Text('T3. 异或和 / xor').shift(UP * 2.5).scale(0.7)
		self.play(ReplacementTransform(title2, title3), run_time=1)
		algo_60pts = Text('60pts 做法 / 60-Points Method').shift(UP * 1 + RIGHT * 3.25).scale(0.65)
		self.play(Write(algo_60pts), run_time=1)
		how_sample = Text('2 1 0 3').shift(LEFT * 1.5)
		how_sample1 = Tex('$k=3$').shift(LEFT * 4 + UP)
		self.play(Write(how_sample), Write(how_sample1), run_time=1)
		how_sample2 = VGroup(
			Text('2', color=RED), Text('1', color=RED),
			Text('0'), Text('3', color=BLUE)
		)
		how_sample2.arrange()
		how_sample2 = how_sample2.shift(LEFT * 1.5)
		self.play(ReplacementTransform(how_sample, how_sample2), run_time=1)
		how_sample3 = VGroup(
			Rectangle(RED, 0.5, 1).shift(LEFT * 2),
			Rectangle(BLUE, 0.5, 0.5).shift(LEFT * 0.75),
			Text('3', color=RED).shift(LEFT * 2 + UP),
			Text('3', color=BLUE).shift(LEFT * 0.75 + UP)
		)
		how_sample2_2 = VGroup(
			Text('2', color=RED), Text('1', color=RED),
			Text('0'), Text('3', color=BLUE)
		)
		how_sample2_2.arrange()
		how_sample2_2.shift(LEFT * 1.5)
		how_sample2_3 = VGroup(
			Text('2', color=RED), Text('1', color=RED),
			Text('0'), Text('3', color=BLUE)
		)
		how_sample2_3.arrange()
		how_sample2_3.shift(LEFT * 1.5)
		self.play(Write(how_sample2_2), Write(how_sample2_3), Create(how_sample3), run_time=1)
		algo_60pts_step1 = Paragraph(
			'1. 预处理前缀异或和',
			'Preprocessing Prefix XOR Sum'
		).shift(RIGHT * 3).scale(0.65)
		self.play(Write(algo_60pts_step1), run_time=1)
		how_sample4 = VGroup(Text('0'), Text('2'), Text('3'), Text('3'), Text('0'))
		how_sample4.arrange()
		how_sample4 = how_sample4.shift(DOWN + LEFT * 2)
		how_sample4_2 = VGroup(Text('0'), Text('2'), Text('3'), Text('3'), Text('0'))
		how_sample4_2.arrange()
		how_sample4_2 = how_sample4_2.shift(DOWN + LEFT * 2)
		self.play(Write(how_sample4[0]), Write(how_sample4_2[0]), run_time=0.2)
		for i in range(4):
			self.play(ReplacementTransform(VGroup(how_sample2_3[i], how_sample4[i]), how_sample4[i + 1]), run_time=0.2)
			self.add(how_sample4_2[i + 1])
		self.play(
			Unwrite(how_sample2),
			Unwrite(how_sample2_2),
			Unwrite(how_sample2_3),
			Unwrite(how_sample4),
			how_sample3.animate.shift(LEFT * 0.25),
			how_sample4_2.animate.shift(UP),
			run_time=1
		)
		how_sample5 = VGroup(
			Text('0', color=RED), Text('2'), Text('3', color=RED),
			Text('3', color=BLUE), Text('0', color=BLUE)
		)
		how_sample5.arrange()
		how_sample5 = how_sample5.shift(LEFT * 2)
		self.play(ReplacementTransform(how_sample4_2, how_sample5), run_time=1)
		how_sample6 = VGroup(Text('0'), Text('2'), Text('3'), Text('3'), Text('0'))
		how_sample6.arrange()
		how_sample6 = how_sample6.shift(LEFT * 2)
		self.play(
			Uncreate(how_sample3),
			ReplacementTransform(how_sample5, how_sample6),
			run_time=1
		)
		how_sample7 = VGroup(Text('0'), Text('0'), Text('1'), Text('1'), Text('2'))
		how_sample7.arrange()
		how_sample7 = how_sample7.shift(LEFT * 2 + DOWN)
		how_sample7_copy = VGroup(Text('0'), Text('0'), Text('1'), Text('1'), Text('2'))
		how_sample7_copy.arrange()
		how_sample7_copy = how_sample7_copy.shift(LEFT * 2 + DOWN)
		how_sample7_last = VGroup(Text('0'), Text('0'), Text('0'), Text('1'), Text('1'))
		for i in range(5):
			how_sample7_last[i].shift(RIGHT * how_sample7[i].get_x() + UP * how_sample7[i].get_y())
		self.play(Write(how_sample7[0]), Write(how_sample7_copy[0]), run_time=1)
		how_sample7_inner = [-1, -1, 0, -1, 3]
		algo_60pts_step2 = VGroup(
			VGroup(Text('2. 动态规划：令'), Tex('$f_i$'), Text('为前'), Tex('$i$'), Text('个数的答案。')),
			VGroup(
				Text('Dynamic Programming: Let'), Tex('$f_i$'), Text('means the answer of first'), Tex('$i$'),
				Text('elements')
			),
			VGroup(Text('2.1. 不选 / Don\'t Select: '), Tex('$f_i=f_{i-1}$')),
			VGroup(
				Text('2.2. 选：找到这之前最后一个与当前异或和为', t2c={'最后一个': RED}), Tex('$k$'), Text('的位置'),
				Tex('$j$'), Text('，满足'), Tex('$f_i=f_j+1$')
			),
			VGroup(
				Text('Select: Find the last position', t2c={'last': RED}), Tex('$j$'), Text('before this one')
			),
			VGroup(
				Text('where the XOR sum with the current position equals'), Tex('$k$'),
				Text(', It is'), Tex('$f_i=f_j+1$')
			),
		)
		for i in range(0, 5):
			algo_60pts_step2[i].arrange()
		algo_60pts_step2.arrange(DOWN, aligned_edge=LEFT)
		algo_60pts_step2 = algo_60pts_step2.shift(DOWN * 3).scale(0.5)
		self.play(Write(algo_60pts_step2), run_time=1)
		for i in range(1, 5):
			self.play(
				ReplacementTransform(how_sample7_copy[i - 1], how_sample7_last[i]),
				how_sample6[i].animate.set_color(BLUE),
				run_time=1 / (i * 2 + 2)
			)
			for j in range(i if how_sample7_inner[i] == -1 else how_sample7_inner[i] + 1):
				self.play(
					how_sample6[j].animate.set_color(RED if j != how_sample7_inner[i] else GREEN), run_time=1 / (i * 2 + 2))
				if j == how_sample7_inner[i]:
					self.play(ReplacementTransform(
						how_sample7_last[i], how_sample7[i]), run_time=1 / (i * 2 + 2))
				self.play(how_sample6[j].animate.set_color(WHITE), run_time=1 / (i * 2 + 2))
			self.play(how_sample6[i].animate.set_color(WHITE), run_time=1 / (i * 2 + 2))
			if how_sample7_inner[i] == -1:
				self.add(how_sample7[i])
				self.remove(how_sample7_last[i])
			self.add(how_sample7_copy[i])
		algo_100pts = Text('100pts 做法 / 100-points Method').shift(RIGHT * 3.25 + UP * 1).scale(0.55)
		self.play(
			ReplacementTransform(algo_60pts, algo_100pts),
			Unwrite(algo_60pts_step1), run_time=1
		)
		algo_100pts_step = Paragraph(
			'3. 注意到动态规划时只需要知道每个数字出现的',
			'最后一个位置，因此可以用一个 map 存储每个',
			'数字最后的位置，达到优化的效果。',
			'Note that dynamic programming only requires',
			'knowing the last position where each digit',
			'appears. Therefore, a map can be used to store',
			'the last position of each digit achieving',
			'an optimized solution.'
		).shift(DOWN + RIGHT * 3.5).scale(0.5)
		self.play(Write(algo_100pts_step), run_time=1)
		self.play(
			Unwrite(how_sample1), Unwrite(how_sample6),
			Unwrite(how_sample7), Unwrite(how_sample7_copy),
			Unwrite(algo_60pts_step2), Unwrite(algo_100pts), Unwrite(algo_100pts_step),
			run_time=1
		)

		# 3 10 8 2 2
		title4 = Text('T4. 多边形 / polygon').shift(UP * 2.5).scale(0.7)
		self.play(ReplacementTransform(title3, title4))
		how_sample = Text('3 10 8 2 2').shift(LEFT * 2)
		self.play(Write(how_sample), run_time=1)
		how_sample1 = Text('2 2 3 8 10').shift(LEFT * 2)
		algo_step1 = Text('1. 排序 / Sort').shift(UP + RIGHT * 2).scale(0.5)
		self.play(
			ReplacementTransform(how_sample, how_sample1), Write(algo_step1), run_time=1)
		algo_step2 = VGroup(
			VGroup(Text('2. 移项，问题转化为对于每一个'), Tex(r'$3\le i\le n$')),
			VGroup(Text('以此为最大值，并在'), Tex('$i$'), Text('之前取至少三个')),
			VGroup(Text('使得总和大于当前的方案数之和。')),
			VGroup(Text('Transforming the problem, for each'), Tex(r'$3 \le i \le n$')),
			VGroup(Text('we seek the maximum value such that')),
			VGroup(Text('there exist at least three solutions before'), Tex('$i$')),
			VGroup(Text('where the sum exceeds the current value.'))
		)
		for i in range(len(algo_step2)):
			algo_step2[i].arrange()
		algo_step2.arrange(DOWN, aligned_edge=LEFT).shift(RIGHT * 3.5 + DOWN).scale(0.5)
		how_sample2 = Tex(r'$\sum_{i=1}^ml_i>2\times\max_{i=1}^ml_i$').shift(LEFT * 2 + DOWN)
		how_sample3 = Tex(r'$\sum_{i=1}^{m-1}l_i+l_m>2l_m$').shift(LEFT * 2 + DOWN)
		how_sample4 = Tex(r'$\sum_{i=1}^{m-1}l_i>l_m$').shift(LEFT * 2 + DOWN)
		self.play(Write(algo_step2), Write(how_sample2), run_time=1)
		self.play(ReplacementTransform(how_sample2, how_sample3), run_time=0.5)
		self.play(ReplacementTransform(how_sample3, how_sample4), run_time=0.5)
		algo_step3 = Paragraph(
			'3. 枚举最大值，背包求得每个数当前的可达成次数，枚举问题的反面求和。',
			'Enumerate the maximum value, calculate the current achievable count for',
			'each number using the knapsack problem, and sum the inverse of the problem.'
		).shift(DOWN * 3).scale(0.5)
		self.play(Write(algo_step3), run_time=1)
		self.play(
			Unwrite(title4), Unwrite(title_sep),
			Unwrite(algo_step), Unwrite(algo_step_sep),
			Unwrite(algo_step1), Unwrite(algo_step2), Unwrite(algo_step3),
			Unwrite(how_sample1), Unwrite(how_sample4),
			run_time=1
		)