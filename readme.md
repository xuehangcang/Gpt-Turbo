# Gpt-Turbo


基于 fastapi 的 gpt-3.5-turbo 项目, 用于快速部署,方便API请求调试，来执行以下操作：

- 起草电子邮件或其他书面文件
- 编写 Python 代码
- 回答有关一组文件的问题
- 创建会话代理
- 为您的软件提供自然语言界面
- 一系列科目的导师
- 翻译语言
- 模拟视频游戏中的角色等等

## 请求示例

```python

import requests

params = {
    "api_key": "OpenAi API 密钥",  # https://platform.openai.com/
    "user_content": " Python 编程语言编写一道程序题",
}
r = requests.get("https://gptturbo.top", params=params)
print(r.json())

"""
{
    'id': 'chatcmpl-6pVJffpbAwOm0Isf8McQ9JPLB43Ds',
    'object': 'chat.completion',
    'created': 1677733127,
    'model': 'gpt-3.5-turbo-0301',
    'usage': {
        'prompt_tokens': 29,
        'completion_tokens': 295,
        'total_tokens': 324
    },
    'choices': [
        {
            'message': {
                'role': 'assistant',
                'content': '题目：\n\n编写一个程序，对于用户输入的一段文本，统计其中单词出现的次数并输出出现次数最多的前 5 个单词及其出现次数。\n\n要求：\n\n1. 仅考虑英文单词，多个单词之间以空格或者标点符号分隔。\n\n2. 对于大小写不同但拼写相同的单词，算作同一个单词。\n\n3. 输出结果按照单词出现的次数从大到小排序。\n\n4. 仅考虑该文本中出现频率最高的前 5 个不同单词。\n\n示例：\n\n输入：hello world, my name is John. I love programming very much. Python is my favorite language.\n\n输出：\n\n1. my: 2\n2. is: 1\n3. name: 1\n4. world: 1\n5. love: 1\n\n解释：\n\n单词 my 出现了 2 次，是出现次数最多的单词；其他出现次数相同的单词名次由字典序决定，例如 is 名次排在 name 前面。'
            },
            'finish_reason': 'stop',
            'index': 0
        }
    ]
}

"""
```



## 参数解释

聊天模型将一系列消息作为输入，并返回模型生成的消息作为输出。

主要输入是消息参数。消息必须是一组消息对象，其中每个对象都有一个角色（“系统”、“用户”或“助手”）和内容（消息的内容）

- api_key  OpenAi API 密钥
- user_content  用户消息有助于指导助手
- system_content 系统消息有助于设置助手的行为
- assistant_content 助手消息帮助存储先前的响应_

