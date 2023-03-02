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

请求
```bash
curl -X 'GET' \
  'http://127.0.0.1:9000/?api_key=OpenAi API 密钥&user_content=%E4%BB%80%E4%B9%88%E6%98%AFBERT' \
  -H 'accept: application/json'
```

响应
```json
{
  "id": "chatcmpl-6pUTqNeTo7ZajPBrzIcEPF4D2p1hd",
  "object": "chat.completion",
  "created": 1677729914,
  "model": "gpt-3.5-turbo-0301",
  "usage": {
    "prompt_tokens": 22,
    "completion_tokens": 203,
    "total_tokens": 225
  },
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "BERT是Bidirectional Encoder Representations from Transformers的缩写，是一种基于Transformer结构的深度双向预训练语言模型的代表性模型。它是由Google提出的，继承了Transformer的自注意力机制，通过预训练将大量的文本数据编码成向量表示，并通过Fine-tune的方式适应于各种下游任务，如文本分类、情感分析、问答系统等。BERT支持双向处理文本上下文，可以更好地理解上下文信息，从而提高了NLP任务的准确性。BERT的出现引起了自然语言处理领域的极大关注，并成为了语言模型的研究热点之一。"
      },
      "finish_reason": "stop",
      "index": 0
    }
  ]
}
```


## 参数解释

聊天模型将一系列消息作为输入，并返回模型生成的消息作为输出。

主要输入是消息参数。消息必须是一组消息对象，其中每个对象都有一个角色（“系统”、“用户”或“助手”）和内容（消息的内容）

- api_key  OpenAi API 密钥
- user_content  用户消息有助于指导助手
- system_content 系统消息有助于设置助手的行为
- assistant_content 助手消息帮助存储先前的响应_

