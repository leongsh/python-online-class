import streamlit as st
import streamlit.components.v1 as components

# -------------------------------------------
# 初始化（session state）
# -------------------------------------------
if 'cart' not in st.session_state:
	# 購物車：儲存每項商品為 dict {'name':..., 'price':...}
	st.session_state.cart = []

if 'quiz_score' not in st.session_state:
	st.session_state.quiz_score = None

if 'quiz_attempts' not in st.session_state:
	st.session_state.quiz_attempts = 0


def sidebar_nav():
	"""建立側邊欄導航選單，回傳所選頁面標識字串"""
	st.sidebar.title("導覽")
	page = st.sidebar.radio("選擇章節：",
							["首頁", "Ch1: 變數與資料型態", "Ch2: 邏輯判斷與迴圈", "Ch3: 資料結構 (List/Dict)", "期末測驗"]) 
	return page


def page_home():
	"""首頁：歡迎詞與學習 Python 的理由（使用 expander 展開說明）"""
	st.title("歡迎來到 Python 互動式學習網站 🎉")
	st.write("這個網站示範了基礎的 Python 概念與練習。請使用左側選單切換章節。")

	with st.expander("為什麼要學 Python？點此展開說明"):
		st.write("""
		- Python 是簡潔且易讀的程式語言，適合初學者。
		- 廣泛應用於資料分析、機器學習、網路開發、自動化等領域。
		- 入門後可以快速寫出有用的小工具，提升學習與工作效率。
		""")


def page_ch1():
	"""Ch1：變數與資料型態 + BMI 計算器（示範字串與整數）"""
	st.header("Ch1: 變數與資料型態")
	st.subheader("基本說明")
	st.write("在 Python 中，常見的資料型態包括：整數 (`int`)、浮點數 (`float`)、字串 (`str`) 等。")

	st.markdown("**字串（String）範例**")
	st.code("name = 'Alice'  # 這是一個字串")

	st.markdown("**整數（Integer）範例**")
	st.code("age = 20  # 這是一個整數")

	st.subheader("BMI 計算器（練習）")
	st.write("請輸入身高（公分）與體重（公斤），即時計算 BMI。")

	# 使用表單來讓使用者輸入
	with st.form(key='bmi_form'):
		height_cm = st.number_input('身高 (公分)', min_value=50.0, max_value=250.0, value=170.0, step=0.5)
		weight_kg = st.number_input('體重 (公斤)', min_value=10.0, max_value=300.0, value=65.0, step=0.1)
		submit = st.form_submit_button('計算 BMI')

	if submit:
		# 將身高從公分轉為公尺後計算 BMI
		height_m = height_cm / 100.0
		bmi = weight_kg / (height_m ** 2)
		bmi_display = round(bmi, 2)
		st.success(f"你的 BMI 為：{bmi_display}")

		# 根據 BMI 顯示體重分類
		if bmi < 18.5:
			category = '過輕'
		elif bmi < 24:
			category = '理想體重'
		elif bmi < 27:
			category = '過重'
		elif bmi < 30:
			category = '輕度肥胖'
		else:
			category = '肥胖'
		st.info(f"判定結果：{category}")

		# 顯示對應的 Python 範例程式碼並用中文註解解說
		code_example = f"""# 將身高從公分轉為公尺
height_m = {height_cm} / 100.0

# 計算 BMI
bmi = {weight_kg} / (height_m ** 2)

print(round(bmi, 2))  # 印出 BMI，保留兩位小數
"""
		st.subheader('對應的 Python 範例代碼（含註解）')
		st.code(code_example)


def page_ch2():
	"""Ch2：邏輯判斷 if/else 與 for 迴圈，互動畫星星金字塔"""
	st.header("Ch2: 邏輯判斷與迴圈")
	st.subheader("if / else 範例說明")
	st.write("if/else 用於根據條件執行不同分支的程式碼，例如：")
	st.code("if score >= 60:\n    print('及格')\nelse:\n    print('不及格')")

	st.subheader("for 迴圈說明")
	st.write("for 迴圈常用來重複執行程式區塊，例如走訪清單中的每個元素：")
	st.code("for item in ['apple', 'banana']:\n    print(item)")

	st.subheader("互動練習：畫星星（金字塔形狀）")
	levels = st.slider('選擇金字塔層數', min_value=1, max_value=20, value=5)

	# 產生金字塔星星（以文字方式顯示）
	pyramid_lines = []
	for i in range(1, levels + 1):
		# 每一層的星星數為 2*i - 1，前面加上空白讓它呈現置中效果
		spaces = ' ' * (levels - i)
		stars = '*' * (2 * i - 1)
		pyramid_lines.append(spaces + stars)

	# 使用等寬字型（code block）顯示金字塔
	st.code('\n'.join(pyramid_lines))

	st.subheader('示範程式碼（如何產生金字塔）')
	st.code("""levels = 5
for i in range(1, levels+1):
	spaces = ' ' * (levels - i)
	stars = '*' * (2*i - 1)
	print(spaces + stars)
""")


def page_ch3():
	"""Ch3：List 與 Dictionary 介紹，並實作超市購物車模擬"""
	st.header("Ch3: 資料結構 (List / Dict)")
	st.subheader("List（列表）")
	st.write("List 用來儲存一系列有順序的資料，可以用索引存取，例如：")
	st.code("fruits = ['apple', 'banana', 'cherry']\\nprint(fruits[0])  # 輸出 'apple'")

	st.subheader("Dictionary（字典）")
	st.write("Dictionary 用鍵值對（key:value）儲存資料，常用於表示物件屬性：")
	st.code("person = {'name': 'Amy', 'age': 30}\\nprint(person['name'])  # 輸出 'Amy'")

	st.markdown("---")
	st.subheader("超市購物車模擬（將水果加入購物車）")

	with st.form('add_item_form'):
		item_name = st.text_input('水果名稱', value='apple')
		item_price = st.number_input('價格（元）', min_value=0.0, value=10.0, step=0.5)
		add = st.form_submit_button('加入購物車')

	if add:
		# 把商品加入 session_state.cart
		st.session_state.cart.append({'name': item_name, 'price': float(item_price)})
		st.success(f"已加入：{item_name}，價格：{item_price} 元")

	# 顯示購物車內容
	st.write('目前購物車：')
	if len(st.session_state.cart) == 0:
		st.info('購物車目前是空的，可以加入第一項商品。')
	else:
		total = sum(item['price'] for item in st.session_state.cart)
		# 以表格方式顯示每項商品
		st.table([{ '名稱': it['name'], '價格': it['price'] } for it in st.session_state.cart])
		st.markdown(f"**總金額： {total:.2f} 元**")

		if st.button('清空購物車'):
			st.session_state.cart = []
			st.success('購物車已清空')


def page_quiz():
	"""期末測驗：三題選擇題，使用 st.form 和 session_state 記錄分數"""
	st.header('期末測驗')
	st.write('請完成下列 3 題選擇題，提交後會顯示分數與回饋。')

	# 題目資料結構：題目、選項、正確答案
	questions = [
		{
			'q': '哪一個是 Python 的註解（comment）？',
			'options': ['// 這是註解', '# 這是註解', '/* 註解 */'],
			'answer': '# 這是註解'
		},
		{
			'q': '下列哪個可以建立一個空的 List？',
			'options': ['{}', '()', '[]'],
			'answer': '[]'
		},
		{
			'q': '下列哪個語句用來迭代（iterate）序列？',
			'options': ['if', 'for', 'def'],
			'answer': 'for'
		}
	]

	# 使用表單收集答案
	with st.form('quiz_form'):
		answers = []
		for i, ques in enumerate(questions):
			ans = st.radio(f"Q{i+1}: {ques['q']}", ques['options'], key=f'q{i}')
			answers.append(ans)
		submit_quiz = st.form_submit_button('提交測驗')

	if submit_quiz:
		# 計分
		correct = 0
		for ans, ques in zip(answers, questions):
			if ans == ques['answer']:
				correct += 1

		score = int(round((correct / len(questions)) * 100))
		st.session_state.quiz_score = score
		st.session_state.quiz_attempts += 1

		st.write(f'你答對了 {correct} / {len(questions)} 題，分數：{score} 分')

		# 依分數給予回饋
		if score == 100:
			st.success('太棒了！滿分！🎉')
			# 放煙火（使用 balloons 並加入簡易 confetti）
			st.balloons()
			# 載入簡單的 confetti JS
			confetti_html = """
			<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
			<script>
			confetti({ particleCount: 200, spread: 160 });
			</script>
			"""
			components.html(confetti_html, height=0)
		elif score >= 70:
			st.success('很好！通過了。繼續保持練習！')
		else:
			st.info('別氣餒，多練習就會進步！可以回到章節複習後再挑戰。')

		# 顯示正確答案與解說
		st.markdown('**正解**')
		for i, ques in enumerate(questions):
			st.write(f"Q{i+1} 正解：{ques['answer']}")


def main():
	st.set_page_config(page_title='Python 互動式學習網站', layout='wide')
	page = sidebar_nav()

	if page == '首頁':
		page_home()
	elif page == 'Ch1: 變數與資料型態':
		page_ch1()
	elif page == 'Ch2: 邏輯判斷與迴圈':
		page_ch2()
	elif page == 'Ch3: 資料結構 (List/Dict)':
		page_ch3()
	elif page == '期末測驗':
		page_quiz()


if __name__ == '__main__':
	main()

