# Day 001 — 2026-10-08 — Python Object Model

## 今日目标
object, reference, identity, mutable/immutable, namespace, scope

## 学习材料
- 主要来源：对应主题的官方文档 / 课程 / 视频
- 具体 URL：
- 完成章节 / 视频时间戳：
- 关键概念：

## Coding
Python 官方 Tutorial；手写 User/Message/Conversation/Tool 四个类

### 实现检查
- [ ] 从空目录开始
- [ ] 写测试
- [ ] 处理异常
- [ ] 做一次本地运行或 benchmark
- [ ] Git commit

## Algorithm
**Two Sum**

- [ ] 独立思考
- [ ] 写出复杂度
- [ ] 代码通过
- [ ] 不看答案复述思路

## 今日交付
建立项目目录；完成 day01 Python 对象模型笔记与代码

## 面试表达
用 3–5 句话回答：

> 今天学的内容是什么？
今天学习 Python 对象模型，包括：
object、reference、identity、mutable/immutable、namespace 和 scope。
并使用这些概念设计了一个简单 AI Agent 数据结构：
User → Conversation → Message → Tool。
> 为什么需要它？
因为真实工程中不是简单写代码，而是需要设计对象之间的关系。
理解对象和引用可以避免：
数据被错误修改
生命周期混乱
模块之间耦合
> 如果不用这个方案，还有什么选择？
例如：
不用 class：可以使用：dict、function、简单数据结构
但是大型项目中：class 可以封装数据和行为，提高维护性。
> 生产环境可能遇到什么问题？
可能遇到：对象状态管理复杂、模块依赖混乱、数据被非法修改、工具调用异常
所以需要：分层架构、类型检查、测试、异常处理

## 今日复盘

### 今天真正理解的 3 件事
1.变量不是对象本身，而是对象的引用。

2.函数也是对象。
所以：Tool("search", "搜索", search)
可以把函数作为能力传入。

3.软件设计核心是对象之间的关系。
Agent 本质：
Message
 ↓
Conversation
 ↓
Service
 ↓
Tool
### 今天卡住的地方
1.理解函数对象和函数调用
2.module namespace 问题

### 我解决问题的方法
查看 traceback
定位错误文件和行号
分析变量作用域
修改模块职责
### 明天第一件事
继续 Day002
## 证据
- GitHub commit：
- Demo / Screenshot：
- Benchmark：
- 测试数量 / 覆盖率：
- 学习时长：

## 完成度
- [ ] 学习材料
- [ ] Coding
- [ ] Algorithm
- [ ] Deliverable
- [ ] Git commit
- [ ] 日志
