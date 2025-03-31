# SlimAIchatUI：极简AI聊天应用
SlimAIchatUI旨在为用户提供便捷的AI聊天体验，项目包含两个版本：JavaScript前端直连版与Python后端代理版。前者通过JavaScript在前端直接调用OpenRouter API，后者借助Python Flask框架搭建后端服务，实现API请求的转发。

## 特性
1. **精简设计**：采用极简的界面设计与交互逻辑，专注于核心聊天功能。
2. **流式响应**：实现实时的流式响应，让用户在对话过程中获得即时反馈。
3. **多版本支持**：提供JavaScript前端直连和Python后端代理两种部署方案，满足不同场景需求。

## 目录结构
```plaintext
SlimAIchatUI/
├── js实现/
│   ├── index.html
├── python后端/
│   ├── app.py
│   ├── index.html
└── README.md
```

## JavaScript前端直连版
### 概述
该版本直接在前端通过JavaScript代码调用OpenRouter API，简化了部署流程，实现快速上线。

### 部署
1. **获取API密钥**：从OpenRouter官网获取有效的API密钥。
2. **配置密钥**：打开`js实现/index.html`文件，找到API密钥配置部分，将获取的密钥填入相应位置。
3. **打开页面**：在浏览器中直接打开`index.html`文件，即可开始使用。

## Python后端代理版
### 概述
该版本使用Python Flask框架搭建后端服务，负责转发API请求，增强了安全性和可扩展性。

### 部署
1. **安装依赖**：确保系统已安装Python，进入`python后端`目录，执行`pip install flask openai`安装所需依赖。
2. **获取API密钥**：从OpenRouter官网获取有效的API密钥。
3. **配置密钥**：打开`python后端/app.py`文件，找到API密钥配置部分，将获取的密钥填入相应位置。
4. **启动服务**：在`python后端`目录下执行`python app.py`启动后端服务。
5. **访问应用**：打开浏览器，访问`http://127.0.0.1:5000`，即可开始使用。

## 贡献
1. **提交问题**：如在使用过程中发现问题或有新的功能需求，欢迎在GitHub上提交issue。
2. **提交代码**：如需提交代码改进项目，可发起pull request，我会尽快进行审核。
