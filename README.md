# GlucoseObservedWithLinebot
Use line bot and python make a sample for glucose observed



糖尿病患飲食助手  

II.	使用套件   
1.	Flask: 用Python編寫的輕量級網頁應用框架  
2.	Lnebot: Line官方提供的API套件，用於連接line  
3.	tempfile: 創建臨時文件與資料夾用  
4.	os: 處理文件與目錄  
5.	matplotlib: 視覺化資料  
6.	json: 分析json格視使用  
7.	pyimgur: 連結imgur與python的套件 
8.	numpy: 方便陣列的操作  

III.	功能簡介  
這是一個簡易式觀測血糖變化的聊天機器人，透過使用端輸入食物名稱以及進食的數量，根據這些資料做運算與分析，回傳這種食物的基本數據以及分析結果(有圖形化結果)
操作指令說明:  
help:  觀測此機器人的功能  
food name '吃的分量': 注意這個格式是固定的(目前食物只有190種)  
舉例:   white rice 200，表示吃 white rice 200 gram  

	使用Heroku架server:  
	可以用git來佈署程式碼  
	連結line的一個中轉網站  
	減少維護管理系統底層的成本  
	操作相對簡單  

	使用Matplotlib圖像化分析數據:  
	可視畫的圖使人更理解內容  
	根據不同的食物與份量繪製不同的圖  

	使用Line message API:  
	用戶向LINE官方帳戶發送消息  
	LINE平台將webhook事件發送到bot服務器的webhook URL  
	根據webhook事件，bot服務器通過LINE平台響應用戶  

	Hovorka Model:  
	一種血糖模組  
	用食物所含的CHO份量可以計算人體將吸收多少  
	未來擴充至人工胰臟比較方便  

	Imgur Model:  
	用來上傳matplotlib的模組  
	上傳後可以得到一圖片網址  
	符合line API傳送圖片的規則  

IV.	Demo影片連結  


V.	參考資料
1.	莫凡Python  
2.	Model Predictive Control for Insulin Administration in People with Type 1 Diabetes - Miriam MN Nærum  
3.	https://yaoandy107.github.io/line-bot-tutorial/  
4.	https://xiaosean.github.io/chatbot/2018-04-10-LineChatbot/  
5.	https://medium.com/@skywalker0803r/line-bot%E5%8A%A9%E6%89%8B%E6%A9%9F%E5%99%A8%E4%BA%BA%E5%AF%A6%E4%BD%9C-893e24db0ab5  
6.	PyImgur  


