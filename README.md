<!-- TOC -->

- [程序设计实践大作业#DSL](#程序设计实践大作业dsl)
  - [需求分析](#需求分析)
    - [1、相关介绍](#1相关介绍)
    - [2、基本要求](#2基本要求)
  - [项目规划](#项目规划)
    - [1、语法定义](#1语法定义)
    - [2、设计规划](#2设计规划)
  - [程序设计](#程序设计)
    - [1.服务端](#1服务端)
    - [2.客户端](#2客户端)
  - [项目测试](#项目测试)
    - [1.测试桩](#1测试桩)
    - [2.自动测试脚本](#2自动测试脚本)
  - [程序演示](#程序演示)
    - [1.启动服务端](#1启动服务端)
    - [2.启动客户端](#2启动客户端)
    - [3.发送消息](#3发送消息)

<!-- /TOC -->
# 程序设计实践大作业#DSL

班级：2019211308

学号：2019211496

姓名：韩世民

## 需求分析

### 1、相关介绍

    领域特定语言（Domain Specific Language，DSL）可以提供一种相对简单的文法，用
    于特定领域的业务流程定制。本作业要求定义一个领域特定脚本语言，这个语言能够描述在
    线客服机器人（机器人客服是目前提升客服效率的重要技术，在银行、通信和商务等领域的
    复杂信息系统中有广泛的应用）的自动应答逻辑，并设计实现一个解释器解释执行这个脚本，
    可以根据用户的不同输入，根据脚本的逻辑设计给出相应的应答。
### 2、基本要求
    脚本语言的语法可以自由定义，只要语义上满足描述客服机器人自动应答逻辑的要求。
    程序输入输出形式不限，可以简化为纯命令行界面。应该给出几种不同的脚本范例，对不同
    脚本范例解释器执行之后会有不同的行为表现。

## 项目规划
### 1、语法定义
1. ## Step XXX
        定义一个步骤，XXX为步骤名
2. ## Speak XXX$nameXXX$amount
        表示向客户端发送消息，其中$name和$amount为变量，会被具体的值替换
3. ## Listen XXX
        开始监听客户说话，并定义监听时长
4. ## Branch XXX YYY
        当监听到客户说话为XXX时，跳转到YYY分支
5. ## Silence XXX
        当监听到客户没有说话，既保持沉默时，跳转到XXX分支
6. ## Default XXX
        默认情况下跳转至XXX分支

### 2、设计规划
1. ## 前后端分离
        通过接口组织前后端交互
2. ## HTML+CSS+JS
        前端使用html+css+js实现，js负责与后端交互的逻辑，交互结果通过html+css在前端呈现
3. ## MySQL处理
        与MySQL数据库交互，模拟真实应用场景
4. ## WebSocket通信协议
        基于通信双方两者之间需要创建持久性的连接，并进行双向数据传输，用来实时通信的通信需求，WebSocket协议是不二之选，规划采用WebSocket协议进行服务端与客户端通信
5. ## 脚本解析
        整个脚本可以保存为由多个step构成的一个字典，其中键为step的名字，值为对应的step类，每个step可以看作是一个action列表，列表每个元素对应于一个action类的对象，由两个列表相互联系构造出脚本相应的语法解析树
6. ## 脚本执行
        定义step名为welcome的过程为入口过程，客户端连接服务端时，为每个客户端创建一个新的线程，连接完成后，先初始化连接信息，之后等待客户端在线程内轮询等待客户端发送消息以进入脚本执行过程。
        进入脚本执行过程后，再次为该客户端进程分配一个线程对脚本文件顺序执行，同时主线程持续接受用户信息，并通过两线程间共享的一个数据结构进行线程间通信，实现客户端与服务端的异步通信。
## 程序设计
### 1.服务端
1. ## MySQL处理
    ### 随机取出一条数据作为客户信息，只返回姓名，模拟实际应用场景中，客服系统应提前了解客户信息
    ```python
    def getName():
    db = pymysql.connect(host="localhost", user="user",
                         password="bupt1234", database='user')
    cursor = db.cursor()
    result = {}
    sql = "SELECT * FROM USER ORDER BY RAND() LIMIT 1"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchone()
        result['name'] = results[0]
        result['age'] = results[1]
        result['sex'] = results[2]
        result['balance'] = results[3]
    except:
        print("Error: unable to fetch data")
    db.close()
    return result['name']
    ```
    ### 通过姓名在数据库中检索相应的信息
    ```python
    def search(name):
    db = pymysql.connect(host="localhost", user="user",
                         password="bupt1234", database='user')
    cursor = db.cursor()
    result = {}
    # sql = """CREATE TABLE USER (
    #          NAME  CHAR(20) NOT NULL,
    #          AGE INT,
    #          SEX CHAR(1),
    #          BALANCE FLOAT )"""
    sql = "SELECT * FROM USER \
        WHERE NAME = '%s'" % (name)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchone()
        result['name'] = results[0]
        result['age'] = results[1]
        result['sex'] = results[2]
        result['balance'] = results[3]
    except:
        print("Error: unable to fetch data")
    db.close()
    return result
    ```
2. ## WebSocket通信协议与多线程
    ### 服务端监听本地9999端口，为访问该端口的程序解析请求，并创建线程创建相应的websocket连接
    ```python
    if not self.isInitialize:
        # 开始握手阶段
        header = self.analyzeReq()  # 分析请求头
        secKey = header['Sec-WebSocket-Key']
        acceptKey = self.generateAcceptKey(secKey)

        response = "HTTP/1.1 101 Switching Protocols\r\n"
        response += "Upgrade: websocket\r\n"
        response += "Connection: Upgrade\r\n"
        response += "Sec-WebSocket-Accept: %s\r\n\r\n" % (
            acceptKey.decode('utf-8'))
        self.con.send(response.encode())
        self.isInitialize = True
        self.myClient = client()
        print('response:\r\n' + response)

        self.sendDataToClient("2019211496"+self.myClient.name)
        # 握手阶段结束
    ```
    ### 解决编码问题。通过url编码，发送消息时编码，接受时解码，消除客户端服务端编码不一致带来的影响
    ```python
    opcode = self.getOpcode()

                if opcode == 8:
                    self.con.close()
                    return
                self.getDataLength()
                clientData = urllib.parse.unquote(self.readClientData())
                print('客户端数据：' + clientData)
                # 处理数据(测试桩 测试通信)
                # ans = self.answer(clientData)
                # self.sendDataToClient(ans)
                if(self.myClient.first == True):
                    self.myClient.first = False
                    t1 = threading.Thread(
                        target=self.FirstReceive, args=(clientData,))
                    t1.start()
                self.myClient.str = clientData
                self.myClient.Listening = False
                # self.sendDataToClient(clientData)
    ```
    ```python 
    def sendDataToClient(self, text):
        sendData = ''
        sendData = struct.pack('!B', 0x81)
        text = urllib.parse.quote(text)
        length = len(text)
        if length <= 125:
            sendData += struct.pack('!B', length)
        elif length <= 65536:
            sendData += struct.pack('!B', 126)
            sendData += struct.pack('!H', length)
        elif length == 127:
            sendData += struct.pack('!B', 127)
            sendData += struct.pack('!Q', length)

        sendData += struct.pack('!%ds' % (length), text.encode('utf8'))
        dataSize = self.con.send(sendData)
    ```
3. ## 线程间异步通信
        每个客户端主线程维护一个mClient对象，其中的属性str为当前客户端最新发送的消息，依赖这个共享的数据结构，实现主客户端线程和脚本执行线程的通信，实现异步通信
4. ## 解析脚本文件
        读取脚本文件，并将脚本文件解析为一个大的字典，每个字典项为一个step，每个step包含一个action列表，实际上是将脚本文件解析为一颗语法分析树
    ```python 
        def ParserFile(file):
        with open(file, encoding='utf8') as mfile:
            flag = True
            for str in mfile:
                str = str.strip()
                str = str.split(' ')
                if(str[0] == 'Step'):
                    if(flag == True):
                        flag = False
                    else:
                        StepList.addStep(step)
                    step = Step(str[1].strip())

                elif(str[0] == 'Speak'):
                    step.addAction(Speak(''.join(str[1:])))
                elif(str[0] == 'Listen'):
                    step.addAction(Listen(str[1]))
                elif(str[0] == 'Branch'):
                    step.addAction(Branch(str[1], str[2]))
                elif(str[0] == 'Silence'):
                    step.addAction(Silence(str[1]))
                elif(str[0] == 'Default'):
                    step.addAction(Default(str[1]))
                elif(str[0] == 'Exit'):
                    step.addAction(Exit())
            StepList.addStep(step)
        # for k in StepList.stepList.keys():
        #     for act in StepList.stepList[k].actionList:
        #         print(act.id)
        mfile.close()
    ```

5. ## 执行脚本文件
        mClient中维护一个stepName和一个num，分别标识当前位于哪个step和第几条action，依次执行脚本文件，直到Exit退出。
    ```python 
        def FirstReceive(self, str):
        mClient = self.myClient
        while(1):
            action = StepList.stepList[mClient.stepName].actionList[mClient.num]
            if(action.id == 0):
                self.sendDataToClient(action.run(mClient.name))
                mClient.num = mClient.num+1
            elif(action.id == 1):

                mClient.Listening = True
                mClient.str = ""
                num = action.time
                while num > 0 and mClient.Listening == True:
                    num = num-1
                    time.sleep(1)
                mClient.Listening = False
                mClient.num = mClient.num+1
            elif(action.id == 2):
                if(fuzz.partial_ratio(mClient.str, action.str) == 100):
                    mClient.stepName = action.name
                    mClient.num = 0
                else:
                    mClient.num = mClient.num+1
            elif(action.id == 3):
                if(mClient.str == ""):
                    mClient.stepName = action.name
                    mClient.num = 0
                else:
                    mClient.num = mClient.num+1
            elif(action.id == 4):
                mClient.stepName = action.name
                mClient.num = 0
            elif(action.id == 5):
                self.con.close()
                return
        ```
### 2.客户端
1. ## 客户端通信
```javascript
function connect() {
            var host = "ws://127.0.0.1:9999/";

            socket = new WebSocket(host);
            try {

                socket.onopen = function (msg) {
                    //alert("连接成功！");
                };

                socket.onmessage = function (msg) {
                    if (typeof msg.data == "string") {
                        displayContent(decodeURI(msg.data));
                    }
                    else {
                        alert("非文本消息");
                    }
                };

                socket.onerror = function (error) { alert("Error：" + error.name); };

                socket.onclose = function (msg) {
                    //关闭
                };
            }
            catch (ex) {
                log(ex);
            }
        }

        async function send() {
            var str = $("textToSend").value;
            if (str != "") {
                socket.send(encodeURI(str));
                $("textToSend").value = "";
                creatReceiver(str);
            } else {
                alert("发送内容不能为空！");
            }
        }
```
2. ## 根据通信结果动态改变前端页面
   ```javascript
   function creatSender(str) {
            $('chatBox-content-demo').insertAdjacentHTML('beforeend', '<div class="sender"><div> <img src="static/picture/1.png"> </div> <div> <div class="left_triangle"></div>  <span>' + str + '</span></div></div>');
            $('chatBox-content-demo').scrollTop = $('chatBox-content-demo').scrollHeight;
    }
    function creatReceiver(str) {
        $('chatBox-content-demo').insertAdjacentHTML('beforeend', '<div class="receiver"><div><img src="static/picture/2.png"></div><div> <div class="right_triangle"></div> <span>' + str + '</span></div></div>');
        $('chatBox-content-demo').scrollTop = $('chatBox-content-demo').scrollHeight;
    }
   ```
## 项目测试
### 1.测试桩
    使用简单函数为前后端通信模块提供数据进行测试
1. ## 通信测试桩
```python
    # 处理数据(测试桩 测试通信)
    # ans = self.answer(clientData)
    # self.sendDataToClient(ans)
    def answer(self, data):
        if(data[0:1] == "啊"):
            return "hello world"
        else:
            result = search(data[0:3])
            if("name" in result.keys()):
                return result['name']+"还有"+str(result['balance'])+"钱"
            else:
                return "说你"
```
2. ## 数据库测试桩
```python
    def answer(self, data):
        if(data[0:1] == "啊"):
            return "hello world"
        else:
            # 数据库(测试桩 测试数据库搜索)
            # result=search("韩高轩")
            result = search(data[0:3])
            if("name" in result.keys()):
                return result['name']+"还有"+str(result['balance'])+"钱"
            else:
                return "说你"
```
3. ## 服务端测试桩
    使用[websocket在线连接](http://www.jsons.cn/websocket/)平台进行测试websocket协议测试
### 2.自动测试脚本
    使用JavaScript编写前端脚本，在前端连接后自动向后端发送消息，进行自动测试。
```javascript
test()
async function test() {
    $("textToSend").value="测试";
    $("sendinput").click();
    await sleep(2000);
    $("textToSend").value="测试";
    $("sendinput").click();
    await sleep(2000);
    $("textToSend").value="测试";
    $("sendinput").click();
    await sleep(2000);
}
```
## 程序演示
### 1.启动服务端
![](http://10.112.112.240:8081/2019211496/dsl/-/raw/main/pic/1.png)
### 2.启动客户端
![](http://10.112.112.240:8081/2019211496/dsl/-/raw/main/pic/2.png)
### 3.发送消息
![](http://10.112.112.240:8081/2019211496/dsl/-/raw/main/pic/3.png)


